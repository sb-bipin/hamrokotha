"""Hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from home import views


admin.site.site_header = "Hamro Kotha Admin Panel"
admin.site.site_title = "HamroKotha Admin Portal"
admin.site.index_title = "Welcome to Hamro_Kotha"


urlpatterns = [
    path("deleteservice", views.deleteservice, name='deleteservice'),
    path("", views.logout, name='logouthome'),
    path("home", views.home, name='home'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("login", views.Login, name='Login'),
    path("signup", views.signup, name='signup'),
    path('gallery', views.gallery, name="gallery"),
    path('logout', views.logout, name="Logout"),
    path('service_details/<int:service_id>/',
         views.service_details, name='service_details'),
    path('about', views.about, name="about"),
    path('loginabout', views.loginabout, name="loginabout"),
    path('logoutService', views.logoutService, name="logoutService"),



]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
