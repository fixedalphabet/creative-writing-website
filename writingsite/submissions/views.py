from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import *
from .forms import SubmissionForm

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('frontpage/index'))
    writingList = Writing.objects.all()
    data = {'writingList': writingList}
    return render(request, 'submissions/index.html', data)


def view(request, submission_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('frontpage/index'))
    submission = get_object_or_404(Writing, pk=submission_id)
    comments = Comment.objects.filter(writing_id=submission_id).order_by('date_uploaded').reverse()
    return render(request, 'submissions/view.html', {'submission': submission, 'comments': comments})


def comment(request, submission_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('frontpage/index'))
    if request.method != 'POST':
        return HttpResponseRedirect(reverse('frontpage/index'))
    submission = get_object_or_404(Writing, pk=submission_id)
    text = request.POST['text']
    if text == '':
        return redirect(view)

    Comment.objects.create(content=text, writing=submission, author=request.user)

    return redirect(view, submission_id)


def new(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('frontpage/index'))
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            _title = form.cleaned_data['title']
            _content = form.cleaned_data['content']
            Writing.objects.create(title=_title, content=_content, author=request.user)
            return redirect(index)
    else:
        form = SubmissionForm()
    return render(request, 'submissions/new.html', {'form': form})
