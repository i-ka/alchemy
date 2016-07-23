from django import forms
from AlchemyCommon.models import UserProfile
from django.contrib.auth.models import User

# Create your views here.


class RegisterForm(forms.Form):

    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                            'placeholder':'Username'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder':'Email'}))

    pass1 = forms.CharField(label="Пароль",
                            min_length=6,
                            max_length=30,
                            widget=forms.PasswordInput(attrs={'class':'form-control',
                                                              'placeholder':'Password'}))

    pass2 = forms.CharField(label="Пароль ещё раз",
                            widget=forms.PasswordInput(attrs={'class':'form-control',
                                                                'placeholder':'Repeat Password'}))

    def clean_pass2(self):
        if (self.cleaned_data["pass2"] != self.cleaned_data.get("pass1", "")):
            raise forms.ValidationError("Пароли не совпадают")
            return self.cleaned_data["pass2"]
