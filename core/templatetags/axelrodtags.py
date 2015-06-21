from django import template

register = template.Library()


@register.filter
def startswith(value, s):
    return value.startswith(s)
