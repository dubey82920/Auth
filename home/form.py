from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class userform(UserCreationForm):
    class meta:
        model=User
        fields=['first_name','email','username','password1','password2']