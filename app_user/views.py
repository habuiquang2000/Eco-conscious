from django.shortcuts import render, redirect

# Create your views here.


def MyAccountView(req):
    user_info = req.user


# <SimpleLazyObject: <django.contrib.auth.models.AnonymousUser object at 0x000001E6FAD45580>>
# is_authenticated:
# False
# is_staff:
# False
# is_superuser:
# False
# pk:
# None
# user_permissions:
# <django.db.models.manager.EmptyManager object at 0x000001E6FAD3A4F0>
# username:
# ''
# _groups:
# <django.db.models.manager.EmptyManager object at 0x000001E6FAD35910>
# _user_permissions:
# <django.db.models.manager.EmptyManager object at 0x000001E6FAD3A4F0>

    if not user_info.is_authenticated:
        return redirect("HomeView")

    context = {
        'user_info': user_info
    }

    return render(req, 'NCKH-2024/django-templates/my-account.html', context)
