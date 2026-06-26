from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Event, Registration
from django.views import View
from django import forms
from django.contrib import messages
from django.urls import reverse_lazy
# Create your views here.

class EventListView(ListView):
    model = Event
    template_name = 'eventi/event_list.html'
    context_object_name = 'events'
    def get_queryset(self):
        return Event.objects.all().order_by('date')

class EventDetailView(DetailView):
    model = Event
    template_name = 'eventi/event_detail.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['is_registered'] = Registration.objects.filter(
                user=self.request.user,
                event=self.get_object()
            ).exists()
        return context

class EventCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Event
    template_name = 'eventi/event_form.html'
    fields = ['title', 'description', 'date', 'location']
    success_url = reverse_lazy('eventi:event_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['date'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'})
        return form

    def test_func(self):
        return self.request.user.role == 'organizer'

    def handle_no_permission(self):
        messages.error(self.request, 'Accesso negato, solo gli organizzatori possono aggiungere eventi')
        return redirect('eventi:event_list')

    def form_valid(self, form):
        form.instance.organizer = self.request.user
        return super().form_valid(form)

class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    template_name = 'eventi/event_form.html'
    fields = ['title', 'description', 'date'] #location
    success_url = reverse_lazy('eventi:event_list')

    def test_func(self):
        obj = self.get_object()
        return obj.organizer == self.request.user

    def handle_no_permission(self):
        messages.error(self.request, "Accesso negato, puoi modificare solo gli eventi inseriti da te")
        return redirect('eventi:event_list')

class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    success_url = reverse_lazy('eventi:event_list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def test_func(self):
        obj = self.get_object()
        return obj.organizer == self.request.user



class BookEventView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        event = get_object_or_404(Event, pk=pk)

        if request.user.role != 'attendee':
            messages.error(request, 'Solo i partecipanti possono prenotare')
            return redirect('eventi:event_detail', pk=pk)

        registration, created = Registration.objects.get_or_create(user=request.user, event=event)

        if created:
            messages.success(request, 'Posto in sala prenotato con successo!')
        else:
            messages.info(request, 'Sei già prenotato per questo spettacolo.')

        return redirect('eventi:event_detail', pk=pk)


class CancelRegistrationView (LoginRequiredMixin, View):
    def post (self, request, pk, *args, **kwargs):
        event = get_object_or_404(Event, pk=pk)
        Registration.objects.filter(user=request.user, event=event).delete()
        messages.success(request, 'Prenotazione annullata')
        return redirect('eventi:event_detail', pk=pk)
class ProfileView(LoginRequiredMixin, View):
    template_name = 'eventi/profile.html'

    def get(self, request, *args, **kwargs):
        user_registrations = Registration.objects.filter(user=request.user).order_by('event__date')
        return render(request, self.template_name, {'user_registrations': user_registrations})