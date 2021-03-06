from django import template

register = template.Library()


@register.filter
def currency(price):
    bar = '{:,.0f} руб.'.format(price).replace(',', ' ')
    return bar


@register.filter
def stars_count(count):
    return '★' * count
