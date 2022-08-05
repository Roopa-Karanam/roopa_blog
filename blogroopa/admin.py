# blogroopa/admin.py

from django.contrib import admin
from . import models
from blogroopa.models import Comments
class CommentInline(admin.TabularInline):
    model = Comments
    fields = ('name', 'email', 'text', 'approved')
    readonly_fields = ('name', 'email', 'text')

# Register the `Post` model
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'created',
        'updated',
    )
    
    
    search_fields = (
        'title',
        'author__username',
        'author__first_name',
        'author__last_name',
    )
    list_filter = (
        'status',
        'topics',
    )
    inlines = [
        CommentInline,
    ]
    prepopulated_fields = {'slug': ('title',)}
    
@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )
    prepopulated_fields = {'slug': ('name',)}
    
@admin.register(models.Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
    )
    search_fields = (
        'text',
        'name',
        )
    list_filter = (
        'name',
        'approved',
    )
    
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'last_name',
        'first_name',
        'submitted'
    )
    # Make these fields read-only in the admin
    readonly_fields = (
        'first_name',
        'last_name',
        'email',
        'message',
        'submitted'
    )
@admin.register(models.Contest)
class ContestAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'photo'
    )
    list_filter = (
        'name',
        'email',
    )
    search_fields = (
        'name',
        'email',
    )
    # Make these fields read-only in the admin
    readonly_fields = (
        'name',
        'email',
        'photo',
        'submitted'
    )

    
    
    



    
admin.site.register(models.Post, PostAdmin)

