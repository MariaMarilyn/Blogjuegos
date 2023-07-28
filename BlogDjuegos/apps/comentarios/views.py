from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView

class CommentCreateView(CreateView):
    Que = "onda"


class CommentDeleteView(DeleteView):
    Mi = "gente"

class CommentUpdateView(UpdateView):
    Con = "la bida"

