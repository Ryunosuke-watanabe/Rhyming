from django.contrib.auth import forms as auth_forms
from django.contrib.auth import get_user_model
from django import forms
from django.db.models import fields
from .models import *
from django.contrib.auth.forms import UserCreationForm

class CreateUser(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username',)
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label

class LoginForm(auth_forms.AuthenticationForm):
    class Meta:
        model = get_user_model()
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label

class RhymeText(forms.ModelForm):
    class Meta:
        model = InputRhyme
        fields = ('text',)
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label