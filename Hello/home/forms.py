from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Houses, Rooms, Property


class signupform(UserCreationForm):
    username = forms.CharField(
        max_length=30, required=True, help_text='Required.')
    first_name = forms.CharField(
        max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(
        max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')
    password1 = forms.EmailField(
        max_length=254, required=True, help_text='Required Password.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(signupform, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.username = self.cleaned_data['username']
        user.password1 = self.cleaned_data['password1']

        if commit:
            user.save()
        return user


# class RoomsDetailsForm(forms.ModelForm):
#     class Meta:
#         model = RoomsDetails
#         fields = ("name", "address", "phone", "imgfield", "price",
#                   "payingmodel", "attachedbathroom", "wifiavailable", "acfan", "descp")


class PropertyDetailsForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'


class RoomsDetailsForm(forms.ModelForm):
    class Meta:
        model = Rooms
        fields = {"attachedbathroom", "wifiavailable", "acfan"}


class HousesDetailsForm(forms.ModelForm):
    class Meta:
        model = Houses
        fields = {"size", "totalrooms"}


# class FlatsDetailsForm(forms.ModelForm):
#     class Meta:
#         model = Flats
#         fields = '__all__'
