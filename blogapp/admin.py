from django.contrib import admin

from .models import Blog, Comment
# Register your models here.

# admin.site.register(Blog)

# class Blogsadmin(admin.ModelAdmin):
#     fields = ['title','body', 'pub_date']


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 2


class Blogsadmin(admin.ModelAdmin):
    fieldsets = [
        ('제목', {'fields': ['title']}),
        ('내용', {'fields': ['body', 'pub_date']}),
    ]
    inlines = [CommentInline]
    list_filter=['pub_date']
    search_fields = ['title']

    
class Commentadmin(admin.ModelAdmin):
    list_display = ['id', 'blog_id', 'blog' , 'comment_text']


admin.site.register(Blog, Blogsadmin)
admin.site.register(Comment, Commentadmin)
