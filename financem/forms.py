from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Usuário')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        # Realizar validações personalizadas no campo username
        if len(username) < 3:
            raise forms.ValidationError('O nome de usuário é muito curto.')
        return username
