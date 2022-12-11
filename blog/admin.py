from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment, Contact


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin): 

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name', 'email_address', 'body')
    search_fields = ('first_name', 'last_name', 'email_address', 'body')

    def Contact(self, request, queryset):
        queryset.update(approved=True)