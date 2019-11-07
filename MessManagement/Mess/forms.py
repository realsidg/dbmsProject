from django import forms

class SignInForm(forms.Form):
    user_regno = forms.CharField(label='RegNo',widget=forms.TextInput(attrs={
    "class":"form-control","required":True}))

    user_pass = forms.CharField(label='Password',widget=forms.TextInput(attrs={'type':'password',
    "id":"inputPassword","class":"form-control","required":True}))
