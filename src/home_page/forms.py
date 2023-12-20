from catalog.models import AppUser

from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm
from django.core.exceptions import ValidationError


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = AppUser
        fields = (
            "username",
            "email",
            "name",
            "surname",
            "phone",
            "country",
            "city",
            "index",
            "address",
            "reserve_address",
            "password",
            "additional_info",
        )


class MyUserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)

    class Meta:
        model = AppUser
        fields = (
            "username",
            "email",
            "name",
            "surname",
            "phone",
            "country",
            "city",
            "index",
            "address",
            "reserve_address",
            "password1",
            "password2",
            "additional_info",
        )

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


# Form for application


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    index = forms.IntegerField(required=True)
    name = forms.CharField(required=True, max_length=30)
    surname = forms.CharField(required=True, max_length=30)
    phone = forms.IntegerField(required=True, help_text="Enter the number in international format.")
    country = forms.CharField(required=True)
    city = forms.CharField(required=True, max_length=30)
    address = forms.CharField(required=True, max_length=60)
    reserve_address = forms.CharField(required=False, max_length=60)
    additional_info = forms.CharField(required=False, max_length=150)

    class Meta:
        model = AppUser
        fields = (
            "username",
            "email",
            "name",
            "surname",
            "phone",
            "country",
            "city",
            "index",
            "address",
            "reserve_address",
            "password1",
            "password2",
            "additional_info",
        )

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.name = self.cleaned_data["name"]
        user.surname = self.cleaned_data["surname"]
        user.country = self.cleaned_data["country"]
        user.city = self.cleaned_data["city"]
        user.index = self.cleaned_data["index"]
        user.address = self.cleaned_data["address"]
        user.reserve_address = self.cleaned_data["reserve_address"]
        user.additional_info = self.cleaned_data["additional_info"]
        if commit:
            user.save()
        return user
