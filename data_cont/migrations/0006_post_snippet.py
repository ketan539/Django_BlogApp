# Generated by Django 4.1.7 on 2023-03-21 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_cont', '0005_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click here to view the Post.', max_length=255),
        ),
    ]
