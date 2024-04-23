from django.conf import settings
from django.shortcuts import render, HttpResponse

# Create your views here.


def HomeStaticHtmlView(req, page):
    return render(req, r'NCKH-2024/eco/{0}'.format(page))


def HomeView(req):
    return render(req, 'NCKH-2024/django-templates/index.html')


def ApplicationInfoView(req):
    return HttpResponse(",".join(settings.CSRF_TRUSTED_ORIGINS))
