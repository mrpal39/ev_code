from django.http import response
from django.shortcuts import render
from .forms import  DocumentForm
import requests

from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def simple_upload(request):
    if request.method == 'POST':
        myfile = DocumentForm(request.POST, request.FILES)


        myfile = request.FILES['file']

        fs = FileSystemStorage()

        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        return render(request, 'imple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'simple_upload.html')

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })


def api(request):
   
   api_key ='306cf1684a42e4be5ec0a1c60362c2ef'
   name='npm'

   api_url="https://libraries.io/api/search?q={}&api_key={}".format(name ,api_key)
   response=requests.get(api_url)
   response_dict = response.json()

   return render(request, 'api.html',{'api': response_dict, }  
   
   
    )










   # return render(request,'search.html',{
#         'url':url,
#         # 'query':query,
#         # 'results':results
#     })   


