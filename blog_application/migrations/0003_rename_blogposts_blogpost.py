# Generated by Django 4.2.1 on 2023-05-22 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_application', '0002_rename_projectmodel_blogposts'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogPosts',
            new_name='BlogPost',
        ),
    ]