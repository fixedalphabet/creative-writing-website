from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    file_upload = models.FileField()
    date_uploaded = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tags', blank=True)


class Tags(models.Model):
    tag = models.CharField(max_length=50)
