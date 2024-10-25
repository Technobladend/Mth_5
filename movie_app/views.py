from django.shortcuts import render

from .models import Director, Movie, Review
from .serializible import (
    DirectorSerializer,
    DirectorValidateSerializer,
    MovieSerializer,
    MovieReviewSerializer,
    MovieValidateSerializer,
    ReviewSerializer,
    ReviewValidateSerializer,
)

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class DirectorListAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

    def post(self, request):
        serializer = DirectorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

        director = Director.objects.create(
            **serializer.validated_data
        )

        return Response(data={'director_id': director.id},
                        status=status.HTTP_201_CREATED)



class DirectorDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = "id"

    def put(self, request, *args, **kwargs):
        serializer = DirectorValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data,
                        status=status.HTTP_201_CREATED)
    def delete(self, request, *args, **kwargs):
        director = self.get_object()
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class MovieListAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def post(self, request, *args, **kwargs):
        serializer = MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)
        
        movies = Movie.objects.create(
            **serializer.validated_data
        )

        return Response(data={'movie_id': movies.id},
                        status=status.HTTP_201_CREATED)



class MovieDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = "id"
    
    def put(self, request, *args, **kwargs):
        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data,
                        status=status.HTTP_201_CREATED)
    
    def delete(self, request):
        movie = self.get_object()
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

    
    


class ReviewListAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def post(self, request, *args, **kwargs):
        serializer = ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)
        
        review = Review.objects.create(
            **serializer.validated_data
        )

        return Response(data={'review_id': review.id},
                        status=status.HTTP_201_CREATED)

class ReviewDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = "id"
    
    def put(self, request, *args, **kwargs):
    
        serializer = ReviewValidateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data,
                        status=status.HTTP_201_CREATED)
    
    def delete(self, request, *args, **kwargs):
        review = self.get_object()
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
