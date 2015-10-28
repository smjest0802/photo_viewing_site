from django.contrib import admin

from .models import Picture, Ocassion


class PictureAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['title', 'description']}),
        (None,  {'fields': ['ocassion',]}),
        ('Photo', {'fields': ['photo', 'image_tag']})

    ]

    readonly_fields = ('image_tag',)

    list_display = ('title', 'description')

    search_fields = ['title', 'description']

admin.site.register(Picture, PictureAdmin)
#admin.site.register(Picture)
admin.site.register(Ocassion)

