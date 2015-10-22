from django.shortcuts import render_to_response
from django.views.generic import DetailView, DeleteView

from .forms import TimeFilter
from type_one.forms import DivErrorList
from type_one.models import ListFailure
from type_one.func_logical import calc_time_failure

def filtering(request):
    if request.method == 'POST': 
        filter_form = TimeFilter(request.POST, error_class = DivErrorList) 
        if filter_form.is_valid(): 
            if request.POST['station_name_1'] == '':
                #Select objects which have time_off < than entered time
                filter_2 = ListFailure.objects.exclude(
                                        time_on__gte=request.POST['time_off'])
                #Than select objects which have time_on > than entered time
                list_of_failure = filter_2.filter(
                                        time_off__gte=request.POST['time_on'])
            else:
                filter_2 = ListFailure.objects.exclude(
                                        time_on__gte=request.POST['time_off'])
                list_of_failure_1 = filter_2.filter(
                                        time_off__gte=request.POST['time_on'])
                #Filtering with selected station
                list_of_failure = list_of_failure_1.filter(
                                    station_name=request.POST['station_name_1'])    

            #Calculated summary time of failure
            s = calc_time_failure(list_of_failure)
            
            no_fail = False
            if len(list_of_failure) == 0: no_fail = True
            
            return render_to_response(r'view_failures\filtering.html',
                                      {'filter_objects':list_of_failure,
                                       'filter_form':filter_form,
                                       'sum':s,
                                       'user':request.user,
                                       'no_failure':no_fail,})    
    else:
        filter_form = TimeFilter()
        
    return render_to_response(r'view_failures\filtering.html',
                              {'filter_form':filter_form,}
                              )

class FailureDetail(DetailView):
    model = ListFailure
    context_object_name = 'failure' 
    template_name = r'view_failures\detail.html'
    
class DeleteFailure(DeleteView):
    model = ListFailure
    #template_name = r'view_failures\delete_failure.html'
    success_url = r'/list_failure/filtering/'
