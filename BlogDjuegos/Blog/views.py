from django.shortcuts import render

def index(request):
    context = {
        }
    return render(request, r'blog/index.html', context)