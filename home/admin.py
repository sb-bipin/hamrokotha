from django.contrib import admin
from home.models import Contact, Login, Property, Rooms, Houses

# Register your models here.
admin.site.register(Contact),
admin.site.register(Login)
admin.site.register(Property)
admin.site.register(Rooms)
admin.site.register(Houses)
