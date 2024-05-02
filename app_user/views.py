from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from django.contrib.auth import user_logged_in, authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
# @login_required
async def MyAccountView(req):
    user_info = req.user

    user = await req.auser()
    if user.is_authenticated:
        pass
        # Do something for authenticated users.
    else:
        pass
        # Do something for anonymous users.

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


# @login_required
class ChangePView(View):
    def get(self, req):
        if req.user.is_authenticated:
            pass
            # Do something for authenticated users.
        else:
            pass
            # Do something for anonymous users.

        """ CHANGE PASSWORD FORM """
        return render(req, 'NCKH-2024/django-templates/blog-details.html')

    def post(self, req):
        """ CHANGE PASSWORD """

        u = User.objects.get(username="john")
        u.set_password("new password")
        u.save()

        return redirect(req.path)
        # return redirect(reverse('BlogDetailsView') + '?id={}'.format(blog_id))


class LView(View):
    def get(self, req):
        """ LOGIN FORM """
        return render(req, 'NCKH-2024/django-templates/blog-details.html')

    def post(self, req):
        """ LOGIN AUTH """

        username = ('username', None)
        password = ('password', None)
        is_remember = ('is_remember', None)

        username = req.POST["username"]
        password = req.POST["password"]
        user = authenticate(req, username=username, password=password)
        if user is not None:
            login(req, user)
            # Redirect to a success page.
        else:
            pass
            # Return an 'invalid login' error message.

        user = authenticate(username="john", password="secret")
        if user is not None:
            pass
            # A backend authenticated the credentials
        else:
            pass
            # No backend authenticated the credentials

        msg = req.session.get('msg', False)
        if msg:
            del (req.session['msg'])

        return redirect(req.path)
        # return redirect(reverse('BlogDetailsView') + '?id={}'.format(blog_id))


class RView(View):
    def get(self, req):
        """ REGISTER FORM """
        return render(req, 'NCKH-2024/django-templates/blog-details.html', context)

    def post(self, req):
        """ REGISTER AUTH """

        name = ('name', None)
        email = ('email', None)
        username = ('username', None)
        password = ('password', None)
        repassword = ('repassword', None)
        is_policy = ('is_policy', None)
        user = User.objects.create_user(
            "john", "lennon@thebeatles.com", "johnpassword")
        user.save()

        return redirect(req.path)
        # return redirect(reverse('BlogDetailsView') + '?id={}'.format(blog_id))


@login_required(redirect_field_name="my_redirect_field", login_url="/accounts/login/")
class OView(View):
    def get(self, req):
        """ LOGOUT """
        return render(req, 'NCKH-2024/django-templates/blog-details.html', context)

    def post(self, req):
        """ LOGOUT AUTH """
        logout(req)
        return redirect(req.path)
        # return redirect(reverse('BlogDetailsView') + '?id={}'.format(blog_id))
