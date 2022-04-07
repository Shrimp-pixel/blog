from django.shortcuts import render
from .models import Post


# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blogapp/home.html', context=context)


def about(request):
    return render(request, 'blogapp/about.html',context={'title': 'about'})
