# from core.models import Item
from django.shortcuts import render
# from django.views.generic import  ListView,DetailView
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    # CreateView,
    # UpdateView,
    # DeleteView
)
from django.core.mail import send_mail
from .forms import EmailPostForm

from core.models import  Comment
from .forms import EmailPostForm, CommentForm , SearchForm
from taggit.models import Tag
from django.db.models import Count
from django.contrib.postgres.search import SearchVector  #Building a search view veter



def  post_search(request):
    form= SearchForm()
    query=None
    results=[]
    if 'query' in request.GET:
        form=SearchForm(request.GET)
        if form.is_valid():
            query=form.cleaned_data['query']
            results=Post.published.annotate(
                search =SearchVector('title','body'),
                ).filter(search=query)
    return render(request,'search.html',{
        'form':form,
        'query':query,
        'results':results
    })            









def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False
    if request.method == 'POST':

        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
        # ... send email
        post_url = request.build_absolute_uri(
            post.get_absolute_url())
        subject = f"{cd['name']} recommends you read "f"{post.title}"
        message = f"Read {post.title} at {post_url}\n\n" f"{cd['name']}\'s comments: {cd['comments']}"
        send_mail(subject, message, 'rp9545416@gmail.com',[cd['to']])
        sent = True     

    else:
        form=EmailPostForm()
        return render(request, 'share.html', {'post': post,
                                            'form': form,
                                            'sent': sent})


class PostDetailView(DetailView):
    model = Post
class PostListView(ListView):
    queryset=Post.published.all()
    context_object_name='posts'
    paginate_by=2
    template_name='list.html'


def post_list(request , tag_slug=None):
    object_list=Post.published.all()
    tag=None

    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        object_list=object_list.filter(tags__in=[tag])
    paginator=Paginator(object_list, 2)  # 3 posts in each page
    page=request.GET.get('page')
    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts=paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts=paginator.page(paginator.num_pages)

    return render(request,
                  'list.html',
                  {'posts': posts,
                   'page': page,
                   'tag': tag})


def post_detail(request, year, month, day, post):
    post=get_object_or_404(Post, slug = post,
                             status = 'published',
                             publish__year = year,
                             publish__month = month,
                             publish__day = day)
  
    comments=post.comments.filter(active=True)
    new_comment=None
    
    # List of similar posts
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts=similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:4]

    if request.method== 'POST':
        #comment aas passed
        comment_form=CommentForm(data=request.POST)
        if  comment_form.is_valid():
            #new coment object 
            new_comment=comment_form.save(comment=False)

            new_comment.post
            new_comment.save()
        else:
            comment_form=CommentForm()    

     
    return render(request,
                  'blog/post_detail.html',
                  {'post': post,
                  'comments': comments,
                  'new_comment': new_comment,
                  'comment_form': comment_form,
                  'similar_posts': similar_posts})
                  

def home(request):
   
    return render(request, 'base.html')


def about(request):
    return render(request, 'about.html')

# def product(request):
#     return render (request ,'product.html' )

# class ItemdDetailView(DetailView):
#     model=Item
#     template_name="product.html"


# def checkout(request):
#     return render (request ,'checkout.html')
