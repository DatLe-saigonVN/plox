from .models import *
from django.shortcuts import  render, redirect
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def homepage(request):
    return render(request, 'home.html')
def update_user_data(user):
    Location.objects.update_or_create(user=user, defaults={'address': user.location.address, 'city':user.location.city})
def signup(request):
    if request.method == 'POST':
        register_form = SignUpForm(request.POST)
        if register_form.is_valid():
            new_article = Article.objects.create(
                author=User.objects.get(pk=request.user.id),
                title=form.cleaned_data["title"],
                message=form.cleaned_data["message"],
            )
            new_article.save()
            user.location.address = form.cleaned_data.get('address')
            user.location.city = form.cleaned_data.get('city')
            update_user_data(user)
            # load the profile instance created by the signal
            user.save()
            raw_password = register_form.cleaned_data.get('password')

            # login user after signing up
            user = authenticate(email=user.email, password=raw_password)
            login(request, user)

            # redirect user to home page
            return redirect('home')
    else:
        register_form = SignUpForm()
    return render(request, 'register.html', {'register_form': register_form})
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})