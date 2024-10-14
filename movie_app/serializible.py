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


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=255)


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(required=False, default='No content', max_length=255)
    duration = serializers.CharField(max_length=255)
    director_id = serializers.IntegerField()

    def validate_director_id(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except:
            raise serializers.ValidationError('Director does not exist!')
        return director_id


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(required=True, max_length=255)
    movie_id = serializers.IntegerField(required=True)
    stars = serializers.FloatField(required=True)


    def validate_movie_id(self, movie_id):
        try:
            Movie.objects.get(id=movie_id)
        except:
            raise serializers.ValidationError('Movie does not exist!')
        return movie_id
    

    def validate_stars(self, stars):
        if stars < 0:
                raise serializers.ValidationError('Stars must be greater than zero')
        return stars