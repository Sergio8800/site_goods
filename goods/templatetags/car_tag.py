from django import template
# from Django_Site.mysite.goods.models import Category, Car
# from mysite.goods.models import *
from goods.models import *

# from mysite.goods.models import Category, Car

register = template.Library()


# для базового шаблона
@register.simple_tag()
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('goods/tag/last_car.html')
def get_last_car(count=3):
    cars = Car.objects.order_by("id")[:count]
    return {"last_cars": cars}
