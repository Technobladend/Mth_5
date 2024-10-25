from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.RegisterAPIView.as_view(), name='user_registration'),
    path('confirm/', views.ConfirmAPIView.as_view(), name='user_confirmation'),
    path('authentication/', views.AuthAPIView.as_view(), name='user_authentication'),
]
