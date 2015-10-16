from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http.response import HttpResponseRedirect
from django.views.generic import DetailView, CreateView, DeleteView
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import List_failure, CustomUser
from .forms import FailureList, Time_filter, RegistrationForm, AccountForm,\
                 DivErrorList
from .func_logical import calc_time_failure

def index(request):
    return render_to_response(r'type_one\index.html', {'user':request.user })

def logout_page(request):
    logout(request)
    return HttpResponseRedirect (r'/type_one/')

def registration_page(request):
    
    if request.method == 'POST':
        form_reg=RegistrationForm(request.POST, error_class=DivErrorList)
        if form_reg.is_valid():
            user1 = CustomUser.objects.create_user(
                            username=form_reg.cleaned_data['username'],
                            email=form_reg.cleaned_data['email'],
                            password=form_reg.cleaned_data['password1'],)
            user = authenticate(username=form_reg.cleaned_data['username'],
                                password = form_reg.cleaned_data['password1'])
            login(request, user)
            return HttpResponseRedirect (r'/type_one/')
    else:
        form_reg=RegistrationForm()
    return render_to_response(r'type_one\registration.html', 
                                 {'form_registration':form_reg})

def account(request,user1):
    
    if request.method == 'GET':
        if request.user.is_authenticated():
            if request.user.username == user1:
                f=AccountForm(initial={
                    'username':request.user.username,
                    'email':User.objects.get(username=user1).email,
                    'first_name':User.objects.get(username=user1).first_name,
                    'last_name':User.objects.get(username=user1).last_name,
                    })
                
                return render_to_response(r'type_one\account_management.html',
                                          {'user':f,
                                           'username': request.user.username })
                
        return HttpResponseRedirect('/type_one/login/')
    elif request.method == 'POST':
        q=get_object_or_404(User, username=user1)
        q.username = request.POST['username']
        q.first_name = request.POST['first_name']
        q.last_name = request.POST['last_name']
        q.save()
        f=AccountForm(initial={'username':request.user.username})
        
        return render_to_response(r'type_one\account_management.html',
                                  {'user':f,
                                   'username': request.user.username }) 

class Create_failure(CreateView):
    form_class = FailureList
    template_name = 'type_one/create.html'
    success_url = '/type_one/confirm/'
    
    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(Create_failure,self).dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        instance=form.save(commit=False)
        name=self.request.user.first_name + ' ' + self.request.user.last_name
        user_nik=self.request.user
        instance.fio_name=name
        instance.username=user_nik
        instance.save()
        return redirect(self.success_url)
    
    def get_form_kwargs(self):
        kwargs = super(Create_failure,self).get_form_kwargs()
        kwargs.update({
                       'error_class':DivErrorList
                       })
        return kwargs
    
def confirm1(request):
    return render_to_response(r'type_one/confirm.html')

def filtering(request):
    if request.method=='POST': 
        filter_form=Time_filter(request.POST, error_class = DivErrorList) 
        if filter_form.is_valid(): 
            if request.POST['station_name_1'] == '':
                #select objects which have time_off < than entered time
                filter_2=List_failure.objects.exclude(
                                        time_on__gte=request.POST['time_off'])
                #than select objects which have time_on > than entered time
                list_of_failure=filter_2.filter(
                                        time_off__gte=request.POST['time_on'])
            else:
                filter_2=List_failure.objects.exclude(
                                        time_on__gte=request.POST['time_off'])
                list_of_failure_1=filter_2.filter(
                                        time_off__gte=request.POST['time_on'])
                #filtering with selected station
                list_of_failure=list_of_failure_1.filter(
                                    station_name=request.POST['station_name_1'])    

            #Calculated summary time of failure
            s=calc_time_failure(list_of_failure)
                        
            return render_to_response(r'type_one\filtering.html',
                                      {'filter_objects':list_of_failure,
                                       'filter_form':filter_form,
                                       'sum':s,
                                       'user':request.user})    
    else:
        filter_form=Time_filter()
        
    return render_to_response(r'type_one\filtering.html',
                              {'filter_form':filter_form,}
                              )

class Failure_detail(DetailView):
    model = List_failure
    context_object_name = 'failure' 
    template_name = r'type_one\detail.html'

class User_detail(DetailView):
    model = User
    context_object_name = 'user'
    template_name = r'type_one\user_detail.html'
    slug_field = 'username'

class Delete_failure(DeleteView):
    model = List_failure
    template_name = r'type_one\delete_failure.html'
    success_url = r'/type_one/list_failure/filtering/'