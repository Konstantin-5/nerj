#coding: utf-8

from django import template
from apps.portfolio import static

register = template.Library()


@register.inclusion_tag('portfolio/main_list.html', takes_context=True)
def main_list_portfolio_fn(context, count_item):

    data = static.item_object.get_item_list(count=count_item)

    if not data:
        return {
            'main_list_portfolio': []
        }

    return_data = []

    for item in data:
        if item.gallery and item.gallery_is_item:
            for gallery in item.gallery.all():
                if gallery.main_image and gallery.active:
                    return_data.append({
                        "name": item.name,
                        "url": item.url,
                        "src_small": gallery.main_image.src_small
                    })

    return {
        'main_list_portfolio': return_data
    }


@register.inclusion_tag('article/slide.html', takes_context=True)
def slide_portfolio_fn(context, count):

    data = static.item_object.get_list_item_slide(count)
    if not data:
        return {
            'slide_article': []
        }

    newData = []

    for item in data:
        for gallery in item.gallery.all():
            if gallery.active or gallery.images.count() == 0:
                continue
            img = gallery.images.all()[0]
            newData.append({'data': item, 'img': img})

    return {
        'slide_article': newData
    }