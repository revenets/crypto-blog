from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import *


class BlogListView(ListView):
    model = News
    template_name = "blog/blog.html"
    context_object_name = "all_news"


class NewsDetailView(DetailView):
    model = News
    context_object_name = "news"


