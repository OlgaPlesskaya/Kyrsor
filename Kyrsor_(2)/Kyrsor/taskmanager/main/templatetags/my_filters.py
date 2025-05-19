from django import template

register = template.Library()

@register.filter(name='height')
def height(value):
    return value.count('\n') * 20 # предполагаем, что каждая строка имеет высоту 20 пикселей