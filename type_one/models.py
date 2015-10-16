from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class CustomUser (User, models.Model):
    day_of_birthday=models.DateField(blank=True, null=True, 
                                     verbose_name='Дата рождения')

type_choices=(
                  ('Critical', (
                                ('Ethernet link down','Ethernet link down'),
                                ('Crit_2','Crit_2'),
                                )
                   ),
                  ('Major', (
                             ('Major_1','Major_1'),
                             ('Major_2','Major_2'),
                             )
                   ),
                  )
   
class Failure_type(models.Model):
    failure_type=models.CharField(max_length=50, choices=type_choices)
    
    class Meta:
        ordering=['failure_type']
    
    def __str__(self):
        return self.failure_type
    
class Fio(models.Model):
    fio=models.CharField(max_length=50)
    
    def __str__(self):
        return self.fio

class Station(models.Model):
    station_name=models.CharField(max_length=50)  
    
    class Meta:
        ordering = ['station_name']
        
    def __str__(self):
        return self.station_name  
    
    
        
class List_failure(models.Model):
    station_name=models.ForeignKey(Station, verbose_name=u'Cтанция')
    type_of_failure=models.ForeignKey(Failure_type, 
                                      verbose_name=u'Тип повреждения')   
    time_on=models.DateField(verbose_name=u'Дата начала')
    time_off=models.DateField(verbose_name=u'Дата окончания')
    time_1 = models.TimeField(verbose_name = u'Время начала')
    time_2 = models.TimeField(verbose_name = u'Время окончания')
    delt_time=models.DurationField(blank=True, null=True)
    fio_name=models.CharField(max_length=20)
    comment=models.TextField(blank=True, null=True, verbose_name=u'Комментарии')
    username=models.CharField(max_length=20)
     
    def save(self, *args, **kwargs):
        self.datetime_object_1 = datetime.combine(self.time_on, self.time_1)
        self.datetime_object_2 = datetime.combine(self.time_off, self.time_2)
        self.delt_time = self.datetime_object_2 - self.datetime_object_1
        super(List_failure,self).save(*args, **kwargs)
    
    class Meta:
        ordering = ['time_on']

class List_failure_for_filtering(List_failure, models.Model):
    station_name_1=models.ForeignKey(Station, 
                                     blank=True, null=True, 
                                     verbose_name=u'Станция')

    