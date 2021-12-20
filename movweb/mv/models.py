from django.db import models

# Create your models here.

class akbar(models.Model):
    movie_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    year = models.IntegerField()
    discription = models.TextField()
    rating = models.IntegerField()
    img = models.ImageField(upload_to="img")

    def __str__(self):
        return self.movie_name



