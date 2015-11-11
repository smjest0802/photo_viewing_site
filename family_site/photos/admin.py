from django.contrib import admin

from .models import Picture, Ocassion, Person


class PictureAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['title', 'description', 'uploadDate']}),
        (None,  {'fields': ['ocassion',]}),
        (None,  {'fields': ['people',]}),
        ('Photo', {'fields': ['photo', 'portrait', 'image_tag']})

    ]

    readonly_fields = ('image_tag',)

    list_display = ('title', 'description')

    search_fields = ['title', 'description']

admin.site.register(Picture, PictureAdmin)
#admin.site.register(Picture)
admin.site.register(Ocassion)
admin.site.register(Person)

