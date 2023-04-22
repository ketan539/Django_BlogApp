from django import forms
from .models import *

choices= Category.objects.all().values_list('name','name')


choice_list=[]

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields=('title', 'author','category','body','header_image','snippet')
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Title'}),
            'author':forms.TextInput(attrs={'class':'form-control','value':'','id':'jsid','type':'hidden'}),
            #'author':forms.Select(attrs={'class':'form-control','placeholder':'Select Author'}),
            'category':forms.Select(choices=choices, attrs={'class':'form-select','placeholder':'Select Category'}),
            'body':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter the Details'}),
            'snippet':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Snippet'}),
            'header_image':forms.FileInput(attrs={'class':'form-control','placeholder':'Upload the Image'})
           }
        labels ={
            'header_image':'Image',
            'body':'Message'
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','body')
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'}),
            'body':forms.Textarea(attrs={'class':'form-control','placeholder':'Write a comment'})
        }
        labels={
        'name':'Name',
        'body':'Comment'
        }