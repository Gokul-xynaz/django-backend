from django.http import HttpResponse
from django.shortcuts import render

def home_page (request):
    return render(request, "navbar.html")

def products(request):
    products = []
    return render(request, "products.html", {'products': products})