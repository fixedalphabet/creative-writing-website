from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    writingList = Writing.objects.order_by('date_uploaded').reverse()
    data = {'writingList': writingList}
    return render(request, 'submissions/index.html')
