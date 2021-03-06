from django.shortcuts import render_to_response, redirect
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import FailureList, DivErrorList
from .func_logical import calc_time_failure

def index(request):
    return render_to_response(r'type_one\index.html', {'user':request.user})
'''
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
        q = get_object_or_404(User, username=user1)
        q.username = request.POST['username']
        q.first_name = request.POST['first_name']
        q.last_name = request.POST['last_name']
        q.save()
        f = AccountForm(initial={'username':request.user.username})
        return render_to_response(r'type_one\account_management.html',
                                  {'user':f,
                                   'username': request.user.username }) 
'''
class CreateFailure(CreateView):
    form_class = FailureList
    template_name = 'type_one/create.html'
    success_url = '/type_one/confirm/'
    
    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(CreateFailure,self).dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        name = self.request.user.first_name + ' ' + self.request.user.last_name
        user_nik = self.request.user
        instance.fio_name = name
        instance.username = user_nik
        instance.save()
        return redirect(self.success_url)
    
    def get_form_kwargs(self):
        kwargs = super(CreateFailure,self).get_form_kwargs()
        kwargs.update({
                       'error_class':DivErrorList
                       })
        return kwargs
    
def confirm1(request):
    return render_to_response(r'type_one/confirm.html')

#class UserDetail(DetailView):
#    model = User
#    context_object_name = 'user'
#    template_name = r'type_one\user_detail.html'
#    slug_field = 'username'
    