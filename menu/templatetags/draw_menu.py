from django import template
from django.urls import resolve
from menu.models import Menu, MenuItem

register = template.Library()

@register.inclusion_tag('menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    try:
        menu = Menu.objects.get(name=menu_name)
    except Menu.DoesNotExist:
        return {'menu': None, 'menu_items': [], 'active_item_ids': []}

    path = context['request'].path
    current_url = resolve(path).url_name

    def get_active_items(items, active_url):
        for item in items:
            if item.get_absolute_url() == active_url:
                return [item]
            if item.children.all():
                result = get_active_items(item.children.all(), active_url)
                if result:
                    return [item] + result
        return []

    menu_items = menu.items.filter(parent__isnull=True).prefetch_related('children')
    active_items = get_active_items(menu.items.all(), current_url)
    active_item_ids = [item.id for item in active_items]

    return {
        'menu': menu,
        'menu_items': menu_items,
        'active_item_ids': active_item_ids,
    }
