from django.shortcuts import render

# Create your views here.
from urllib.parse import urlparse
import datetime
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import get_user_model
from .models import OAuthUser
from django.contrib.auth import login
from django.shortcuts import get_object_or_404
from django.views.generic import FormView, RedirectView
from oauth.forms import RequireEmailForm
from django.urls import reverse
from django.db import transaction
from webdev.utils import send_email, get_md5, save_user_avatar
from webdev.utils import get_current_site
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseForbidden
from .oauthmanager import get_manager_by_type, OAuthAccessTokenException
from webdev.blog_signals import oauth_user_login_signal

import logging

logger = logging.getLogger(__name__)


def get_redirecturl(request):
    nexturl = request.GET.get('next_url', None)
    if not nexturl or nexturl == '/login/' or nexturl == '/login':
        nexturl = '/'
        return nexturl
    p = urlparse(nexturl)
    if p.netloc:
        site = get_current_site().domain
        if not p.netloc.replace('www.', '') == site.replace('www.', ''):
            logger.info('illegalurl:' + nexturl)
            return "/"
    return nexturl


def oauthlogin(request):
    type = request.GET.get('type', None)
    if not type:
        return HttpResponseRedirect('/')
    manager = get_manager_by_type(type)
    if not manager:
        return HttpResponseRedirect('/')
    nexturl = get_redirecturl(request)
    authorizeurl = manager.get_authorization_url(nexturl)
    return HttpResponseRedirect(authorizeurl)


def authorize(request):
    type = request.GET.get('type', None)
    if not type:
        return HttpResponseRedirect('/')
    manager = get_manager_by_type(type)
    if not manager:
        return HttpResponseRedirect('/')
    code = request.GET.get('code', None)
    try:
        rsp = manager.get_access_token_by_code(code)
    except OAuthAccessTokenException as e:
        logger.warning("OAuthAccessTokenException:" + str(e))
        return HttpResponseRedirect('/')
    except Exception as e:
        logger.error(e)
        rsp = None
    nexturl = get_redirecturl(request)
    if not rsp:
        return HttpResponseRedirect(manager.get_authorization_url(nexturl))
    user = manager.get_oauth_userinfo()
    if user:
        if not user.nikename or not user.nikename.strip():
            import datetime
            user.nikename = "djangoblog" + datetime.datetime.now().strftime('%y%m%d%I%M%S')
        try:
            temp = OAuthUser.objects.get(type=type, openid=user.openid)
            temp.picture = user.picture
            temp.matedata = user.matedata
            temp.nikename = user.nikename
            user = temp
        except ObjectDoesNotExist:
            pass
        # facebook的token过长
        if type == 'facebook':
            user.token = ''
        if user.email:
            with transaction.atomic():
                author = None
                try:
                    author = get_user_model().objects.get(id=user.author_id)
                except ObjectDoesNotExist:
                    pass
                if not author:
                    result = get_user_model().objects.get_or_create(email=user.email)
                    author = result[0]
                    if result[1]:
                        try:
                            get_user_model().objects.get(username=user.nikename)
                        except ObjectDoesNotExist:
                            author.username = user.nikename
                        else:
                            author.username = "djangoblog" + datetime.datetime.now().strftime('%y%m%d%I%M%S')
                        author.source = 'authorize'
                        author.save()

                user.author = author
                user.save()

                oauth_user_login_signal.send(
                    sender=authorize.__class__, id=user.id)
                login(request, author)
                return HttpResponseRedirect(nexturl)
        else:
            user.save()
            url = reverse('oauth:require_email', kwargs={
                'oauthid': user.id
            })

            return HttpResponseRedirect(url)
    else:
        return HttpResponseRedirect(nexturl)


def emailconfirm(request, id, sign):
    if not sign:
        return HttpResponseForbidden()
    if not get_md5(
            settings.SECRET_KEY +
            str(id) +
            settings.SECRET_KEY).upper() == sign.upper():
        return HttpResponseForbidden()
    oauthuser = get_object_or_404(OAuthUser, pk=id)
    with transaction.atomic():
        if oauthuser.author:
            author = get_user_model().objects.get(pk=oauthuser.author_id)
        else:
            result = get_user_model().objects.get_or_create(email=oauthuser.email)
            author = result[0]
            if result[1]:
                author.source = 'emailconfirm'
                author.username = oauthuser.nikename.strip() if oauthuser.nikename.strip(
                ) else "djangoblog" + datetime.datetime.now().strftime('%y%m%d%I%M%S')
                author.save()
        oauthuser.author = author
        oauthuser.save()
    oauth_user_login_signal.send(
        sender=emailconfirm.__class__,
        id=oauthuser.id)
    login(request, author)

    site = get_current_site().domain
    content = '''
    p>Congratulations, you have successfully bound your mailbox, 
    you can use {type} to log in to this website directly without a
     password. Welcome to continue to pay attention to this website,
      the address is</p> 
                <a href="{url}" rel="bookmark">{url}</a> 
    '''.format(type=oauthuser.type, url='http://' + site)

    send_email(emailto=[oauthuser.email, ], title='Congratulations on your successful binding!!', content=content)
    url = reverse('oauth:bindsuccess', kwargs={
        'oauthid': id
    })
    url = url + '?type=success'
    return HttpResponseRedirect(url)


class RequireEmailView(FormView):
    form_class = RequireEmailForm
    template_name = 'oauth/require_email.html'

    def get(self, request, *args, **kwargs):
        oauthid = self.kwargs['oauthid']
        oauthuser = get_object_or_404(OAuthUser, pk=oauthid)
        if oauthuser.email:
            pass
            # return HttpResponseRedirect('/')

        return super(RequireEmailView, self).get(request, *args, **kwargs)

    def get_initial(self):
        oauthid = self.kwargs['oauthid']
        return {
            'email': '',
            'oauthid': oauthid
        }

    def get_context_data(self, **kwargs):
        oauthid = self.kwargs['oauthid']
        oauthuser = get_object_or_404(OAuthUser, pk=oauthid)
        if oauthuser.picture:
            kwargs['picture'] = oauthuser.picture
        return super(RequireEmailView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        email = form.cleaned_data['email']
        oauthid = form.cleaned_data['oauthid']
        oauthuser = get_object_or_404(OAuthUser, pk=oauthid)
        oauthuser.email = email
        oauthuser.save()
        sign = get_md5(settings.SECRET_KEY +
                       str(oauthuser.id) + settings.SECRET_KEY)
        site = get_current_site().domain
        if settings.DEBUG:
            site = '127.0.0.1:8000'
        path = reverse('oauth:email_confirm', kwargs={
            'id': oauthid,
            'sign': sign
        })
        url = "http://{site}{path}".format(site=site, path=path)

        content =  """ 
<p>Please click the link below to bind your email</p> 
                <a href="{url}" rel="bookmark">{url}</a> 
 Thank you again! 
                <br /> 
If the above link cannot be opened, please copy this link to your browser. 
                {url} 
                """ .format(url=url)
        send_email(emailto=[email, ], title='Bind your email', content=content)
        url = reverse('oauth:bindsuccess', kwargs={
            'oauthid': oauthid
        })
        url = url + '?type=email'
        return HttpResponseRedirect(url)


def bindsuccess(request, oauthid):
    type = request.GET.get('type', None)
    oauthuser = get_object_or_404(OAuthUser, pk=oauthid)
    if type == 'email':
        title = 'Binding successful' 
        content = "Congratulations, the binding is only one step away, please log in to your mailbox to check the email to complete the binding, thank you."
    else:
        title =  'Binding successful'
        content = "Congratulations on your successful binding. You can use {type} to log in to this site directly without a password in the future. Thank you for your interest in this site.".format(
            type=oauthuser.type)
    return render(request, 'oauth/bindsuccess.html', {
        'title': title,
        'content': content
    })