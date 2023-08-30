<<<<<<< HEAD
=======
from django.db import models
>>>>>>> master
from django.http import JsonResponse
import logging
from .forms import PropertyDetailsForm, RoomsDetailsForm, HousesDetailsForm
from tkinter import Image
from django.shortcuts import get_object_or_404, render, redirect
import pytest

# from .models import RoomsDetails
from .forms import signupform
from django.contrib.auth import login, authenticate
from django.contrib.auth import authenticate, login
from datetime import datetime
from django.shortcuts import redirect, render, HttpResponse
from home.models import Contact, Property, Rooms
from django.contrib import messages
from .forms import signupform
from django.views.decorators.csrf import csrf_protect


def logout(request):
    return render(request, "logouthome.html")

# Create your views here.


def about(request):
    return render(request, "about.html")


def loginabout(request):
    return render(request, "loginabout.html")


# def index(request):
#     return render(request, "index.html")


def home(request):
    userproperties = Property.objects.filter(owner_id=request.user.id)
    return render(request, "index.html", {'userproperties': userproperties})


def services(request):
    filter_type = request.GET.get("filter")
    logging.info(filter_type)

<<<<<<< HEAD
    filter_mapping = {
        "ac": Property.objects.filter(rooms__acfan="AC").prefetch_related('rooms').order_by("price"),
        "lowhighprice": Property.objects.order_by('price'),
        "attachbathroom": Property.objects.filter(rooms__attachedbathroom="Yes").prefetch_related('rooms').order_by('price')
=======
    def get_all_properties():
        return Property.objects.all().order_by('-id')

    def get_ac_properties():
        return Property.objects.filter(rooms__acfan=True).select_related('rooms').order_by("price")

    def get_low_high_price_properties():
        return Property.objects.order_by('price_numeric')

    def get_attached_bathroom_properties():
        return Property.objects.filter(rooms__attachedbathroom=True).select_related('rooms').order_by('price_numeric')

    filter_mapping = {
        "": get_all_properties,
        "ac": get_ac_properties,
        "lowhighprice": get_low_high_price_properties,
        "attachbathroom": get_attached_bathroom_properties
>>>>>>> master
    }

    allimages = filter_mapping.get(
        filter_type, Property.objects.all().order_by('-id'))

    response = render(request, 'services.html', {'propertydetails': allimages})
    return response

    # return render(request, "services.html")
    # return HttpResponse("This is the servicespage created from Django..! ")


<<<<<<< HEAD
def deleteservice(request, service_id):
    services = Property.objects.filter(id=service_id)
    service = get_object_or_404(services, pk=service_id)
    service.delete()
    return JsonResponse({'success': True})


def service_details(request, service_id):
    # services = get_object_or_404(Property, id=service_id)
    services = Property.objects.filter(id=service_id)

=======
def service_details(request, service_id):
    # services = get_object_or_404(Property, id=service_id)
    services = Property.objects.filter(id=service_id)
>>>>>>> master
    return render(request, 'service_details.html', {'services': services})


def logoutService(request):
    logoutServices = Property.objects.all()[:12]
<<<<<<< HEAD
=======
    # messages.error(request, "Please log in to see more.")
>>>>>>> master
    return render(request, 'logoutService.html', {'logoutServices': logoutServices})


@csrf_protect
def contact(request):
    if request.method == "POST":
        email = request.POST.get('email')
        fullname = request.POST.get('fullname')
        desc = request.POST.get('desc')
        # date= request.POST.get('date')
        contact = Contact(email=email, fullname=fullname,
                          desc=desc, date=datetime.today())
        contact.save()
        messages.success(
            request, "Your information is submitted successfully. ")

    return render(request, "contact.html")
    # return HttpResponse("This is the contactpage created from Django..! ")


@csrf_protect
def signup(request):
    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        # else:
        #     return redirect('logouthome')
    else:
        form = signupform()
    return render(request, 'signup.html', {'form': form})


@csrf_protect
def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
<<<<<<< HEAD
            # return render(request, 'index.html')
        else:
            return render(request, 'login.html')
    else:
=======
        else:
            messages.error(request, "Invalid credentials. Please try again.")
            return render(request, "login.html")
    else:
        messages.error(request, "Please login for more details.")
>>>>>>> master
        return render(request, 'login.html')


@csrf_protect
def gallery(request):
    if request.method == 'POST':
        property_form = PropertyDetailsForm(request.POST, request.FILES)
        property_instance = property_form.save(commit=False)  # Don't save yet
        property_instance.owner = request.user  # Set the owner to the logged-in user
        property_instance = property_form.save()
        # form_type = request.POST.get('attachedbathroom')
        # form_type=
        # print(form_type.errors)

        if request.POST.get('attachedbathroom'):
            form = RoomsDetailsForm(request.POST)
            if form.is_valid():
                room = form.save(commit=False)
                room.property = property_instance
                room.save()
                messages.success(
                    request, "Your information is submitted successfully. ")
            else:
                print(form.errors)

        elif request.POST.get('size'):
            form = HousesDetailsForm(request.POST)
            if form.is_valid():
                house = form.save(commit=False)
                # property_id = request.POST.get('property_id')
                # property_obj = Property.objects.get(id=property_id)
                house.property = property_instance
                house.save()
                messages.success(
                    request, "Your information is submitted successfully. ")
            else:
                print(form.errors)

    else:
        property_form = PropertyDetailsForm()
        # print(form.errors)

    return render(request, 'gallery.html', {'property_form': property_form})
