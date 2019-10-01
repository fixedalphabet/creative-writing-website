from django.contrib import admin
from .models import Post, Tags

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    filter_horizontal = ['tags', ]

    list_display = ('title', 'date_uploaded')


admin.site.register(Post, PostAdmin)
admin.site.register(Tags)
