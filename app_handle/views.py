from django.shortcuts import render
from django.http import Http404
from django.urls import resolve

# Create your views here.


def Page404Handle(req, exception):
    try:
        tried = exception.args[0]["tried"]
    except (IndexError, TypeError, KeyError):
        tried = req.resolver_match.tried if req.resolver_match else None

    context = {
        "urlpatterns": tried,
        "reason": str(exception),
    }
    return render(req, 'NCKH-2024/django-templates/page-404.html', context)


def Page404View(req):

    return render(req, 'NCKH-2024/django-templates/page-404.html')


# from django.shortcuts import render
# from django.template import RequestContext


# def handler404(request, *args, **argv):
#     response = render('NCKH-2024/django-templates/page-404.html', {},
#                       context_instance=RequestContext(request))
#     response.status_code = 404
#     return response


# def handler500(request, *args, **argv):
#     response = render('NCKH-2024/django-templates/page-404.html', {},
#                       context_instance=RequestContext(request))
#     response.status_code = 500
#     return response
