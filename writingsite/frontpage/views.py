from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    data = {'text': "This is now shown."}
    return render(request, 'frontpage/homepage.html', data)
