from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    duration = models.CharField(max_length=100)
    director = models.ForeignKey(Director, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

class Review(models.Model):
    text = models.CharField(max_length=255)
    movie = models.ForeignKey(Movie, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
