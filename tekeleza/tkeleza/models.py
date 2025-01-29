from django.db import models



class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)  # Store hashed passwords

    def __str__(self):
        return self.username

    


class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    publication_date = models.DateField()
    image = models.ImageField(upload_to='article_images/')
    author_name = models.CharField(max_length=255 )

    author_location = models.CharField(max_length=255) 

    def __str__(self):
        return self.title
