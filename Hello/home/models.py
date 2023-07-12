from email.headerregistry import Group
from django.contrib.auth.models import User
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


class Login(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=False),
    username = models.CharField(max_length=122)
    password = models.CharField(max_length=121)

    def __str__(self):
        return self.username


# class RoomsDetails(models.Model):
#     name = models.CharField(max_length=50, default=None)
#     address = models.CharField(max_length=50, default=None)
#     phone = models.CharField(max_length=10, default=None)
#     imgfield = models.ImageField(upload_to='images/', default=None)
#     price = models.CharField(max_length=5, default=None)
#     payingchoice = [('Monthly', 'Monthly'), ('Quarterly', 'Quarterly'),
#                     ('Semi-Annually', 'Semi-Annually'), ('Annually', 'Annually')]
#     payingmodel = models.CharField(
#         max_length=20, choices=payingchoice, default='Monthly')
#     attachedbathroomchoice = [('Yes', 'Yes'), ('No', 'No')]
#     attachedbathroom = models.CharField(
#         max_length=5, choices=attachedbathroomchoice, default='No')
#     wifiavailablechoice = [('Yes', 'Yes'), ('No', 'No')]
#     wifiavailable = models.CharField(
#         max_length=5, choices=wifiavailablechoice, default='No')
#     acfanchoice = [('AC', 'AC'), ('Fan', 'Fan')]
#     acfan = models.CharField(
#         max_length=5, choices=acfanchoice, default='Fan')
#     descp = models.CharField(max_length=50, default=None)

#     def __str__(self):
#         return self.name


class Property(models.Model):
    name = models.CharField(max_length=50, default=None)
    address = models.CharField(max_length=50, default=None)
    phone = models.CharField(max_length=10, default=None)
    imgfield = models.ImageField(upload_to='images/', default=None)
    price = models.CharField(max_length=5, default=None)
    payingchoice = [('Monthly', 'Monthly'), ('Quarterly', 'Quarterly'),
                    ('Semi-Annually', 'Semi-Annually'), ('Annually', 'Annually')]
    payingmodel = models.CharField(
        max_length=20, choices=payingchoice, default='Monthly')
    descp = models.CharField(max_length=50, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='property', null=True, blank=True, default=None)

    # class Meta:
    #     abstract = True

    def __str__(self):
        return self.name


class Rooms(models.Model):
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name='rooms', null=True, blank=True, default=None)
    attachedbathroomchoice = [('Yes', 'Yes'), ('No', 'No')]
    attachedbathroom = models.CharField(
        max_length=5, choices=attachedbathroomchoice, default='No')
    wifiavailablechoice = [('Yes', 'Yes'), ('No', 'No')]
    wifiavailable = models.CharField(
        max_length=5, choices=wifiavailablechoice, default='No')
    acfanchoice = [('AC', 'AC'), ('Fan', 'Fan')]
    acfan = models.CharField(
        max_length=5, choices=acfanchoice, default='Fan')
    # propertyrooms = models.OneToOneField(
    #     Property, on_delete=models.CASCADE, default=id, related_name='acfan')

    # def __str__(self):
    #     return f"Room {self.acfan} - Property: {self.property.name}"


class Houses(models.Model):
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name='houses', null=True, blank=True, default=None)
    size = models.CharField(max_length=10, default=None)
    totalrooms = models.CharField(max_length=3, default=None)


class Flats(models.Model):
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name='flats', null=True, blank=True, default=None)
    wifiavailablechoice = [('Yes', 'Yes'), ('No', 'No')]
    wifiavailable = models.CharField(
        max_length=5, choices=wifiavailablechoice, default='No')
    totalrooms = models.CharField(max_length=3, default=None)
