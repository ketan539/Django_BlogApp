from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import *
from .models import *
from .forms import *
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
# def info(request):
#     return render(request,'info.html')

def home(request):
    return render(request,'home.html')


class HomeView(ListView):
    model= Post
    template_name='info.html'
    # ordering=['-id']
    ordering=['-post_date']
    paginate_by=5

    def get_context_data(self,*args, **kwargs):
        cat_menu= Category.objects.all()
        context= super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"]= cat_menu
        return context

def LikePostView(request,pk):
    post= get_object_or_404(Post, id=request.POST.get('post_id'))
    liked=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked= False
    else:
        post.likes.add(request.user)
        liked=True
    
    return HttpResponseRedirect(reverse('details', args=[str(pk)]))

class DetailsView(DetailView):
    model= Post
    template_name='details.html'

    def get_context_data(self,*args, **kwargs):
        context= super(DetailsView, self).get_context_data(*args, **kwargs)
        data=get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes= data.total_likes()

        liked= False
        if data.likes.filter(id=self.request.user.id).exists():
            liked=True
        context["total_likes"]= total_likes
        context['liked']=liked
        return context

class AddPostView(CreateView):
    model=Post
    form_class=PostForm
    template_name='add_post.html'
    # fields='__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    # def post(self, request, *args, **kwargs):
    #     form = self.get_form()
    #     if form.is_valid():
    #         instance = form.save(commit=False)
    #         instance.user = request.user
    #         instance.header_image = request.FILES.get('header_image')
    #         instance.save()
    #         return redirect(self.success_url)
    #     else:
    #         return self.form_invalid(form)
    

class AddCategoryView(CreateView):
    model=Category
    form_class=CategoryForm
    template_name='add_post.html'
    # fields='__all__'

class AddCommentView(CreateView):
    model=Comment
    form_class=CategoryForm
    template_name='add_comment.html'
    # fields='__all__'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url=reverse_lazy('info') 

class UpdatePostView(UpdateView):
    model=Post
    form_class=PostForm
    template_name='update_post.html'


class DeletePostView(DeleteView):
    model=Post
    template_name='delete.html'

    success_url=reverse_lazy('info')

def CategoryView(request,cats):
    category_post=Post.objects.filter(category=cats)
    return render(request,'categories.html',{'cats':cats,'category_post':category_post})