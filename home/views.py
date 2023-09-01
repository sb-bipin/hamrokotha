from django.shortcuts import render, redirect
from django.shortcuts import render
from django.db import models
from django.http import JsonResponse
import logging
from .forms import ClientDetailsForm, PropertyDetailsForm, RoomsDetailsForm, HousesDetailsForm
from tkinter import Image
from django.shortcuts import get_object_or_404, render, redirect
import pytest

# from .models import RoomsDetails
from .forms import signupform
from django.contrib.auth import login, authenticate
from django.contrib.auth import authenticate, login
from datetime import datetime
from django.shortcuts import redirect, render, HttpResponse
from home.models import Contact, Property, Client
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


# This is comment

def services(request):
    filter_type = request.GET.get("filter")

    if filter_type == "ac":
        allimages = Property.objects.filter(rooms__acfan="ac")
    elif filter_type == "lowhighprice":
        allimages = Property.objects.filter(rooms__wifiavailable="Yes")
    elif filter_type == "attachbathroom":
        allimages = Property.objects.filter(rooms__attachedbathroom="Yes")
    else:
        allimages = Property.objects.all().order_by("-id")

    context = {'propertydetails': allimages}
    return render(request, 'services.html', context)


def service_details(request, service_id):
    # services = get_object_or_404(Property, id=service_id)
    services = Property.objects.filter(id=service_id)
    return render(request, 'service_details.html', {'services': services})


def logoutService(request):
    logoutServices = Property.objects.all()[:12]
    # messages.error(request, "Please log in to see more.")
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
        else:
            messages.error(request, "Invalid credentials. Please try again.")
            return render(request, "login.html")
    else:
        messages.error(request, "Please login for more details.")
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


@csrf_protect
def client(request):
    if request.method == "POST":
        client_form = ClientDetailsForm(request.POST)
        if client_form.is_valid():
            client_instance = client_form.save(commit=False)  # Don't save yet
            client_instance.client = request.user  # Set the owner to the logged-in user

            client_instance = client_form.save()
            messages.success(
                request, "Your information is submitted successfully. ")
        else:
            messages.success(request, "your data is not valid")
            print(client_form.errors)
            return render(request, 'service_details.html', {'client_form': client_form})
    else:
        client_form = ClientDetailsForm()

    return render(request, 'service_details.html', {'client_form': client_form})
    # return HttpResponse("This is the contactpage created from Django..! ")


def inbox(request):
    clientmsg = Client.objects.exclude(client_id=request.user.id)
    return render(request, 'inbox.html', {'clientmsg': clientmsg})


def delete_service(request, service_id):
    try:
        service = Property.objects.get(pk=service_id)
        if service.delete():
            messages.success(request, "Yur property is deleted successfully.")
        else:
            messages.success(
                request, "Yur property is not deleted.Error in deletion.")

    except Property.DoesNotExist:
        # Redirect to the page where properties are listed
        print(service.errors)
    return redirect('home')
