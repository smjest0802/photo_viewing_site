from django.db import models
import os, datetime

loginChoices=[('gmail','Gmail'),
         ('facebook','Facebook'),
         ('twitter', 'Twitter')]

# TBD: Should not be hardcoded. Or a better generic ocassion created.
DEFAULT_OCASSION=1

# TBD: May not use this. Need to understand Django's User configuration first.
class User(models.Model):
    """Used to track users allowed to access the site"""
    username = models.CharField(max_length=50)
    loginchoice = models.CharField(max_length=20)    # TBD: Consider changing to an Integer (Enum)

    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)

    createDate = models.DateTimeField()
    updateDate = models.DateTimeField()

class Person(models.Model):
    """Used to associate a person to other things"""

    firstName = models.CharField('First Name', max_length=50)
    lastName = models.CharField('Last Name', max_length=50)

    mother = models.ForeignKey('self', blank = True, null = True, related_name="photos_persons_mother")
    father = models.ForeignKey('self', blank = True, null = True, related_name="photos_persons_father")

    profilePicture = models.ForeignKey('Picture', blank = True, null = True)

    def __unicode__(self):
        return "%s, %s" % (self.lastName, self.firstName)

class Ocassion(models.Model):
    """Used to store the occations to choose from"""
    linkText = models.CharField('Link Text', max_length=50)
    name = models.CharField('Name', max_length=100)
    description = models.CharField('Description', max_length=200)

    occuredDate = models.DateTimeField('Date', default=datetime.datetime.utcnow)

    fileLocation = models.CharField('File Location', max_length=30, blank = True)

    # Used to show text in 'admin' screens
    # TBD: Need to find a better way
    def __unicode__(self):
        return self.name

def get_upload_path(instance, filename):
    return os.path.join(instance.ocassion.fileLocation, filename)

class Picture(models.Model):
    """Used to store the pictures"""
    title = models.CharField('Title', max_length=100)
    description = models.CharField('Description', max_length=200, blank = True)

    people = models.ManyToManyField(Person, blank = True)

    uploadDate = models.DateTimeField('Upload Date', default=datetime.datetime.utcnow)

    ocassion = models.ForeignKey(Ocassion, default=DEFAULT_OCASSION)

    photo = models.ImageField(upload_to=get_upload_path)
    portrait = models.BooleanField('Is portrait?', default=0) # Default the fields to false

    def image_tag(self):
        # TBD: Adjust so the Admin page correctly displays photo too (So there is a preview of how it will display on the site).
        return u'<img src="%s" height="200px" width="200px"/>' % self.photo.url

    image_tag.short_description = 'Photo'
    image_tag.allow_tags = True

    def __unicode__(self):
        displayStr = "Title: %s\n" % self.title
        displayStr += "Description: %s\n" % self.description

        return displayStr


