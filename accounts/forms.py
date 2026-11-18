from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import UserModel


class RegistrationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Shablonda bu maydonlar "required", serverda ham shunday bo'lsin
        for name in ('first_name', 'last_name', 'email'):
            self.fields[name].required = True


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'email', 'avatar')