from django import forms
from .models import CustomUser
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.password_validation import validate_password
import re



class UserRegForm(forms.ModelForm):

    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'phone_number', 'email', 'coop_name')


    def clean(self):
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            self.add_error('password2','Пароли не совпадают.')
        email = self.cleaned_data['email']
        username = self.cleaned_data['username']
        if email and CustomUser.objects.filter(email=email).exclude(username=username).exists():
            self.add_error('email', 'Указанный электронный адрес уже существует')
        phone_number = self.cleaned_data['phone_number']
        if phone_number and CustomUser.objects.filter(phone_number=phone_number).exclude(username=username).exists():
            self.add_error('phone_number', 'Этот мобильный номер уже существует')
        return super().clean()

    def clean_password(self):
        password = self.cleaned_data.get('password')
        try:
            validate_password(password, self.instance)
        except forms.ValidationError as error:
            self.add_error('password', error)
        return password

class LoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class PassResForm(PasswordResetForm):

    def clean_email(self):
        email = self.cleaned_data['email']
        if not CustomUser.objects.filter(email__iexact=email, is_active=True).exists():
            self.add_error('email', 'Пользователя с указанным e-mail не существует.')
        return email


class AddPhoneForm(forms.Form):

    phone_number = forms.CharField()
    coop_name = forms.CharField(required=False)

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        _pattern = re.compile("^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$")
        if not _pattern.match(phone_number):
            self.add_error('phone_number', 'Ввеите существующий мобильный номер')
        if phone_number and CustomUser.objects.filter(phone_number=phone_number).exists():
            self.add_error('phone_number', 'Этот мобильный номер уже существует')
        return phone_number


class UserUpdateProfile(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'phone_number', 'email', 'coop_name')
