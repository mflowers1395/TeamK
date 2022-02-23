from django.urls import path
from .import views

urlpatterns =[
    path('register/', views.launchRegister),
    path('home/', views.launchHomePage),
]