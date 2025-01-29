# Generated by Django 5.1.5 on 2025-01-25 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tkeleza', '0003_authorprofile_remove_article_author_location_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author_profile',
        ),
        migrations.AddField(
            model_name='article',
            name='author_name',
            field=models.CharField(default='Unknown Author', max_length=255),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='article_images/'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='AuthorProfile',
        ),
    ]
