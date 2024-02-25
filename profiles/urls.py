from django.urls import path
from profiles import views

urlpatterns = [
    path('profiles/', views.ProflieList.as_view()),
    path('profiles/<int:pk>/', views.ProfileView.as_view()),
]