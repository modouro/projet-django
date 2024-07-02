from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AjouterBlog(UserCreationForm):
    titre       = forms.CharField(label='titre',
                                  widget=forms.TextInput(
                                      attrs={
                                          "class": "form-control"
                                      }
                                  ))
    description = forms.CharField(label='description',
                                  widget=forms.TextInput(
                                      attrs={
                                          "class": "form-control"
                                      }
                                  ))
    contenu     = forms.TextInput(label='contenu',
                                  widget=forms.TextInput(
                                      attrs={
                                          "class": "form-control"
                                      }
                                  ))
    date_create   = forms.DateTimeField(label='Date de création',
                                      widget=forms.DateTimeInput(
                                          attrs={
                                              "class": "form-control"
                                          }
                                      ))
    dateupdate  = forms.DateTimeField(label='Mise à jours',
                                      widget=forms.DateTimeInput(
                                          attrs={
                                              "class": "form-control"
                                          }
                                      ))
    class Meta:
        model = User
        fields = ('titre', 'description', 'contenu', 'date_create', 'dateupdate')