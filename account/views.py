import json

from django.shortcuts import render
from django.template.context import RequestContext
import urllib.request
import ssl

from social.apps.django_app.default.models import UserSocialAuth


def home(request):
    return render(
        request,
        template_name='home.html',
        context={
            'request': request,
            'user': request.user,
        }
    )
