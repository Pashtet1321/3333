from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    model = Post
    template_name = 'all_news.html'
    context_object_name = 'newst'


class PostDetail(DetailView):
    model = Post
    template_name = 'all_news.html'
    context_object_name = 'news'
