from django.db import models
from type_one.models import ListFailure, Station

class ListFailureFiltering(ListFailure, models.Model):
    station_name_1 = models.ForeignKey(Station, 
                                     blank=True, null=True, 
                                     verbose_name=u'Станция')