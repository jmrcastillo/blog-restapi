from rest_framework import generics  # type: ignore
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Blog
from .serializers import BlogSerializer, UserSerializer
from django.contrib.auth import authenticate

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class LoginView(APIView):
    permission_classes = ()

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username,
                            password=password
                            )
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"},
                            status=status.HTTP_400_BAD_REQUEST)


class BlogList(generics.ListAPIView):
    """Show All Blog List"""

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    """Detail of Blog Post"""

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
