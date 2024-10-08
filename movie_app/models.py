from django.db import models
from django.db.models import Avg


class Director(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

    @property
    def movie_count(self):
        return self.movies.count()
    

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    duration = models.CharField(max_length=100)
    director = models.ForeignKey(Director, null=True, blank=True, on_delete=models.CASCADE, related_name='movies')

    def __str__(self):
        return self.title
    
    @property
    def average_rating(self):
        average_rating = self.reviews.aggregate(average=Avg('stars'))['average']
        return average_rating if average_rating is not None else 0
    
    @property
    def review_list(self):
        return [i.text for i in self.reviews.all()]
    



STARS_CHOISES = (
    (i, "* " * i) for i in range(1, 6)
)
    

class Review(models.Model):
    text = models.CharField(max_length=255)
    movie = models.ForeignKey(Movie, null=True, blank=True, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(choices=STARS_CHOISES, default=5)

    def __str__(self):
        return self.text
