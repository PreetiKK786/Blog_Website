# Generated by Django 3.2.6 on 2021-09-18 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default="My Freakin' Awesome Blog!", max_length=255),
        ),
    ]
