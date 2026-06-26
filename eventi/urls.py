from django.urls import path
from .views import EventListView, EventDetailView, EventUpdateView, EventCreateView, EventDeleteView, BookEventView, CancelRegistrationView, ProfileView
app_name = 'eventi'
urlpatterns = [
    path('', EventListView.as_view(), name='event_list'),
    path('<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('event/create/', EventCreateView.as_view(), name='event_create'),
    path('event/<int:pk>/update/', EventUpdateView.as_view(), name='event_update'),
    path('event/<int:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),
    path('event/<int:pk>/book/',BookEventView.as_view(), name='book_event'),
    path('event/<int:pk>/cancel/', CancelRegistrationView.as_view(), name='cancel_registration'),
    path('profile/', ProfileView.as_view(), name='user_profile'),
]