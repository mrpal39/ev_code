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

import requests

def  post_api(request):
    form= SearchForm()
    query=None
    results=[]

    api_key='306cf1684a42e4be5ec0a1c60362c2ef'
    url=("https://libraries.io/api/search?q={}&api_key={}".format(form,api_key))

    response = requests.get(url)
    response_dict = response.json()
    # if 'query' in request.GET:
    #     response_dict=SearchForm(request.GET)
    #     if response_dict.is_valid():
    #         query=form.cleaned_data['query']
    #         results=Post.published.annotate(
    #             search =SearchVector('title','body'),
    #             ).filter(search=query)
    return render(request,'search.html',{
        'form':response_dict,
        # 'query':query,
        # 'results':results
    })            



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
    return render(request,'api.html',{
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
    pk_url_kwarg = 'article_id'
    context_object_name = "article"

    def get_object(self, queryset=None):
     obj = super(PostDetailView, self).get_object()
     obj.viewed()
     self.object = obj
     return obj

    
    def get_context_data(self, **kwargs):
        articleid = int(self.kwargs[self.pk_url_kwarg])
        comment_form = CommentForm()
        user = self.request.user
        # 如果用户已经登录，则隐藏邮件和用户名输入框
        if user.is_authenticated and not user.is_anonymous and user.email and user.username:
            comment_form.fields.update({
                'email': forms.CharField(widget=forms.HiddenInput()),
                'name': forms.CharField(widget=forms.HiddenInput()),
            })
            comment_form.fields["email"].initial = user.email
            comment_form.fields["name"].initial = user.username

        article_comments = self.object.comment_list()

        kwargs['form'] = comment_form
        kwargs['article_comments'] = article_comments
        kwargs['comment_count'] = len(
            article_comments) if article_comments else 0

        kwargs['next_article'] = self.object.next_article
        kwargs['prev_article'] = self.object.prev_article

        return super(ArticleDetailView, self).get_context_data(**kwargs) 


class PostListView(ListView):

    queryset=Post.published.all()
    context_object_name='posts'
    paginate_by=2
    template_name='list.html'
    
    
    page_type = ''
    page_kwarg = 'page'

    def get_view_cache_key(self):
        return self.request.get['pages']

    @property
    def page_number(self):
        page_kwarg = self.page_kwarg
        page = self.kwargs.get(
            page_kwarg) or self.request.GET.get(page_kwarg) or 1
        return page

    def get_queryset_cache_key(self):
     
        raise NotImplementedError()

    def get_queryset_data(self):
        """
        子类重写.获取queryset的数据
        """
        raise NotImplementedError()

    # def get_queryset_from_cache(self, cache_key):
       
    #     value = cache.get(cache_key)
    #     if value:
    #         logger.info('get view cache.key:{key}'.format(key=cache_key))
    #         return value
    #     else:
    #         article_list = self.get_queryset_data()
    #         cache.set(cache_key, article_list)
    #         logger.info('set view cache.key:{key}'.format(key=cache_key))
    #         return article_list
     
    # def get_queryset(self):
       
    #     key = self.get_queryset_cache_key()
    #     value = self.get_queryset_from_cache(key)
    #     return value
    
    # def get_context_data(self, **kwargs):
    #     kwargs['linktype'] = self.link_type
    #     return super(PostListView, self).get_context_data(**kwargs)
    

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
