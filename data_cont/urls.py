from . import views 
from django.urls import path
from .views import *

urlpatterns = [

path('home',views.home,name='home'),
path('',views.home,name='home'),
# path('info',views.info,name='info'),
path('info',HomeView.as_view(),name='info'),
path('article/<int:pk>', DetailsView.as_view(),name='details'),
path('article/edit/<int:pk>', UpdatePostView.as_view(),name='update_post'),
path('article/<int:pk>/remove', DeletePostView.as_view(),name='delete'),
path('post/',AddPostView.as_view(),name='add_post'),
path('article/<int:pk>/comment/',AddCommentView.as_view(),name='add_comment'),
path('category/',AddCategoryView.as_view(),name='add_category'),
path('categories/<str:cats>',views.CategoryView,name='categories'),
path('like/<int:pk>',views.LikePostView,name='like_post')


]