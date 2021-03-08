from django.shortcuts import render
from .forms import  SearchForm
import requests
def base(request):
    # import requests

    # # url = "https://gplaystore.p.rapidapi.com/newFreeApps"
    # url="https://libraries.io/api/"
    # querystring = {"platforms":"NPM/base62"}

    # headers = {'x-rapidapi-key': "?api_key=306cf1684a42e4be5ec0a1c60362c2ef'" }

    # response = requests.request("GET", url, headers=headers, params=querystring)

    # print(response.text)

   return render(request, 'base.html'
    )

def home(request):
 


#  Platforms=(' https://libraries.io/api/platforms?api_key=306cf1684a42e4be5ec0a1c60362c2ef')
#  Project=('https://libraries.io/api/NPM/base62?api_key=306cf1684a42e4be5ec0a1c60362c2ef')

    # url=requests()
    # url='https://libraries.io/api/:platform/:name/dependent_repositories?api_key=306cf1684a42e4be5ec0a1c60362c2ef'
    # url=requests.get('https://libraries.io/api/github/librariesio/repositories?api_key=306cf1684a42e4be5ec0a1c60362c2ef')
    url=requests.get('https://libraries.io/api/platforms?api_key=306cf1684a42e4be5ec0a1c60362c2ef')
    
    form=url.json()
    return render(request, 'index.html',{
        'form':form
    }
    )


def Search(request):
#     form= SearchForm()
#     query=None
#     results=[]

#     # if 'query' in requests.GET:
#     #   form=SearchForm(request.GET)
#     #   if form.is_valid():
#     #       query=form.cleaned_data['query']
#     #       results=Post.published.annotate(
#     #           search =SearchVector('title','body'),
#     #           ).filter(search=query)
    r=requests.get('https://libraries.io/api/search?q=&api_key=306cf1684a42e4be5ec0a1c60362c2ef')   

    dr=r.json()
    return render(request, 'Search.html',{
        'search':dr
    }
    )



# def  post_search(request):
#     form= SearchForm()
    
#     payload={'key1':'search?q=','key2':['form','&api_key=306cf1684a42e4be5ec0a1c60362c2ef']}

#     url=requests.get=('https://libraries.io/api/get',params=payload) 
#     # results=[]
#     # if 'query' in request.GET:
#     #     form=SearchForm(
#         # if form.is_valid():
#         #     query=form.cleaned_data['query']
#         #     results=Post.published.annotate(
#         #         search =SearchVector('title','body'),
#         #         ).filter(search=query)
#     return render(request,'search.html',{
#         'url':url,
#         # 'query':query,
#         # 'results':results
#     })            


