# Generated by Django 3.1 on 2020-08-14 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('voice', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='AudioSentence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentence', models.CharField(max_length=100000)),
                ('flag', models.BooleanField(default=0)),
            ],
        ),
    ]