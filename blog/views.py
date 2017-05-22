from django.shortcuts import render
from django.http import HttpResponse
from blog.models import blog
from datetime import datetime

# Create your views here.
def home(request):
    return HttpResponse("Reynold's home page")

def detail(request, args_1):
    post = blog.objects.all()[int(args_1)]
    str = ("title = %s, category = %s, content = %s" %(post.title, post.category, post.content))

    return HttpResponse("looking at: %s." % str)


def test(request):
    return render(request, 'test.html', {'current_time':datetime.now()})

def index(request):
    post_list = blog.objects.all()
    return render(request, 'index.html', {'post_list': post_list})
