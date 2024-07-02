from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormLogin(forms.Form):
    username = forms.CharField(label="Nom utilisateur",
                               widget=forms.TextInput(
                                   attrs={
                                       "class":"form-control"
                                   })
                                   )
    password = forms.CharField(label="Mot de passe",
                               widget=forms.PasswordInput(
                                   attrs={
                                       "class":"form-control"
                                   })
                                   )
    
class SignUpForm(UserCreationForm):
    username = forms.CharField(label="Nom utilisateur",
                               widget=forms.TextInput(
                                   attrs={
                                       "class": "form-control"
                                   })
                                   )
    email = forms.EmailField(label="Email",
                             widget=forms.EmailInput(
                                 attrs={
                                     "class": "form-control"
                                 })
                                 )
    password1 = forms.CharField(label="Mot de passe",
                                widget=forms.PasswordInput(
                                    attrs={
                                        "class": "form-control"
                                    })
                                    )
    password2 = forms.CharField(label="Confirme mot de passe",
                                widget=forms.PasswordInput(
                                    attrs={
                                        "class": "form-control"
                                    })
                                    )
    
class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2')   