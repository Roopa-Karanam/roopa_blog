from django.views import View
from django.shortcuts import render
from . import models
from django.db.models import Count
from django.views.generic.base import TemplateView

# Create your views here.
    
class HomeView( TemplateView):
    template_name = 'blogroopa/home.html'

    def get_context_data(self, **kwargs):
        # Get the parent context
        context = super().get_context_data(**kwargs)
        latest_posts = models.Post.objects.filter(status=models.Post.PUBLISHED).order_by('-published')[:3]
        context.update({'latest_posts': latest_posts})

        return context
class AboutView(TemplateView):
    template_name = 'blog/about.html'
    
def terms_and_conditions(request):
   return render(request, 'blog/terms_and_conditions.html')    