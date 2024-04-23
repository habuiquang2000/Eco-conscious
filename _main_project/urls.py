"""
URL configuration for _main_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls import handler400, handler500

from cicd_hook.views import TypeformSubmissions

from app_blog.views import (
    BlogDetailsView,
    BlogView,
    BlogThreeColView
)
from app_gallery.views import (
    GalleryFullView,
    GalleryGridView,
    GalleryMasonryView
)
from app_handle.views import (
    Page404View
)
from app_home.views import (
    ApplicationInfoView,
    HomeStaticHtmlView,
    HomeView
)
from app_info.views import (
    AboutView,
    ComingSoonView,
    ContactOneView,
    EventDetailsView,
    EventsListView,
    ProjectsDetailsView,
    ProjectsListView,
    TeamView,
    TestimonialsView,
)
from app_user.views import (
    MyAccountView
)

webhooks = [
    re_path(
        r'^typeform/submission',
        TypeformSubmissions.as_view(),
        name="TypeformSubmissions",
    )
]

urlpatterns = [
    path('admin', admin.site.urls),

    path('ckeditor/', include('ckeditor_uploader.urls')),
    re_path(r'^api-auth', include('rest_framework.urls')),

    re_path(r'^webhooks', include(
        (webhooks, "webhooks"), namespace="webhooks"),),
]

urlpatterns += [
    re_path(r'^about.html', AboutView, name='AboutView'),
    re_path(r'^blog-details.html', BlogDetailsView.as_view(),
            name='BlogDetailsView'),
    re_path(
        r'^blog-three-col.html',
        BlogThreeColView.as_view(),
        name='BlogThreeColView'
    ),
    re_path(r'^blog.html', BlogView.as_view(), name='BlogView'),
    re_path(r'^coming-soon.html', ComingSoonView, name='ComingSoonView'),
    re_path(r'^contact-one.html', ContactOneView, name='ContactOneView'),
    re_path(r'^event-details.html', EventDetailsView, name='EventDetailsView'),
    re_path(r'^events-list.html', EventsListView, name='EventsListView'),
    re_path(r'^gallery-full.html', GalleryFullView, name='GalleryFullView'),
    re_path(r'^gallery-grid.html', GalleryGridView, name='GalleryGridView'),
    re_path(r'^gallery-masonry.html', GalleryMasonryView,
            name='GalleryMasonryView'),
    re_path(r'^index.html', HomeView, name='IndexView'),
    re_path(r'^my-account.html', MyAccountView, name='MyAccountView'),
    re_path(r'^page-404.html', Page404View, name='Page404View'),
    re_path(
        r'^projects-details.html',
        ProjectsDetailsView,
        name='ProjectsDetailsView'
    ),
    re_path(r'^projects-list.html', ProjectsListView, name='ProjectsListView'),
    re_path(r'^team.html', TeamView, name='TeamView'),
    re_path(r'^testimonials.html', TestimonialsView, name='TestimonialsView'),

    re_path(r'^application', ApplicationInfoView, name='ApplicationInfoView'),
    path('<str:page>', HomeStaticHtmlView, name='HomeStaticHtmlView'),
    path('', HomeView, name='HomeView'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'app_handle.views.Page404Handle'
# handler500 = 'app_handle.views.handler500'

# handler404 = 'app_handle.views.handler404'
# handler500 = 'app_handle.views.handler500'
