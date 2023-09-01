from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Signup.as_view(), name='home'),
    path('cars/', CarsView.as_view(), name='cars')
]