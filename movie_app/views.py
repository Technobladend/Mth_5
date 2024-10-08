from django.shortcuts import render

from .models import Director, Movie, Review
from .serializible import (
    DirectorSerializer,
    MovieSerializer,
    MovieReviewSerializer,
    ReviewSerializer,
)

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def director_list_api_view(request):
    directors = Director.objects.all()
    data = DirectorSerializer(instance=directors, many=True).data
    return Response(data=data)


@api_view(['GET'])
def director_details_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
        data = DirectorSerializer(instance=director).data
        return Response(data=data)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'detail': 'Director does not exist in database'})
    

@api_view(['GET'])
def movie_list_api_view(request):
    movies = Movie.objects.prefetch_related('reviews').all()
    data = MovieSerializer(instance=movies, many=True).data
    return Response(data=data)



@api_view(['GET'])
def movie_details_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
        data = MovieSerializer(instance=movie).data
        data.pop('reviews', None)
        data.pop('average_rating', None)
        return Response(data=data)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'detail': 'Movie does not exist in database'})
    

@api_view(['GET'])
def movie_reviews_list_api_view(request):
    movies = Movie.objects.all()
    data = MovieReviewSerializer(instance=movies, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)
    
    


@api_view(['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()
    data = ReviewSerializer(instance=reviews, many=True).data
    return Response(data=data)


@api_view(['GET'])
def review_details_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
        data = ReviewSerializer(instance=review).data
        return Response(data=data)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'detail': 'Review does not exist in database'})
    
