from django.db import models

class book(models.Model):
    book_name = models.CharField(max_length=100)
    date_added = models.DateField(auto_now=True)
    author = models.CharField(max_length=50)
    series = models.CharField(max_length=50, default='Нет')
    brief_description = models.TextField()
    language = models.CharField(max_length=15)
    release_year = models.IntegerField()
    picture = models.ImageField(upload_to = 'static\Images')
    files = models.FileField(upload_to='static\Files')


class comments(models.Model):
    name = models.CharField(max_length=50)
    comment = models.TextField()
    date = models.DateField(auto_now=True)
    score = models.IntegerField()
    book_id = models.IntegerField()

