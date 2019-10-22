from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    postList = Post.objects.order_by('date_uploaded').reverse()
    data = {'postList': postList}
    return render(request, 'frontpage/homepage.html', data)
