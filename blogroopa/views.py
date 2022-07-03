from django.shortcuts import render
from . import models
from django.db.models import Count

# Create your views here.

def home(request):
    """
    The Blog homepage
    """
    #return render(request, 'blogroopa/home.html')
    #return render(request, 'blogroopa/home.html', {'message': 'Hello world!'})
    latest_posts = models.Post.objects.filter(status=models.Post.PUBLISHED).order_by('-published')[:3]
    topics=models.Topic.objects.annotate(Count('blogroopa_posts')).order_by('-blogroopa_posts__count')[:10]
    # Add as context variable "latest_posts"
    context = {'topics': topics, 'latest_posts': latest_posts}
    return render(request, 'blogroopa/home.html', context)
    