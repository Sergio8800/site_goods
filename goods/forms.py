from django import forms
# from snowpenguin.django.recaptcha3.fields import ReCaptchaField
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .models import *


class AddCar(forms.ModelForm):
    class Meta:
        model = Car
        fields = ("author", "title", "genres", "category", "fuel", "price")
        widgets = {'author': forms.HiddenInput()}
        # def __init__(self, *args,**kwargs):
        #     super().__init__(*args,**kwargs)
        #     for field in self.fields:
        #         self.fields[field].widget.attrs['class'] = 'form-control'


class ReviewForm(forms.ModelForm):
    """Форма отзывов"""

    # captcha = ReCaptchaField()

    class Meta:
        model = Reviews
        fields = ("name", "email", "text")
        # widgets = {
        #     "name": forms.TextInput(attrs={"class": "form-control border"}),
        #     "email": forms.EmailInput(attrs={"class": "form-control border"}),
        #     "text": forms.Textarea(attrs={"class": "form-control border"})
        # }


class RatingForm(forms.ModelForm):
    """Форма добавления рейтинга"""
    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Rating
        fields = ("star", "email",)


class AuthForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "password")


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        # fields = "__all__"
        fields = ("username", "password", "email")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

