from django.forms import ModelForm, PasswordInput, modelform_factory
from .models import *

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'middle_name', 'password')
        widgets = {'password':PasswordInput()}

carsForm = modelform_factory(Cars, fields='__all__')