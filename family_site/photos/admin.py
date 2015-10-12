from django.contrib import admin

from .models import Pictures

class PicturesAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['title', 'description']}),
        ('Picture Location', {'fields': ['pictureName', 'pictureLocation']})

    ]

    list_display = ('title', 'description')

    search_fields = ['title', 'description']

admin.site.register(Pictures, PicturesAdmin)

