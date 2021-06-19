from django.shortcuts import render
from .models import Posts

def index(request):
    data = Posts.objects.all()
    context = {'allposts':data}
    return render(request, 'posts/index.html', context)