from vmapp.models import User
from django import forms
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'phone_number','email','password','city','state','zipcode']
