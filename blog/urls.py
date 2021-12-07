from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.BlogListView.as_view(), name="blog"),
    path("news/<int:pk>", views.NewsDetailView.as_view(), name="news"),
]
