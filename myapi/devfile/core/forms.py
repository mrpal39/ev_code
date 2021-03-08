from django import forms


#Building a search view



class  SearchForm(forms.Form):
    query =forms.CharField()


class uploadForm(forms.ModelForm):
    images=forms.ImageField()



# # from .forms import EmailPostForm, CommentForm , SearchForm
# User Repositories='https://libraries.io/api/github/:login/repositories?api_key=306cf1684a42e4be5ec0a1c60362c2ef'
# user='             https://libraries.io/api/github/andrew?api_key=306cf1684a42e4be5ec0a1c60362c2ef'
# Repository='       https://libraries.io/api/github/:owner/:name?api_key=306cf1684a42e4be5ec0a1c60362c2ef'
#            ='      https://libraries.io/api/github/gruntjs/grunt/projects?api_key=306cf1684a42e4be5ec0a1c60362c2ef '
# ProjectSearch='    https://libraries.io/api/search?q=grunt&api_key=306cf1684a42e4be5ec0a1c60362c2ef'
# Platforms= ' GET   https://libraries.io/api/platforms?api_key=306cf1684a42e4be5ec0a1c60362c2ef '
#                    https://libraries.io/api/NPM/base62?api_key=306cf1684a42e4be5ec0a1c60362c2ef '

# ProjectDependen    https://libraries.io/api/:platform/:name/:version/dependencies?api_key=306cf1684a42e4be5ec0a1c60362c2ef'
#                  ' https://libraries.io/api/NPM/base62/2.0.1/dependencies?api_key=306cf1684a42e4be5ec0a1c60362c2ef '
# DependentReposito= https://libraries.io/api/NPM/base62/dependent_repositories?api_key=306cf1684a42e4be5ec0a1c60362c2ef '
# ProjectContributo= https://libraries.io/api/NPM/base62/contributors?api_key=306cf1684a42e4be5ec0a1c60362c2ef '
# ProjectSourceRank='https://libraries.io/api/NPM/base62/sourcerank?api_key=306cf1684a42e4be5ec0a1c60362c2ef'