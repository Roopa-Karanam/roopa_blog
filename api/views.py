from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import F
from django.http import HttpResponse


from rest_framework import generics


from blogroopa.models import Post,Comment
from . import serializers

from blogroopa import models



# Create your views here.

@api_view(['GET'])
def index(request):
    return Response()


class PostListView(generics.ListAPIView):
    """
    Returns a list of published posts
    """
    serializer_class = serializers.PostListSerializer
    
    queryset = Post.objects.filter(status=models.Post.PUBLISHED)


class PostDetailView(generics.RetrieveAPIView):
    """
    Returns post details
    """
    serializer_class = serializers.PostDetailSerializer
    queryset = Post.objects.filter(status=models.Post.PUBLISHED)
class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = serializers.CommentSerializer
    queryset = Comment.objects.all()

    def get_queryset(self):
        post_id = self.request.query_params.get('post')
        queryset = super().get_queryset()
        if post_id and post_id.isdecimal():
            queryset = queryset.filter(post_id=int(post_id))
        return queryset.order_by('-created')
def likes(request,pk):
    qset= Comment.objects.get(pk=pk)
    qset.likes = F('likes') + 1
    qset.save()
    return HttpResponse(qset.likes)
 

def dislikes(request,pk):
    print("likes")
    qset= Comment.objects.get(pk=pk)
    qset.dislikes = F('dislikes') + 1
    qset.save()
    return HttpResponse(qset.dislikes)
    
    