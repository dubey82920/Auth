from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.hello,name="home"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('signup/',views.signup,name="signup"),
    path('profile/',views.profile,name="profile")
]