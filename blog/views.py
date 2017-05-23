from django.shortcuts import render
from django.http import HttpResponse
from blog.models import blog
from datetime import datetime
from django.http import Http404

# Create your views here.
def home(request):
    return HttpResponse("Reynold's home page")

def detail(request, id):
    try:
        articles = blog.objects.get(id=str(id))
    except blog.DoesNotExist:
        raise Http404
    return render(request, 'article.html', {'post': articles})


def test(request):
    return render(request, 'test.html', {'current_time':datetime.now()})

def index(request):
    post_list = blog.objects.all()
    return render(request, 'index.html', {'article_list': post_list})
