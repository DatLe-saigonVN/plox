from django.shortcuts import render
from .models import *
# Create your views here.
def user_login(request):
    if request.session.get('username',None) and request.session.get('type',None)=='customer':
        return redirect('user_dashboard')
    if request.session.get('username',None) and request.session.get('type',None)=='manager':
        return redirect('manager_dashboard')
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        if not len(username):
            messages.warning(request,"Username field is empty")
            redirect('user_login')
        elif not len(password):
            messages.warning(request,"Password field is empty")
            redirect('user_login')
        else:
            pass
        if Customer.objects.filter(username=username):
            user=Customer.objects.filter(username=username)[0]
            password_hash=user.password
            res=check_password(password,password_hash)
            if res==1:
                request.session['username'] = username
                request.session['type'] = 'customer'
                return render(request,'booking/index.html',{})
            else:
                messages.warning(request,"Username or password is incorrect")
                redirect('user_login')
        else:
            messages.warning(request,"No, Account exist for the given Username")
            redirect('user_login')
    else:
        redirect('user_login')
    return render(request,'base.html',{})