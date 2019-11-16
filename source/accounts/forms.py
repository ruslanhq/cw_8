from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='Email', required=True)
    name = forms.CharField(max_length=20, label='Name', required=True)

    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email', 'name')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            User.objects.get(email=email)
            raise ValidationError('User with this email already exists', code='user_email_exists')
        except User.DoesNotExist:
            return email


