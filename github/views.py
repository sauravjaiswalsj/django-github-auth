from django.shortcuts import render
from django.contrib import admin
from django.urls import path

# Create your views here.

def dashboard_page(request):
    return render(request,'dashboard.html',{}) 

def index_page(request):
    return render(request, 'index.html', {})