from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from datetime import datetime, date
from ckeditor.fields import RichTextField


class Post(models.Model):
    title=models.CharField(max_length=255)
    header_image=models.ImageField(null=True, blank=True,upload_to='images/')
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    body=RichTextField(blank=True,null=True)
    # body= models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category=models.CharField(max_length=255,default='Smartphones')
    likes=models.ManyToManyField(User,related_name='blog_posts')
    snippet=models.CharField(max_length=255)

    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.title + ' | '  + str(self.author)
    
    def get_absolute_url(self):
        return reverse('info')

class Category(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name  
    
    def get_absolute_url(self):
        # return reverse_lazy('add_post', kwargs={'pk': self.kwargs['pk']})
        return reverse('info')
    

class Profile(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    phone_number= models.CharField(max_length=20,blank=True)
    company_name= models.CharField(max_length=255,null=True)
    profile_image= models.FileField(upload_to='profile_images/',null=True)

    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
       return reverse('info')
    

class Comment(models.Model):
    post=models.ForeignKey(Post,related_name='comments', on_delete=models.CASCADE)
    name= models.CharField(max_length=20,blank=True)
    body= models.TextField()
    comment_date= models.DateField(auto_now_add=True)

    def __str__(self):
        return self.post.title + ' | '  + str(self.name) + ' | '  + str(self.comment_date)
    
    def get_absolute_url(self):
        # return reverse_lazy('add_post', kwargs={'pk': self.kwargs['pk']})
       return reverse('info')

