from django import forms
from django.core.validators import EmailValidator

class MyForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=10)
    email = forms.EmailField(
        validators=[EmailValidator(message="Please enter a valid email address.")]
    )
