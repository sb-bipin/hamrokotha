from .forms import PropertyDetailsForm, RoomsDetailsForm, HousesDetailsForm
from tkinter import Image
from django.shortcuts import get_object_or_404, render, redirect


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


def home(request):
    return render(request, "index.html")


# def gallery(request):
#     return render(request, "gallery.html")


def index(request):
    return render(request, "index.html")
    # return HttpResponse("This is the homepage created from Django..! ")


def services(request):
    filter_type = request.GET.get("filter")
    print(filter_type)
    # allimages = Property.objects.all()

    if (filter_type == "ac"):
        allimages = Property.objects.filter(
            rooms__acfan="AC").prefetch_related('rooms').order_by("-id")
    elif (filter_type == "lowhighprice"):
        allimages = Property.objects.order_by('price')
    elif (filter_type == "attachbathroom"):
        allimages = Property.objects.filter(
            rooms__attachedbathroom="Yes").prefetch_related('rooms').order_by('-id')
    else:
        allimages = Property.objects.all().order_by('-id')
    return render(request, 'services.html', {'propertydetails': allimages})

    # return render(request, "services.html")
    # return HttpResponse("This is the servicespage created from Django..! ")


def service_details(request, service_id):
    # services = get_object_or_404(Property, id=service_id)
    services = Property.objects.filter(id=service_id)

    return render(request, 'service_details.html', {'services': services})


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
        property_instance = property_form.save()
        # form_type = request.POST.get('attachedbathroom')
        # form_type=
        # print(form_type.errors)

        if request.POST.get('attachedbathroom'):
            form = RoomsDetailsForm(request.POST)
            if form.is_valid():
                room = form.save(commit=False)
                # property_id = request.POST.get('property_id')
                # property_obj = Property.objects.get(id=property_id)
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


# @csrf_protect
# def gallery(request):
#     if request.method == 'POST':
#         property_form = PropertyDetailsForm(request.POST, request.FILES)
#         rooms_form = RoomsDetailsForm(request.POST)
#         houses_form = HousesDetailsForm(request.POST)

#         if property_form.is_valid() and rooms_form.is_valid() and houses_form.is_valid():
#             # Save the Property form data to the database
#             property_instance = property_form.save()
#             # Create a Rooms instance without saving to the database
#             rooms_instance = rooms_form.save(commit=False)
#             houses_instance = houses_form.save(commit=False)

#             rooms_instance.property = property_instance  # Set the foreign key relationship
#             houses_instance.property = property_instance

#             rooms_instance.save()  # Save the Rooms instance with the foreign key relationship
#             houses_instance.save()

#             messages.success(
#                 request, "Your information is submitted successfully. ")
#             # Redirect to a success page or another view
#             # return redirect('property_list')
#         else:
#             print(property_form.errors)
#             print(rooms_form.errors)
#             print(houses_form.errors)

#     else:
#         property_form = PropertyDetailsForm()
#         rooms_form = RoomsDetailsForm()
#         houses_form = HousesDetailsForm()

#     return render(request, 'gallery.html', {'property_form': property_form, 'rooms_form': rooms_form, 'houses_form': houses_form})
