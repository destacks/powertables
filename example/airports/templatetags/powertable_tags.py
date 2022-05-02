from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def with_sorting_prefix(value):
    return f"sorting_{value}"
