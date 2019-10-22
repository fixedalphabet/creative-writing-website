from django.db import models

# Create your models here.


class Writing(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()


class Comment(models.Model):
    content = models.TextField()
    writing = models.ForeignKey(Writing, on_delete=models.CASCADE)
