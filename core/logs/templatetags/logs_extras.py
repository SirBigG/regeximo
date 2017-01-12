from django import template

register = template.Library()


@register.filter
def times(number):
    """
    For using range function in templatetags.
    :param number: int
    :return range obj:
    """
    return range(1, number+1)
