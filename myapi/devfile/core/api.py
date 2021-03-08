from django.http.response import HttpResponse
from requests_oauthlib import OAuth2Session


import json

import requests_oauthlib
from django.HttpResponse import request
import requests
from django.shortcuts import  redirect, session,

#  payload={'key1':'search?q=','key2':['form','&api_key=306cf1684a42e4be5ec0a1c60362c2ef']}
# client_id = '&api_key=306cf1684a42e4be5ec0a1c60362c2ef'
client_id = "<your client key>"
client_secret = "<your client secret>"
authorization_base_url = 'https://github.com/login/oauth/authorize'
token_url = 'https://github.com/login/oauth/access_token'



@app.route("/login")
def login():
    github = OAuth2Session(client_id)
    authorization_url, state = github.authorization_url(authorization_base_url)

    # State is used to prevent CSRF, keep this for later.
    session['oauth_state'] = state
    return redirect(authorization_url)



@app.route("/callback")
def callback():
    github = OAuth2Session(client_id, state=session['oauth_state'])
    token = github.fetch_token(token_url, client_secret=client_secret,
                               authorization_response=request.url)

    return json(github.get('https://api.github.com/user').json())    