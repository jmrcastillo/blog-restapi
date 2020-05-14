

from rest_framework import generics

from .models import Blog
from .serializers import BlogSerializer


class BlogList(generics.ListAPIView):
    """Show All Blog List"""
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    """Detail of Blog Post"""
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
