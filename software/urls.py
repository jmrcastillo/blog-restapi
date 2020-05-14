

from django.urls import path


from . import apiviews


urlpatterns = [
    path('', apiviews.BlogList.as_view()),
    path('<int:pk>/', apiviews.BlogDetail.as_view()),
]
