from django.contrib import admin

from .models import Blog, Comment

# Register your models here.


class LessonInline(admin.StackedInline):
    model = Comment


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'created_at',
    )
    inlines = [LessonInline]
