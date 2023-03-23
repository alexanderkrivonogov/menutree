from django import template

from menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context):
    query_set = MenuItem.objects.order_by('parent')
    menu_items = {}
    for item in query_set:
        if item.parent_id not in menu_items:
            menu_items[item.parent_id] = []
        menu_items[item.parent_id].append(
            {'id': item.id, 'name': item.name, 'children': menu_items.get(item.id, []), 'parent_id': item.parent_id})
    context['menu_items'] = menu_items
    return context


@register.inclusion_tag('menu/menu_children.html', takes_context=True)
def draw_menu_children(context, menu_items, parent_id=None):
    if parent_id in menu_items:
        menu_children = menu_items[parent_id]
        for item in menu_children:
            if item['id'] in menu_items:
                item['children'] = menu_items[item['id']]
        context['menu_children'] = menu_children
        print(menu_children)
        return context
    context['menu_children'] = []
    return context
