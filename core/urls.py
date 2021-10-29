from django.urls import path
from .views import index
import core

app_name = "core" 
urlpatterns = [
    path('', index, name='core'),
]