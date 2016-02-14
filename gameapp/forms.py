from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='User name', max_length=100)
    password = forms.CharField(label='Password', max_length=100)

class SolutionForm(forms.Form):
    solution = forms.CharField(label='Solution', max_length=100)
