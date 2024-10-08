from . import views

from django.urls import path


urlpatterns = [
    path('directors/', views.director_list_api_view, name='director_list'),
    path('directors/<int:id>/', views.director_details_api_view, name='director_id'),
    path('movies/', views.movie_list_api_view, name='movie_list'),
    path('movies/<int:id>/', views.movie_details_api_view, name='movie_id'),
    path('reviews/', views.review_list_api_view, name='review_list'),
    path('reviews/<int:id>/', views.review_details_api_view, name='review_id'),
    path('movies/reviews/', views.movie_reviews_list_api_view, name='movie_review')
]