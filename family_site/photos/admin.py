from django.contrib import admin

from .models import Picture, Ocassion, Person

class PictureAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['title', 'description']}),
        (None,  {'fields': ['ocassion',]}),
        (None,  {'fields': ['people',]}),
        ('Photo', {'fields': ['photo', 'portrait', 'image_tag']}),
        ('Audit Info', {'fields': ['createDateTime', 'updatedDateTime'],
                        'classes': ('collapse',)}),

    ]

    readonly_fields = ('image_tag', 'createDateTime', 'updatedDateTime')

    list_display = ('title', 'description', 'createDateTime', 'updatedDateTime')

    search_fields = ['title', 'description']

admin.site.register(Picture, PictureAdmin)

class OcassionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'description']}),
        (None, {'fields': ['linkText', 'occuredDate']}),
        (None, {'fields': ['fileLocation',]}),
        ('Audit Info', {'fields': ['createDateTime', 'updatedDateTime'],
                        'classes': ('collapse',)}),
    ]

    list_display = ('name', 'description', 'createDateTime', 'updatedDateTime')
    readonly_fields = ('createDateTime', 'updatedDateTime')

admin.site.register(Ocassion, OcassionAdmin)

class PersonAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', {'fields': [('firstName', 'lastName')]}),
        ('Parents', {'fields': [('mother', 'father')]}),
        ('Picture', {'fields': ['profilePicture',]}),
        ('Audit Info', {'fields': ['createDateTime', 'updatedDateTime'],
                        'classes': ('collapse',)}),
    ]

    list_display = ('lastName', 'firstName', 'createDateTime', 'updatedDateTime')
    readonly_fields = ('createDateTime', 'updatedDateTime')

admin.site.register(Person, PersonAdmin)

