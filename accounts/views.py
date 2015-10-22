from django.shortcuts import render_to_response, get_object_or_404
from django.http.response import HttpResponseRedirect
from django.views.generic import DetailView
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User

from type_one.models import CustomUser
from type_one.forms import DivErrorList
from .forms import RegistrationForm, AccountForm                 

def logout_page(request):
    logout(request)
    return HttpResponseRedirect (r'/type_one/')

def registration_page(request):
    if request.method == 'POST':
        form_reg = RegistrationForm(request.POST, error_class=DivErrorList)
        if form_reg.is_valid():
            user1 = CustomUser.objects.create_user(
                            username=form_reg.cleaned_data['username'],
                            email=form_reg.cleaned_data['email'],
                            password=form_reg.cleaned_data['password1'],)
            user = authenticate(username=form_reg.cleaned_data['username'],
                                password=form_reg.cleaned_data['password1'])
            login(request, user)
            return HttpResponseRedirect (r'/type_one/')
    else:
        form_reg = RegistrationForm()
    return render_to_response(r'account\registration.html', 
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
                return render_to_response(r'account\account_management.html',
                                          {'user':f,
                                           'username': request.user.username })
                
        return HttpResponseRedirect('/type_one/login/')
    
    elif request.method == 'POST':
        q = get_object_or_404(User, username=user1)
        q.username = request.POST['username']
        q.first_name = request.POST['first_name']
        q.last_name = request.POST['last_name']
        q.save()
        f = AccountForm(initial={'username':request.user.username})
        return render_to_response(r'account\account_management.html',
                                  {'user':f,
                                   'username': request.user.username }) 
        
class UserDetail(DetailView):
    model = User
    context_object_name = 'user'
    template_name = r'account\user_detail.html'
    slug_field = 'username'
