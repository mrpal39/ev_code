from django.shortcuts import render
from urllib.request import urlopen
from django.shortcuts import render
from django.views import View
import requests

# class apiurl(View):

def apiurl(request):
    url =requests('https://api.github.com/')
    
    data=url.requests.json()
    context ={
        'data':data
    }
    
    return render(request,'index.html', context)


