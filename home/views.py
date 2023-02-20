from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .form import userform
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def hello(request):
    return render(request, 'navbar.html')


def login(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Registerd Successfuly !!")
            auth_login(request, user)
            subject = "welcome to Auth"
            massage = " thank you for login"
            send_mail(
                subject,
                massage,
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,                
            )

            return redirect('home')
        else:
            messages.error(request, "useename or password is not valid")
    return render(request, "login.html")


def signup(request):
    page = 'register'
    form = userform()
    if request.method == 'POST':
        form = userform(request.POST)
        if form.is_valid:
            user = form.save(commit='false')
            user.username = user.username.lower()
            user.save()
            # messages.success(request, "Registerd Successfuly !!")
            # auth_login(request, user)
            # subject = "welcome to Auth"
            # massage = " thank you for login"
            # send_mail(
            #     subject,
            #     massage,
            #     settings.EMAIL_HOST_USER,
            #     user.email,
            #     fail_silently=False,                
            # )

            return redirect('home')

        else:
            messages.error(request, "somthing wrong !!")
    context = {'page': page, 'form': form}
    return render(request, 'login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('login')


def profile(request):
    profile=User.objects.all()
    context={
        'profile':profile
    }
    return render(request,'profile.html')