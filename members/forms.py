from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from data_cont.models import *



class RegisterForm(UserCreationForm):

    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your Email Address'}))
    first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your First Name'}))
    last_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Last Name'}))

    class Meta:
        model= User
        fields= ('username', 'email','first_name','last_name', 'password1', 'password2' )

    def __init__(self, *args, **kwargs):
        super(RegisterForm,self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'



class EditForm(UserChangeForm):

    class Meta:
        model= User
        fields= ('username', 'first_name','last_name',
                 'email')

    def __init__(self, *args, **kwargs):
        super(EditForm,self).__init__(*args, **kwargs)

        # self.fields['last_login'].widget.attrs['class']='form-control'
        # self.fields['is_superuser'].widget.attrs['class']='form-check-input'
        # self.fields['groups'].widget.attrs['class']='form-select'
        # self.fields['user_permissions'].widget.attrs['class']='form-select'
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['first_name'].widget.attrs['class']='form-control'
        self.fields['last_name'].widget.attrs['class']='form-control'
        self.fields['email'].widget.attrs['class']='form-control'
      
        # self.fields['is_staff'].widget.attrs['class']='form-check-input'
        # self.fields['is_active'].widget.attrs['class']='form--check-input'
        # self.fields['date_joined'].widget.attrs['class']='form-control'
    
class PasswordChangingForm(PasswordChangeForm):


    old_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your old password','type':'password'}))
    new_password1=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your new password','type':'password','label':'New Password'}))
    new_password2=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Re-Enter you new password','type':'password'}))

    class Meta:
        model= User
        fields='__all__'

    
    # labels ={

    #     'id_new_password1':'New Password',
    #     'id_new_password2':'Re-Enter Password'
           
    #    }


class EditProfilePageForm(forms.ModelForm):
    
    phone_number=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter your contact number'}))
    company_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your company name','label':'New Password'}))
    profile_image=forms.FileField(max_length=100,widget=forms.FileInput(attrs={'class':'form-control','placeholder':'Re-Enter you new password'}))
    

    class Meta:
        model= Profile
        fields=('profile_image','phone_number','company_name')





class CreateProfilePageForm(forms.ModelForm):
    
    phone_number=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter your contact number'}))
    company_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your company name','label':'New Password'}))
    profile_image=forms.FileField(max_length=100,widget=forms.FileInput(attrs={'class':'form-control','placeholder':'Re-Enter you new password'}))
    

    class Meta:
        model= Profile
        fields=('profile_image','phone_number','company_name')



