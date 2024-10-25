from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration_api_view, name='user_registration'),
    path('confirm/', views.confirmation_api_view, name='user_confirmation'),
    path('authentication/', views.authorization_api_view, name='user_authentication'),
]
