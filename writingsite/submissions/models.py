from django.db import models
from django.conf import settings


class Writing(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    date_uploaded = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, )


class Comment(models.Model):
    content = models.TextField()
    writing = models.ForeignKey(Writing, on_delete=models.CASCADE)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, )
