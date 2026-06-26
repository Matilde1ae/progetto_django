from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=False, label="Email")
    numero_telefono = forms.CharField(required=False, label="Numero Telefono")
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES, required=True, label="Registrati come")

    class Meta(UserCreationForm.Meta):
        model =CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'numero_telefono', 'role')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'username' in self.fields:
            self.fields['username'].help_text = ""
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Le password non coincidono!")
        return cleaned_data