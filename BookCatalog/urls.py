from django.urls import path
from .import views

urlpatterns =[
    path("mainCatalog/", views.launchBookCatalog),
    path("searchResults/", views.launchSearchResults),
    path("buyerPage/", views.launchBuyerPage),
    path("sellerPage/", views.launchSellerPage),
]