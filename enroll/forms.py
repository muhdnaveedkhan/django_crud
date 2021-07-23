from django.core import validators
from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Student

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'email', 'password') #We can use list as well
        widgets = {
            'name':forms.TextInput(attrs={'class': 'form-control'}), 
            'email':forms.EmailInput(attrs={'class': 'form-control'}), 
            'password':forms.PasswordInput(render_value = True, attrs={'class': 'form-control'}),
            
            }