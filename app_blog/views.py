from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View
from django.urls import reverse
from django.core.paginator import Paginator

from .models import Blog, Comment
from .forms import CommentForm

# Create your views here.


class BlogDetailsView(View):
    def get(self, req):
        """ READ BLOG """
        search_params = req.GET.get
        id: str = search_params('id', '')
        blog_id: int = int(id) if id.isdigit() else 0

        query_blog = Blog.objects

        blog = query_blog.filter(id=blog_id).first()

        context = {}

        if blog is not None:
            comments = blog.comments.exclude(
                comment_to_reply__isnull=False
            ).all()

            context = {
                'form': CommentForm(),
                'blog': blog,
                'comments': comments,
            }

        return render(req, 'NCKH-2024/django-templates/blog-details.html', context)

    def post(self, req):
        """ CREATE COMMENT """
        search_params = req.GET.get
        body_data = req.POST.get

        blog_id: str = search_params('id', 0)

        comment_id = body_data('comment_id', None)
        fullname = body_data('fullname')
        avatar = req.FILES.get('avatar')
        content = body_data('content')

        blog = Blog.objects.filter(id=blog_id).first()

        if blog:
            query_comment = Comment(
                blog=blog,
                fullname=fullname,
                content=content,
            )
            if comment_id:
                comment = Comment.objects.filter(id=comment_id).first()
                query_comment.comment_to_reply = comment
            if avatar:
                query_comment.avatar = avatar
            query_comment.save()

        # return HttpResponseRedirect('BlogDetailsView', status=201)
        return redirect(reverse('BlogDetailsView') + '?id={}'.format(blog_id))


class BlogView(View):
    def get(self, req):
        search_params = req.GET.get

        page_search: str = search_params('page', '1')
        limit_search: str = search_params('limit', '5')

        page: int = int(page_search)if page_search.isdecimal() else 1
        limit: int = int(limit_search)if limit_search.isdecimal() else 5

        query_blog = Blog.objects
        blogs = query_blog.all()

        p = Paginator(blogs, limit)

        this_page = p.page(page)

        context = {
            'blogs': this_page.object_list,
            'count': p.count,
            'num_pages': p.num_pages,
            'next_page_number': this_page.has_next() and this_page.next_page_number(),
            'current_page_number': page,
            'previous_page_number': this_page.has_previous() and this_page.previous_page_number(),
            # The 1-based index of the first item on this page
            # 'start_index': this_page.start_index(),
            # The 1-based index of the last item on this page
            # 'end_index': this_page.end_index(),
            'has_next': this_page.has_next(),
            # False
            'has_previous': this_page.has_previous(),
            # True
            # 'has_other_pages': this_page.has_other_pages(),
            # True
            'page_range': p.page_range,
            'limit': limit,
        }

        return render(req, 'NCKH-2024/django-templates/blog.html', context)

    def post(self, req):
        """ CREATE COMMENT """
        search_params = req.GET.get
        body_data = req.POST.get

        blog_id: str = search_params('id', 0)

        fullname = body_data('fullname')
        avatar = req.FILES.get('avatar')
        content = body_data('content')

        blog = Blog.objects.filter(id=blog_id).first()

        if blog is not None:
            query_comment = Comment(
                blog=blog,
                fullname=fullname,
                content=content,
            )
            if avatar is not None:
                query_comment.avatar = avatar
            query_comment.save()

        # return HttpResponseRedirect('BlogDetailsView', status=201)
        return redirect('BlogThreeColView')


class BlogThreeColView(View):
    def get(self, req):
        """ READ FORM CREATE BLOG """
        return render(req, 'NCKH-2024/django-templates/blog-three-col.html')

    def post(self, req):
        """ CREATE BLOG """
        body_data = req.POST.get

        title = body_data('title', '')
        description = body_data('description', '')
        content = body_data('content', '')
        image = req.FILES.get('image')

        query_blog = Blog(
            title=title,
            description=description,
            content=content,
        )

        if image is not None:
            query_blog.image = image

        query_blog.save()

        return redirect('BlogThreeColView')
