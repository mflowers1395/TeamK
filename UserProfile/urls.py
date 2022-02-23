from django.urls import path
from .import views

urlpatterns =[
    path('profile/', views.launchUserProfile),
    path('register/', views.launchSignUpPage),
]