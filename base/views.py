from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'base/home.html')


def first_post(request):
    return render(request, 'post/poems.html')

def second_post(request):
    return render(request, 'post/stories.html')

def third_post(request):
    return render(request, 'post/third_post.html')