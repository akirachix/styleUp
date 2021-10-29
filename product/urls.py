# from . import views
from django.urls import path
from .views import getCategories
import product

app_name = "product" 
urlpatterns = [
    path('', getCategories, name='product'),
]