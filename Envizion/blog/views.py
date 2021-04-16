from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
posts = [
    {
        'author': 'haris',
        'title' : 'post1',
        'content': 'Hello, this is my first post',
        'postDate': '21-03-2019'
    }
]
def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)




