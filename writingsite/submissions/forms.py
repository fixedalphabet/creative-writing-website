from django import forms


class SubmissionForm(forms.Form):
    title = forms.CharField(max_length=120)
    content = forms.CharField(widget=forms.Textarea)
