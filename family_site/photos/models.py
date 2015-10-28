from django.db import models

loginChoices=[('gmail','Gmail'),
         ('facebook','Facebook'),
         ('twitter', 'Twitter')]

# TBD: Should not be hardcoded.
DEFAULT_OCASSION=1

class User(models.Model):
    """Used to track users allowed to access the site"""
    username = models.CharField(max_length=50)
    loginchoice = models.CharField(max_length=20)    # TBD: Consider changing to an Integer (Enum)

    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)

    createDate = models.DateTimeField()
    updateDate = models.DateTimeField()

class Ocassion(models.Model):
    """Used to store the occations to choose from"""
    linkText = models.CharField('Link Text', max_length=50)
    name = models.CharField('Name', max_length=100)
    description = models.CharField('Description', max_length=200)

    fileLocation = models.CharField('File Location', max_length=30, blank = True) # TBD: Couldn't reference, try adding later.

    # Used to show text in 'admin' screens
    # TBD: Need to find a better way
    def __unicode__(self):
        return self.name


# Temp location
import os
def get_upload_path(instance, filename):
    return os.path.join(instance.ocassion.fileLocation, filename)

class Picture(models.Model):
    """Used to store the pictures"""
    title = models.CharField('Title', max_length=100)
    description = models.CharField('Description', max_length=200)

    ocassion = models.ForeignKey(Ocassion, default=DEFAULT_OCASSION)

    photo = models.ImageField(upload_to=get_upload_path, blank = True)

    def image_tag(self):
        return u'<img src="%s" height="200px" width="200px"/>' % self.photo.url

    image_tag.short_description = 'Photo'
    image_tag.allow_tags = True

    def __unicode__(self):
        displayStr = "Title: %s\n" % self.title
        displayStr += "Description: %s\n" % self.description

        return displayStr


