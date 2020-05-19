from django.urls import path  # type: ignore


from . import apiviews
from .apiviews import UserCreate, LoginView
from rest_framework.authtoken import views


urlpatterns = [
    path("", apiviews.BlogList.as_view()),
    path("<int:pk>/", apiviews.BlogDetail.as_view()),
    path("users/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
    path("logins/", views.obtain_auth_token, name="logins"),
]
