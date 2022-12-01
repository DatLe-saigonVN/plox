from django.urls import path
from PloxWeb import views

urlpatterns = [path('', views.user_login),
               ]

