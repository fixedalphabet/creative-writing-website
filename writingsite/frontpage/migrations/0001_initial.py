# Generated by Django 2.2.5 on 2019-10-01 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('content', models.TextField()),
                ('file_upload', models.FileField(upload_to='')),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('tags', models.ManyToManyField(blank=True, to='frontpage.Tags')),
            ],
        ),
    ]
