from django.forms               import ModelForm
from django                     import forms
from User                       import models
from django.contrib.auth.models import User

class ReviewForm(ModelForm):
    class Meta:
        model = models.Review
        fields = [
            'rev_id',
            'rev_obr_id',
            'rev_review',
            'rev_nota',
        ]

        widgets = {
           'rev_obr_id':           forms.Select                 (attrs={
                'class':'sign__input',
                'placeholder': 'Obra Escolhida'
            }),
            'rev_review':          forms.Textarea                  (attrs={
                'class':'sign__input',
                'placeholder': 'Review da Obra'
            }),
            'rev_nota':             forms.NumberInput                 (attrs={
                'class':'sign__input',
                'placeholder': 'Nota da Obra',
            }),
        }

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

