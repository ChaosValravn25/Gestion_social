from django import template

register = template.Library()

@register.filter(name='endswith')
def endswith(value, arg):
    """Verifica si el valor termina con el argumento especificado."""
    if isinstance(value, str):
        return value.endswith(arg)
    return False
