from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='User name', max_length=100)
    password = forms.CharField(label='Password', max_length=100)

class ResponseForm(forms.Form):
    response = forms.CharField(label='Solution', max_length=100)
