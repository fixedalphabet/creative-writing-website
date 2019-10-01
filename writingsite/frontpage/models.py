from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    file_upload = models.FileField(blank=True, null=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tags', blank=True)

    def __str__(self):
        return self.title


class Tags(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name_plural = 'Tags'
