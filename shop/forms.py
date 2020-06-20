from django import forms

class ProductForm(forms.Form):
    name = forms.CharField()
    image = forms.ImageField()
    description = forms.CharField()
    price = forms.FloatField()
    article = forms.CharField(label='Артикул')

    def cart_add(self):
        # Добавить телефон в корзину
        pass