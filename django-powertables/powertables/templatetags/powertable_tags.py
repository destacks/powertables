from typing import List

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def with_sorting_prefix(value):
    return f"sorting_{value}"


@register.filter
def get_attribute(obj) -> List[any]:
    return [getattr(obj, f.name) for f in obj._meta.get_fields() if f.name != "id"]
