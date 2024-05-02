from django.contrib import admin

from .models.blog import Blog, BlogComment
from .models.event import Event, EventComment
from .models.gallery import Gallery, GalleryComment

# Register your models here.


class BlogInline(admin.StackedInline):
    model = BlogComment


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'created_at',
    )
    inlines = [BlogInline]


class EventInline(admin.StackedInline):
    model = EventComment


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'created_at',
    )
    inlines = [EventInline]


class GalleryInline(admin.StackedInline):
    model = GalleryComment


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'created_at',
    )
    inlines = [GalleryInline]
