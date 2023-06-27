from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Houses, Rooms, Property


class signupform(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(signupform, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.full_name = self.cleaned_data['first_name']
        user.address = self.cleaned_data['last_name']
        user.address = self.cleaned_data['username']
        user.address = self.cleaned_data['password1']

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
