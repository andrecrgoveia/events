from django import template

register = template.Library()

# Decorator for split username of email.
@register.filter(name='get_username_before_at')
def get_username_before_at(email):
    return email.split('@')[0] if email else ""
