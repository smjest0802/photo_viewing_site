from django.db import models

loginChoices=[('gmail','Gmail'),
         ('facebook','Facebook'),
         ('twitter', 'Twitter')]

class User(models.Model):
    """Used to track users allowed to access the site"""
    username = models.CharField(max_length=50)
    loginchoice = models.CharField(max_length=20)    # TBD: Consider changing to an Integer (Enum)

    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)

    createDate = models.DateTimeField()
    updateDate = models.DateTimeField()

class Pictures(models.Model):
    """Used to store the pictures"""
    title = models.CharField('Title', max_length=100)
    description = models.CharField('Description', max_length=200)

    # TBD: Consider storing the picture in the database
    pictureLocation = models.CharField('Picture Location', max_length=200)
    pictureName = models.CharField('Picture Name', max_length=200)

    def __unicode__(self):
        displayStr = "Title: %s\n" % self.title
        displayStr += "Description: %s\n" % self.description
        displayStr += "Picture Location: %s\n" % self.pictureLocation
        displayStr += "Picture Name: %s" % self.pictureName

        return displayStr


