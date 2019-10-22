from django.db import models

# Create your models here.


class Writing(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    date_uploaded = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    content = models.TextField()
    writing = models.ForeignKey(Writing, on_delete=models.CASCADE)
    date_uploaded = models.DateTimeField(auto_now_add=True)
