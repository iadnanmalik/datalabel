# Generated by Django 3.1 on 2020-08-19 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ImageLabel', '0003_auto_20200819_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='flag',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='image',
            name='username',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]
