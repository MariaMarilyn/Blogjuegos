from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView

def index(request):
    context = {
        }
    return render(request, r'comentarios/index.html', context)

class CommentCreateView(CreateView):
    Que = "onda"


class CommentDeleteView(DeleteView):
    Mi = "gente"

class CommentUpdateView(UpdateView):
    Con = "la bida"


