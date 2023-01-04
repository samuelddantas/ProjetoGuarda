from django.forms               import ModelForm
from django                     import forms
from User                       import models
from django.contrib.auth.models import User

class ReviewForm(ModelForm):
    class Meta:
        model = models.Review
        fields = '__all__'

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'id',
            'username',    
            'first_name',
            'last_name',
            'email',  
        ]

