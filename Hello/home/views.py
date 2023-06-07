from .forms import PropertyDetailsForm, RoomsDetailsForm
from tkinter import Image
from django.shortcuts import render, redirect

from .models import Rooms

# from .models import RoomsDetails
from .forms import signupform
from django.contrib.auth import login, authenticate
from django.contrib.auth import authenticate, login
from datetime import datetime
from django.shortcuts import redirect, render, HttpResponse
from home.models import Contact, Property
from django.contrib import messages
from .forms import signupform
from django.views.decorators.csrf import csrf_protect


def logout(request):
    return render(request, "logouthome.html")

# Create your views here.


def home(request):
    return render(request, "index.html")


# def gallery(request):
#     return render(request, "gallery.html")


def index(request):
    return render(request, "index.html")
    # return HttpResponse("This is the homepage created from Django..! ")


def services(request):
    allimages = Property.objects.all()
    return render(request, 'services.html', {'roomsdetails': allimages})

    # return render(request, "services.html")
    # return HttpResponse("This is the servicespage created from Django..! ")


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
            return render(request, 'index.html')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


# @csrf_protect
# def gallery(request):
#     # dump(gallery)
#     if request.method == 'POST':
#         # dump(request)
#         form = RoomsDetailsForm(request.POST, request.FILES)
#         if form.is_valid():
#         # dump(form)
#         form.save()
#         messages.success(
#         request, "Your information is submitted successfully. ")
#         return HttpResponse('Successfully uploaded')
#         else:
#         dump(form)
#         print(form.errors)
#         dump(form)
#         return HttpResponse('Not Successful ')
#     else:
#         form = RoomsDetailsForm()
#     return render(request, "gallery.html", {"form": form})


@csrf_protect
def gallery(request):
    if request.method == 'POST':
        property_form = PropertyDetailsForm(request.POST, request.FILES)
        rooms_form = RoomsDetailsForm(request.POST)

        if property_form.is_valid() and rooms_form.is_valid():
            # Save the Property form data to the database
            property_instance = property_form.save()
            # Create a Rooms instance without saving to the database
            rooms_instance = rooms_form.save(commit=False)
            rooms_instance.property = property_instance  # Set the foreign key relationship
            rooms_instance.save()  # Save the Rooms instance with the foreign key relationship
            messages.success(
                request, "Your information is submitted successfully. ")
            # Redirect to a success page or another view
            # return redirect('property_list')
        else:
            print(property_form.errors)
            print(rooms_form.errors)

    else:
        property_form = PropertyDetailsForm()
        rooms_form = RoomsDetailsForm()

    return render(request, 'gallery.html', {'property_form': property_form, 'rooms_form': rooms_form})
