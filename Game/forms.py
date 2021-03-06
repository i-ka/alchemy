from django import forms
from django.contrib.auth.models import User
from alchemysite import settings
from django.core.mail import EmailMessage

from AlchemyCommon.models import UserProfile, Report
from AlchemyCommon.utils import getActivationEmailText
# Create your views here.


class RegisterForm(forms.Form):

    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                            'placeholder':'Имя пользователя'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder':'Email'}))

    pass1 = forms.CharField(label="Пароль",
                            min_length=6,
                            max_length=30,
                            widget=forms.PasswordInput(attrs={'class':'form-control',
                                                              'placeholder':'Пароль'}))

    pass2 = forms.CharField(label="Пароль ещё раз",
                            widget=forms.PasswordInput(attrs={'class':'form-control',
                                                                'placeholder':'Пароль еще раз'}))
    def save(self):
        user = User(username=self.cleaned_data['username'],
                    email=self.cleaned_data['email'])
        user.set_password(self.cleaned_data['pass1'])
        user.save()
        if settings.EMAIL_CONFIRM:
            user.is_active = False
            (token, emailText) = getActivationEmailText(user)
            user.profile.activationToken = token
            user.profile.save()
            msg = EmailMessage ('Registration confirm',
                                emailText,
                                'alchemy@noreply.hh',
                                [self.cleaned_data['email']])
            msg.content_subtype = "html"
            msg.send()
            user.save()
        return user

    def clean_email(self):
        if (User.objects.filter(email=self.cleaned_data['email']).exists()):
            raise forms.ValidationError("Такой email уже занят!")
        return self.cleaned_data['email']

    def clean_username(self):
        if (User.objects.filter(username=self.cleaned_data['username']).exists()):
            raise forms.ValidationError("Такое имя пользователя уже занято!")
        return self.cleaned_data['username']

    def clean_pass2(self):
        if (self.cleaned_data["pass2"] != self.cleaned_data.get("pass1", "")):
            raise forms.ValidationError("Пароли не совпадают")
        return self.cleaned_data["pass2"]


class ReportForm(forms.ModelForm):

    class Meta:
        model = Report

        fields = [
            'text',
            'screenshot'
        ]

        widgets = {
            'text': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Текст жалобы/предложения'}),
            'screenshot': forms.ImageField()
        }
