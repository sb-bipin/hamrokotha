from django.db import models

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
    phone = models.IntegerField(default=None)
    img = models.ImageField(upload_to='images/', default=None)
    Rooms = "Rooms"
    Flat = "Flat"
    House = "House"
    Others = "Others"
    propertychoice = [('Rooms', "Rooms"), ('Flat', "Flat"),
                      ('House', "House"), ('Others', "Others")]
    propertytype = models.CharField(
        choices=propertychoice, max_length=10, default='Others')
    descp = models.CharField(max_length=50, default=None)

    def _str_(self):
        return self.name
