from django import template

register = template.Library()


@register.filter(name="dict_key")
def dict_key(dict, key):
    """Returns a dictionary key as a string if it exists, else 'none'"""
    return dict[f'{key}'] if key in dict else 'none'
