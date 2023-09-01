from django.views.generic import CreateView
from .forms import *

class Signup(CreateView):
    form_class = UserForm
    template_name = 'home.html'
    success_url = '/'

class CarsView(CreateView):
    form_class = carsForm
    template_name = 'cars.html'
    success_url = '/'