from django.urls import path
from .import views

urlpatterns =[
    path("messagingPannel/", views.launchMessagingPannel),
]