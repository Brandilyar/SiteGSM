from django import forms
from .models import Card

class PostForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['number_card']
        widgets ={'number_card':forms.Select(attrs={'class':'form-control'})
        
        }