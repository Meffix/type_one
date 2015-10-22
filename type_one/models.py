from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class CustomUser (User, models.Model):
    day_of_birthday = models.DateField(blank=True, null=True, 
                                     verbose_name='Дата рождения')

class FailureType(models.Model):
    failure_type = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    
    class Meta:
        ordering = ['failure_type']
    
    def __str__(self):
        return self.failure_type
    
class Station(models.Model):
    station_name = models.CharField(max_length=50)  
    
    class Meta:
        ordering = ['station_name']
        
    def __str__(self):
        return self.station_name  
     
class ListFailure(models.Model):
    station_name = models.ForeignKey(Station, verbose_name=u'Cтанция')
    type_of_failure = models.ForeignKey(FailureType, 
                                      verbose_name=u'Тип повреждения')   
    time_on = models.DateField(verbose_name=u'Дата начала')
    time_off = models.DateField(verbose_name=u'Дата окончания')
    time_1 = models.TimeField(verbose_name=u'Время начала')
    time_2 = models.TimeField(verbose_name=u'Время окончания')
    delt_time = models.DurationField(blank=True, null=True)
    fio_name = models.CharField(max_length=20)
    comment = models.TextField(blank=True, null=True, verbose_name=u'Комментарии')
    username = models.CharField(max_length=20)
     
    def save(self, *args, **kwargs):
        self.datetime_object_1 = datetime.combine(self.time_on, self.time_1)
        self.datetime_object_2 = datetime.combine(self.time_off, self.time_2)
        self.delt_time = self.datetime_object_2 - self.datetime_object_1
        super(ListFailure,self).save(*args, **kwargs)
    
    class Meta:
        ordering = ['time_on']