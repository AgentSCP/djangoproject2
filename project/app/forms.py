from django import forms

class UserForm(forms.Form):
    name = forms.CharField(max_length=20, min_length=2)
    age = forms.IntegerField()
