from django import forms
from django.forms.models import ModelForm
from django.forms.widgets import TextInput, EmailInput, PasswordInput
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.fields import CharField

from type_one.models import CustomUser


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=254, 
                               widget=TextInput(attrs={'placeholder':'Логин'}))
    password = forms.CharField(label=("Password"), 
                               widget=forms.PasswordInput(
                                        attrs={'placeholder':'Пароль'}
                                        ) 
                               )
class RegistrationForm(UserCreationForm):
    password1 = CharField(widget=PasswordInput(attrs={'class':'form-control',})
                          )
    password2 = CharField(widget=PasswordInput(attrs={'class':'form-control',})
                          )
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {'username':TextInput(attrs={'class':'form-control'},),
                   'email':EmailInput(attrs={'class':'form-control'},),}
    
    def clean_email(self):
        try:
            User.objects.get(email=self.cleaned_data['email'])
        except ObjectDoesNotExist:
            return self.cleaned_data['email']
        raise forms.ValidationError(
                            u'Пользователь с таким e-mail уже зарегистрирован'
                            ) 
             
    def clean_password2(self):
        if len(self.cleaned_data['password1']) < 6:
            raise forms.ValidationError(u'Минимальная  длина пароля 6 символов')
        if 'password1' in self.cleaned_data:
            p1 = self.cleaned_data['password1']
            p2 = self.cleaned_data['password2']
            if p1 == p2:
                return p2
        raise forms.ValidationError("Введите одинаковые пароли")

class AccountForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'day_of_birthday', 
                'first_name', 'last_name', 'email']