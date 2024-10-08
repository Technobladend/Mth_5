from rest_framework import serializers
from movie_app.models import Director, Movie, Review
from django.db.models import Avg

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title description duration director'.split()


class MovieReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title description duration director average_rating review_list'.split()


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'name movie_count'.split()

