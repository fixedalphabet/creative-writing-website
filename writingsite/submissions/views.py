from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.


def index(request):
    writingList = Writing.objects.all()
    data = {'writingList': writingList}
    return render(request, 'submissions/index.html', data)


def view(request, submission_id):
    submission = get_object_or_404(Writing, pk=submission_id)
    return render(request, 'submissions/view.html', {'submission':submission})