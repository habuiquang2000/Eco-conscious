from django.shortcuts import render

# Create your views here.


def GalleryFullView(req):
    # query = Blog.objects

    # context = {
    #     'blogs': query.all()
    # }

    # return render(req, 'NCKH-2024/django-templates/blog-details.html', context)
    return render(req, 'NCKH-2024/django-templates/gallery-full.html')


def GalleryGridView(req):
    # query = Blog.objects

    # context = {
    #     'blogs': query.all()
    # }

    # return render(req, 'NCKH-2024/django-templates/blog.html', context)
    return render(req, 'NCKH-2024/django-templates/gallery-grid.html')


def GalleryMasonryView(req):
    # query = Blog.objects

    # context = {
    #     'blogs': query.all()
    # }

    # return render(req, 'NCKH-2024/django-templates/blog-three-col.html', context)
    return render(req, 'NCKH-2024/django-templates/gallery-masonry.html')
