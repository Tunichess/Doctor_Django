from django import forms
from django.contrib.auth.models import User
from first_app.models import STATE,Personne,TYPE
    
class UserForm(forms.ModelForm):
    password =forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=('username','email','password')

class RegistrationForm(forms.ModelForm):
    class Meta:
        model=Personne
        fields=('first_name','last_name','birthday','state')

class StateForm(forms.Form):
    state = forms.ChoiceField(choices=STATE)

class QuestionForm(forms.Form):
    questtype = forms.ChoiceField(choices=TYPE)
