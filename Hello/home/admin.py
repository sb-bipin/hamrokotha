from django.contrib import admin
from .models import RoomsDetails
from home.models import Contact, Login

# Register your models here.
admin.site.register(Contact),
admin.site.register(Login)
admin.site.register(RoomsDetails)
