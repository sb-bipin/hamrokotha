from django.db import models
from phone_field import PhoneField
# Create your models here.


class Contact(models.Model):
    email = models.CharField(max_length=122)
    fullname = models.CharField(max_length=122)
    desc = models.CharField(max_length=1000, default="None")
    date = models.DateField()

    def __str__(self):
        return self.fullname


# class Signup(models.Model):
#     username = models.CharField(max_length=122)
#     password = models.CharField(max_length=121)
#     if password is None:
#         password = "hamrokotha"

#     def _str_(self):
#         return self.username


class Login(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=False),
    username = models.CharField(max_length=122)
    password = models.CharField(max_length=121)

    def _str_(self):
        return self.username


class Image(models.Model):
    name = models.CharField(max_length=50, default=None)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    # phone = models.CharField(max_length=20, default=None)
    img = models.ImageField(upload_to='images/', default=None)
    # Rooms = "Rooms"
    # Flat = "Flat"
    # House = "House"
    # Others = "Others"
    propertychoice = [('Room', "Rooms"), ('Flat', "Flats"),
                      ('House', "Houses"), ('Other', "Others")]
    propertytype = models.CharField(
        max_length=20, choices=propertychoice, default='Other')
    descp = models.CharField(max_length=50, default=None)

    def _str_(self):
        return self.name
