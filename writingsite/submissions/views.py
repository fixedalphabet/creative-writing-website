from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import *

# Create your views here.


def index(request):

    writingList = Writing.objects.all()
    data = {'writingList': writingList}
    return render(request, 'submissions/index.html', data)


def view(request, submission_id):
    submission = get_object_or_404(Writing, pk=submission_id)
    comments = Comment.objects.order_by('date_uploaded').reverse()
    return render(request, 'submissions/view.html', {'submission': submission, 'comments': comments})


def comment(request, submission_id):
    submission = get_object_or_404(Writing, pk=submission_id)
    text = request.POST['text']
    if text == '':
        return redirect(view)

    Comment.objects.create(content=text, writing=submission, author=request.user)

    return redirect(view, submission_id)
