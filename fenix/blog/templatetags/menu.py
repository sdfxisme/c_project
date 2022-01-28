from django import template
from blog.models import Emitent

register = template.Library()

@register.inclusion_tag('blog/menu_tpl.html')
def show_menu(menu_class= 'menu'):
    emitents = Emitent.objects.all()
    return {'emitents': emitents, "menu_class": menu_class }