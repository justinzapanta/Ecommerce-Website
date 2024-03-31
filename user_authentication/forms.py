from django import forms
from django.contrib.auth.models import User

input_style = 'height: 2.5rem; width: 15rem; border: 1px; border-style: solid; padding-left: 0.5rem;'

class SignIn_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']

        widgets = {
            'email' : forms.TextInput(attrs={
                'style' : f'{input_style} margin-left: 0.2rem;',
                'required' : 'required',
            }),
            
            'password' : forms.PasswordInput(attrs={
                'style' : f'{input_style} margin-left: 2rem;',
                'class' : 'ml-14 mt-5'
            })
        }



class SignUp_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password']

        widgets = {
            'email' : forms.TextInput(attrs={
                'style' : f'{input_style} margin-left: 1.1rem;',
                'required' : 'required',
            }),

            'first_name' : forms.TextInput(attrs={
                'style' : f'{input_style} margin-left: 2.6rem; margin-top: 0.7rem;',
                'required' : 'required',
            }),

            'last_name' : forms.TextInput(attrs={
                'style' : f'{input_style} margin-left: 2.7rem; margin-top: 0.7rem;',
                'required' : 'required',
            }),

            'password' : forms.PasswordInput(attrs={
                'style' : f'{input_style} margin-left: 3rem; margin-top: 0.7rem;',
                'required' : 'required',
            })
        }