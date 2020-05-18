from django.urls import path  # type: ignore


from . import apiviews


urlpatterns = [
    path("", apiviews.BlogList.as_view()),
    path("<int:pk>/", apiviews.BlogDetail.as_view()),
]
