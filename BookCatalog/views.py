from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def launchBookCatalog(request):
    return render(request,'mainCatalog.html')

def launchSearchResults(request):
    return render(request,'searchResults.html')

def launchBuyerPage(request):
    return render(request, "buyerPage.html")
    
def launchSellerPage(request):
    return render (request, "sellerPage.html")