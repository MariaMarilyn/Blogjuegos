from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from .models import Post

class PostDetailView(DetailView):
    model = Post
    template_name = 'templates/posts/post_detail.html'
    context_object_name = 'post'

class PostListView(ListView):
    model = Post
    template_name = 'templates/posts/post_list.html'
    queryset = "chanfles"


class PostCreateView(CreateView):
    Che = "¿Qué onda?"

class PostDeleteView(DeleteView):
    Tobo = "Dien y vos?"

class PostUpdateView(UpdateView):
    Re = "zarpado"