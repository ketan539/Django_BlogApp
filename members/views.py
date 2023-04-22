from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import *
from data_cont.models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import RegisterForm, EditForm, PasswordChangingForm, EditProfilePageForm, CreateProfilePageForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import authenticate, login

# class CustomLoginView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'registration/login.html')

#     def post(self, request, *args, **kwargs):
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('registration/show_profile', pk=request.user.profile.pk)
#         else:
#             return render(request, 'registration/login.html', {'error_message': 'Invalid login credentials'})


class UserRegisterView(generic.CreateView):
    form_class=RegisterForm
    template_name='registration/register.html'

    success_url= reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class=EditForm
    template_name='registration/edit_profile.html'

    success_url= reverse_lazy('info')

    def get_object(self):
        return self.request.user


class PasswordEditView(PasswordChangeView):
    form_class= PasswordChangingForm
    template_name='registration/change_password.html'
    success_url= reverse_lazy('password_changed')

def PasswordChanged(request):
    return render(request,'registration/password_changed.html')


class ShowProfileView(DetailView):
    model=Profile
    template_name='registration/show_profile.html'

    def get_context_data(self, *args, **kwargs): 
        page_user= Profile.objects.all()
        context= super(ShowProfileView,self).get_context_data(*args, **kwargs)

        page_user= get_object_or_404(Profile,id=self.kwargs['pk'])
        context['page_user']= page_user
        return context
    

class EditProfilePageView(generic.UpdateView):
    model=Profile
    form_class= EditProfilePageForm
    template_name='registration/edit_profile_page.html'
    # fields='__all__'
    success_url=reverse_lazy('info')


class CreateProfilePageView(CreateView):
    model=Profile
    form_class= CreateProfilePageForm
    template_name='registration/create_profile.html'
    # fields='__all__'
    # success_url=reverse_lazy('info')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
