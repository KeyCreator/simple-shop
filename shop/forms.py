from django import forms

class PhoneForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()
    price = forms.FloatField()

    def cart_add(self):
        # Добавить телефон в корзину
        pass