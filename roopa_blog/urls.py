"""roopa_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
#from . import views   # Import the views module
from blogroopa import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #path('', views.index),  # Add our index view to the URL patterns
    path('admin/', admin.site.urls),    

    path('', views.HomeView.as_view(), name='home'),  # Set root to home view
    path('about/', views.AboutView.as_view(), name='about'),
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path(
        'posts/<int:year>/<int:month>/<int:day>/<slug:slug>/',
        views.PostDetailView.as_view(),
        name='post-detail',
    ),
    path(
        'posts/<int:pk>/',
        views.PostDetailView.as_view(),
        name='post-detail',
    ),
    
    path(
        'topics/<slug:slug>/',
        views.TopicDetailView.as_view(),
        name='topic-detail',
    ),
    path('topics/', views.TopicListView.as_view(), name='topic-list'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('contest/', views.ContestFormView.as_view(), name='contest'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api/', include('api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
