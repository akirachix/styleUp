from django.contrib import admin

import product
from . import views
from django.urls import path,include

urlpatterns = [
   path('',views.home, name='home'),
   path('signup', views.signup, name='signup'),
   path('signin', views.signin, name='signin'),
   path('signout', views.signout, name='signout'),
   path('activate/<uidb64>/<token>', views.activate, name='activate'),
   # path('product', views.product, name=product),
]