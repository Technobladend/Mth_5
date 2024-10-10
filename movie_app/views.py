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

@api_view(['GET', 'POST'])
def director_list_create_api_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        data = DirectorSerializer(instance=directors, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        name = request.data.get('name')

        director = Director.objects.create(
            name=name,
        )

        return Response(data={'director_id': director.id},
                        status=status.HTTP_201_CREATED)



@api_view(['GET', 'PUT', 'DELETE'])
def director_details_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, 
                        data={'detail': 'Director does not exist in database'})

    if request.method == 'GET':
        data = DirectorSerializer(instance=director).data
        return Response(data=data)

    elif request.method == 'PUT':
        director.name = request.data.get('name')
        director.save()
        return Response(data=DirectorSerializer(director).data,
                        status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST'])
def movie_list_create_api_view(request):
    if request.method == 'GET':
        movies = Movie.objects.prefetch_related('reviews').all()
        data = MovieSerializer(instance=movies, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director')

        movie = Movie.objects.create(
            title=title,
            description=description,
            duration=duration,
            director_id=director_id,
        )

        return Response(data={'movie_id': movie.id},
                        status=status.HTTP_201_CREATED)



@api_view(['GET', 'PUT', 'DELETE'])
def movie_details_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
        data = MovieSerializer(instance=movie).data
        data.pop('reviews', None)
        data.pop('average_rating', None)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'detail': 'Movie does not exist in database'})
    
    if request.method == 'GET':
        data = MovieSerializer(instance=movie).data
        return Response(data=data)
    
    elif request.method == 'PUT':
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director_id = request.data.get('director')
        movie.save()
        return Response(data=MovieSerializer(movie).data,
                        status=status.HTTP_201_CREATED)
    
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET'])
def movie_reviews_list_api_view(request):
    movies = Movie.objects.all()
    data = MovieReviewSerializer(instance=movies, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)
    
    


@api_view(['GET', 'POST'])
def review_list_create_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        data = ReviewSerializer(instance=reviews, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        text = request.data.get('text')
        movie_id = request.data.get('movie_id')
        stars = request.data.get('stars')
        
        review = Review.objects.create(
            text=text,
            movie_id=movie_id,
            stars=stars,
        )

        return Response(data={'review_id': review.id},
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_details_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
        data = ReviewSerializer(instance=review).data
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'detail': 'Review does not exist in database'})
    
    if request.method == 'GET':
        data = ReviewSerializer(instance=review).data
        return Response(data=data)
    
    elif request.method == 'PUT':
        review.text = request.data.get('text')
        review.stars = request.data.get('stars')
        review.movie_id = request.data.get('movie_id')
        review.save()
        return Response(data=ReviewSerializer(review).data,
                        status=status.HTTP_201_CREATED)
    
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
