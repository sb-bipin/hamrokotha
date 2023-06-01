from tkinter import Image
from django.shortcuts import render, redirect

from .models import RoomsDetails
from .forms import RoomsDetailsForm, signupform
from django.contrib.auth import login, authenticate
from django.contrib.auth import authenticate, login
from datetime import datetime
from django.shortcuts import redirect, render, HttpResponse
from home.models import Contact
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
    allimages = RoomsDetails.objects.all()
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


@csrf_protect
def gallery(request):
    # dump(form1)
    if request.method == 'POST':
        # dump(request)
        form1 = RoomsDetailsForm(request.POST, request.FILES)
        if form1.is_valid():
            # dump(form1)
            form1.save()
            messages.success(
                request, "Your information is submitted successfully. ")
            # return HttpResponse('Successfully uploaded')
        else:
            dump(form1)
            print(form1.errors)
            # dump(form1)
            # return HttpResponse('Not Successful ')
    else:
        form1 = RoomsDetailsForm()
    return render(request, "gallery.html", {"form": form1})
