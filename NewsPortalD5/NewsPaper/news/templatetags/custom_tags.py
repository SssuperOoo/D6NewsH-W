from datetime import datetime
from django import template


register = template.Library()


@register.simple_tag()
def format_date(post,format_string='%b %M %Y'):
   return post.created_at.strftime(format_string)