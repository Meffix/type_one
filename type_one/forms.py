from django import forms
from django.utils import timezone
from django.forms.models import ModelForm
from django.forms.widgets import Select, TextInput, Textarea
from django.forms.utils import ErrorList
from django.utils.safestring import mark_safe

from .models import ListFailure

'''
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=254, 
                               widget=TextInput(attrs={'placeholder':'Логин'}))
    password = forms.CharField(label=("Password"), 
                               widget=forms.PasswordInput(
                                        attrs={'placeholder':'Пароль'}
                                        ) 
                               )
'''
class CalendarWidget(forms.TextInput):
    class Media:
        css = {
           'all':(r'//code.jquery.com/ui/1.11.4/themes/smoothness/jquery-ui.css',
                   ),
           }
        js = (r'//code.jquery.com/jquery-1.10.2.js',
              r'//code.jquery.com/ui/1.11.4/jquery-ui.js',)
    
class DivErrorList(ErrorList):
    '''
    Set errorlist as <div>
    '''
    def __str__(self):
        return self.as_divs()
    def as_divs(self):
        if not self: return u''
        return mark_safe(u'<div class="errorlist">%s</div>' \
                        % ''.join([u'<div class="error">%s</div>' \
                                     % e for e in self]))
            
class FailureList(ModelForm):
    '''
    Form for add Failure
    '''
    class Meta:
        model = ListFailure
        exclude = ['delt_time','fio_name','username']
        widgets = {'station_name':Select (attrs={'size':1, 
                                                'class':'form-control',}),
                   'type_of_failure':Select (attrs={'size':1, 
                                                'class':'form-control',}),
                   'time_on':CalendarWidget (attrs={'class':'form-control',}),
                   'time_off':CalendarWidget (attrs={'class':'form-control',}),
                   'time_1':TextInput (attrs={'class':'form-control',}),
                   'time_2':TextInput (attrs={'class':'form-control',}),
                   'comment':Textarea (attrs={'class':'form-control', 
                                               'rows':'3'}),
                   }
 
    def clean_time_on(self):
        '''
        Check time_on < time now
        '''
        data_1 = self.cleaned_data['time_on']
        data_2 = timezone.now().date()
        if data_1 > data_2:
            raise forms.ValidationError(u'Введите верную дату начала аварии!')
        return data_1
      
    def clean_time_off(self):
        '''
        Check time_off < time now
        '''
        data_1 = self.cleaned_data['time_off']
        data_2 = timezone.now().date()
        if data_1 > data_2:
            raise forms.ValidationError(
                                    u'Введите верную дату завершения аварии!'
                                    )
        return data_1
    
    def clean(self):
        '''
        Check time_on < time_off
        '''
        cleaned_data = super(FailureList,self).clean()
        data_1 = cleaned_data.get('time_on')
        data_2 = cleaned_data.get('time_off')
        if data_1 and data_2:
            if data_1 > data_2:
                msg = u'Дата начала должна быть меньше даты окончания!'
                self.add_error('time_on',msg)

'''
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
'''