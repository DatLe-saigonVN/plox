from django.urls import path
from PloxWeb import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("login", views.login_request, name="login"),
    path("register", views.signup, name="register")
               ]

