from django import forms
from AlchemyCommon.models import UserProfile
from django.contrib.auth.models import User

# Create your views here.


class RegisterForm(forms.Form):

    username = forms.CharField(max_length=30)
    email = forms.EmailField()

    pass1 = forms.CharField(widget=forms.PasswordInput,
                            label="Пароль",
                            min_length=6,
                            max_length=30)

    pass2 = forms.CharField(widget=forms.PasswordInput, label="Пароль ещё раз")

    def clean_pass2(self):
        if (self.cleaned_data["pass2"] != self.cleaned_data.get("pass1", "")):
            raise forms.ValidationError("Пароли не совпадают")
            return self.cleaned_data["pass2"]
