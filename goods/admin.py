from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


@admin.register(Car)
class AllCars(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'get_image')
    # list_display = ('id', 'title', 'price')
    list_display_links = ('title',)
    list_filter = ('title', 'price')
    search_fields = ('title__name',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="60", height="50" ')

    get_image.short_description = "Images"
    # readonly_fields = ('poster',)


admin.site.register(CarName)
admin.site.register(Category)
admin.site.register(RatingStar)
admin.site.register(Specifications)

admin.site.register(CarShorts)
admin.site.register(Genre)


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'parent', 'car')

# Register your models here.
