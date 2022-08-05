
from django.shortcuts import render
from . import models
#from django.db.models import Count
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import DetailView, CreateView, FormView, ListView

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
    template_name = 'blogroopa/about.html'
    
def terms_and_conditions(request):
   return render(request, 'blogroopa/terms_and_conditions.html')

class PostListView(ListView):
    model = models.Post
    context_object_name = 'posts'
    queryset = models.Post.objects.filter(status=models.Post.PUBLISHED).order_by('-published')  # Customized queryset

class TopicListView(ListView):
    model = models.Topic
    context_object_name = 'topics'
    queryset = models.Topic.objects.all()  # Customized queryset   
class ContestFormView(CreateView):
    model=models.Contest
    success_url = reverse_lazy('home')
    fields = [
        'name',
        'email',
        'photo',
    ]
    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Thank you for the submission.'
        )
        return super().form_valid(form)


    
class PostDetailView(DetailView):
    model = models.Post

    def get_queryset(self):
        queryset = super().get_queryset()

        # If this is a `pk` lookup, use default queryset
        if 'pk' in self.kwargs:
            return queryset

        # Otherwise, filter on the published date
        return queryset.filter(
            published__year=self.kwargs['year'],
            published__month=self.kwargs['month'],
            published__day=self.kwargs['day'],
        )

class TopicDetailView(DetailView):
    model = models.Topic
    def get_queryset(self):
        return super().get_queryset().all()
class ContactFormView(CreateView):
    model = models.Contact
    success_url = reverse_lazy('home')
    fields = [
        'first_name',
        'last_name',
        'email',
        'message',
    ]

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Thank you! Your message has been sent.'
        )
        return super().form_valid(form)
    