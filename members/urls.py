from . import views 
from django.urls import path
from .views import *
# from django.contrib.auth import views as auth_views


urlpatterns = [

path('register/',UserRegisterView.as_view(),name='register'),
path('edit_profile/',UserEditView.as_view(),name='edit_profile'),
path('password/',PasswordEditView.as_view()),
path('PasswordChanged',views.PasswordChanged,name='password_changed'),
path('<int:pk>/profile/', ShowProfileView.as_view(),name='show_profile'),
path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(),name='edit_profile_page'),
path('create_profile_page/', CreateProfilePageView.as_view(),name='create_profile_page'),
# path('login/',CustomLoginView.as_view(),name='login')
#path('password/',auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html'))

]