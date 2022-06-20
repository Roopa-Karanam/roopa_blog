from django.contrib import admin

# Register your models here.
from . import models

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'created',
        'updated',
        'author',
    )
    search_fields = (
        'title',
        'author__username',
        'author__first_name',
        'author__last_name',
    )
    list_filter = (
        'status',
        'topics'
    )
    prepopulated_fields = {'slug': ('title',)}
    
@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )
    prepopulated_fields = {'slug': ('name',)}

# Register the `Post` model
admin.site.register(models.Post, PostAdmin)