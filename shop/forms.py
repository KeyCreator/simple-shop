from django import forms

class CartForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()
    price = forms.FloatFiled()