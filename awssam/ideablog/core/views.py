
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Products,MyModel,feeds




def home(request):
	
	context={
	'posts':Post.objects.all()

	}

	return render (request,'blog/home.html',context)

class PostListView(ListView):
    model = Post
    template_name ='blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name ='posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
	model=Post
	template_name = 'blog/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content','description']
    template_name = 'blog/post_form.html'  # <app>/<model>_<viewtype>.html


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)





class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):

	model=Post
	fields=['title','content','description']
	template_name='blog/post_form.html'

	def form_valid(self, form):
		form.instance.author=self.request.user
		return super().form_valid(form)

	def test_func(self):

	    post =self.get_object()
	    if self.request.user==post.author:
	     	return True
	    return False	



class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):

	model=Post
	success_url='/'
	template_name = 'blog/post_confirm_delete.html'




	def test_func(self):

	    post =self.get_object()
	    if self.request.user==post.author:
	     	return True
	    return False	





def index(request):
	fore=Products.objects.all()
	feed=feeds.objects.all()




	context={
	  'fore':fore,
	  'feed':feed
	}




	return render(request, 'index.html',context)
def  about(request):
	return render(request, 'about.html')
def  product(request):
	form =productForm(request.POST)

	if  form.is_valid():
		form.save()
		form =productForm()

	context={
	  'form':form
	}

	return render(request, 'product.html',context)
 
def  contact(request):
	feed=feeds.objects.all()

	

	return render(request, "contact.html",{'feed':feed})