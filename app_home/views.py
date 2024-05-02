from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, HttpResponse
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic import ListView, DetailView, View


# Create your views here.


# class HomeView(ListView):
#     model = Item
#     paginate_by = 10
#     template_name = "home.html"


# class OrderSummaryView(LoginRequiredMixin, View):
#     def get(self, *args, **kwargs):
#             order = Order.objects.get(user=self.request.user, ordered=False)
#             context = {
#                 'object': order
#             }
#             return render(self.request, 'order_summary.html', context)


# class ItemDetailView(DetailView):
#     model = Item
#     template_name = "product.html"


def HomeStaticHtmlView(req, page):
    return render(req, r'NCKH-2024/eco/{0}'.format(page))


def HomeView(req):
    # messages.info(req, "You do not have an active order")
    # messages.warning(req, "You do not have an active order")
    # messages.success(req, "Successfully added coupon")

    return render(req, 'NCKH-2024/django-templates/index.html')


def ApplicationInfoView(req):
    return HttpResponse(",".join(settings.CSRF_TRUSTED_ORIGINS))
