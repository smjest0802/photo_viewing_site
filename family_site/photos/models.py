from django.db import models
import os, datetime

# TBD: Should not be hardcoded. Or a better generic ocassion created.
DEFAULT_OCASSION = 1

class CommonInfo(models.Model):
    """Contains the fields common to all models"""
    createDateTime = models.DateTimeField('Create Date Time', default=datetime.datetime.now)
    updatedDateTime = models.DateTimeField('Updated Date Time', default=datetime.datetime.now)

    class Meta:
        abstract = True

class Person(CommonInfo):
    """Used to associate a person to other things"""

    firstName = models.CharField('First Name', max_length=50)
    lastName = models.CharField('Last Name', max_length=50)

    mother = models.ForeignKey('self', blank = True, null = True, related_name="photos_persons_mother")
    father = models.ForeignKey('self', blank = True, null = True, related_name="photos_persons_father")

    profilePicture = models.ForeignKey('Picture', blank = True, null = True)

    def __unicode__(self):
        return "%s, %s" % (self.lastName, self.firstName)

class Ocassion(CommonInfo):
    """Used to store the occations to choose from"""
    linkText = models.CharField('Link Text', max_length=50)
    name = models.CharField('Name', max_length=100)
    description = models.CharField('Description', max_length=200)

    occuredDate = models.DateTimeField('Date Occured?', default=datetime.datetime.now)

    fileLocation = models.CharField('File Location', max_length=30, blank = True)

    def __unicode__(self):
        return self.name

def get_upload_path(instance, filename):
    """Gets the Media path to save and retrieve the files from"""
    return os.path.join(instance.ocassion.fileLocation, filename)

class Picture(CommonInfo):
    """Used to store the pictures"""
    title = models.CharField('Title', max_length=100)
    description = models.CharField('Description', max_length=200, blank = True)

    people = models.ManyToManyField(Person, blank = True)

    ocassion = models.ForeignKey(Ocassion, default=DEFAULT_OCASSION)

    photo = models.ImageField(upload_to=get_upload_path)
    portrait = models.BooleanField('Is portrait?', default=0) # Default the fields to false

    def image_tag(self):
        """Used to display the picture on the Admin screen"""
        # TBD: Adjust so the Admin page correctly displays photo too (So there is a preview of how it will display on the site).
        return u'<img src="%s" height="200px" width="200px"/>' % self.photo.url

    image_tag.short_description = 'Photo'
    image_tag.allow_tags = True

    def __unicode__(self):
        return "%s <%s>" % (self.title, self.description)


