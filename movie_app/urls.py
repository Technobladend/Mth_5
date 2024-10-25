from . import views

from django.urls import path


urlpatterns = [
    path('directors/', views.DirectorListAPIView.as_view(), name='director_list'),
    path('directors/<int:id>/', views.DirectorDetailView.as_view(), name='director_id'),
    path('movies/', views.MovieListAPIView.as_view(), name='movie_list'),
    path('movies/<int:id>/', views.MovieDetailView.as_view(), name='movie_id'),
    path('reviews/', views.ReviewListAPIView.as_view(), name='review_list'),
    path('reviews/<int:id>/', views.ReviewDetailView.as_view(), name='review_id'),
]