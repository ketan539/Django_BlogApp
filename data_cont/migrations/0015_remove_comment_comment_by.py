# Generated by Django 4.1.7 on 2023-03-25 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_cont', '0014_alter_comment_comment_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_by',
        ),
    ]