from django.forms.models import ModelForm
from django.forms.widgets import Select

from .models import ListFailureFiltering
from type_one.forms import CalendarWidget

class TimeFilter(ModelForm):
    '''
    Form for filtering failure
    '''
    class Meta:
        model = ListFailureFiltering
        fields = ['station_name_1', 'time_on', 'time_off']
        widgets = {'station_name_1':Select (attrs={'size':1, 
                                                'class':'form-control',}),
                 'time_on':CalendarWidget (attrs={'class':'form-control'}),
                 'time_off':CalendarWidget (attrs={'class':'form-control'})
                 }