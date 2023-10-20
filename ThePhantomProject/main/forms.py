from dataclasses import field, fields
from django import forms
from .models import Product, Category, Review

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class ProductPostForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'description', 'details', 'image', 'price', 'category')
        

class CategoryPostForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name', 'description', 'image')
        
class ReviewPostForm(forms.ModelForm):
    score = forms.DecimalField(widget=forms.NumberInput(attrs={
    'min': 0.0, 
    'max': 5.0,
    'step': 0.1
    }))
    
    class Meta:
        model = Review
        fields = ('title','score', 'content')
        
