from django.shortcuts import render

# Create your views here.


def AboutView(req):
    # query = Blog.objects

    # context = {
    #     'blogs': query.all()
    # }

    # return render(req, 'NCKH-2024/django-templates/blog-details.html', context)
    return render(req, 'NCKH-2024/django-templates/about.html')


def ComingSoonView(req):
    # query = Blog.objects

    # context = {
    #     'blogs': query.all()
    # }

    # return render(req, 'NCKH-2024/django-templates/blog.html', context)
    return render(req, 'NCKH-2024/django-templates/coming-soon.html')


def ContactOneView(req):
    # query = Blog.objects

    # context = {
    #     'blogs': query.all()
    # }

    # return render(req, 'NCKH-2024/django-templates/blog-three-col.html', context)
    return render(req, 'NCKH-2024/django-templates/contact-one.html')


def EventDetailsView(req):
    # query = Blog.objects

    # context = {
    #     'blogs': query.all()
    # }

    # return render(req, 'NCKH-2024/django-templates/blog-details.html', context)
    return render(req, 'NCKH-2024/django-templates/event-details.html')


def EventsListView(req):
    # query = Blog.objects

    # context = {
    #     'blogs': query.all()
    # }

    # return render(req, 'NCKH-2024/django-templates/blog.html', context)
    return render(req, 'NCKH-2024/django-templates/events-list.html')


def ProjectsDetailsView(req):
    # query = Blog.objects

    # context = {
    #     'blogs': query.all()
    # }

    # return render(req, 'NCKH-2024/django-templates/blog-three-col.html', context)
    return render(req, 'NCKH-2024/django-templates/projects-details.html')


def ProjectsListView(req):
    # query = Blog.objects

    # context = {
    #     'blogs': query.all()
    # }

    # return render(req, 'NCKH-2024/django-templates/blog-details.html', context)
    return render(req, 'NCKH-2024/django-templates/projects-list.html')


def TeamView(req):
    # query = Blog.objects

    # context = {
    #     'blogs': query.all()
    # }

    # return render(req, 'NCKH-2024/django-templates/blog.html', context)
    return render(req, 'NCKH-2024/django-templates/team.html')


def TestimonialsView(req):
    # query = Blog.objects

    # context = {
    #     'blogs': query.all()
    # }

    # return render(req, 'NCKH-2024/django-templates/blog-three-col.html', context)
    return render(req, 'NCKH-2024/django-templates/testimonials.html')
