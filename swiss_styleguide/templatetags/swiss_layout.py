from django import template

register = template.Library()


@register.inclusion_tag('swiss_field.html')
def swiss_field(field, required=False, **kwargs):
    return {
        'field': field,
        'required': required
    }
