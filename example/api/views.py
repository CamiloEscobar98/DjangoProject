from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from example.models import Post
from example.api.serializers import PostSerializer

class PostApiViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()