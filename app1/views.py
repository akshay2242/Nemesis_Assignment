from .forms import CustomUserForm
from django.views.generic import CreateView, ListView, UpdateView,DeleteView,TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from .models import CustomUser
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.

# Home view
class Home(TemplateView):
    template_name = 'app1/home.html'

# SignUp view
class Signup(CreateView):
    form_class = CustomUserForm
    template_name = 'app1/signup.html'
    success_url = '/login/'

# Login view 
class Login(LoginView):
    template_name = 'app1/login.html'

# All Users details view
@method_decorator(login_required, name='dispatch')
class AllUsersDetails(ListView):
    model = CustomUser
    template_name = 'app1/all_users_details.html'
    context_object_name = 'data'

# Update User view
@method_decorator(login_required, name='dispatch')
class UpdateUserDetail(UpdateView):
    model = CustomUser
    fields = ['username', 'email', 'address']
    template_name = 'app1/update_user.html'
    success_url = '/all_users_details/'

# Delete User view
@method_decorator(login_required, name='dispatch')
class DeleteUser(DeleteView):
    model = CustomUser
    success_url = '/all_users_details/'
    template_name = 'app1/user_delete.html'

# Logout view
@method_decorator(login_required, name='dispatch')
class Logout(LogoutView):
    template_name = 'app1/logout.html'
    success_url = '/user_detail/'
    