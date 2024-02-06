from django.contrib import admin
from django.urls import path
from urlApp import views

urlpatterns = [
    path('hyd-jobs/', views.hydJobs),
    path('pune-jobs/', views.puneJobs),
    path('mumbai-jobs/', views.mumbaiJobs),
    path('chenai-jobs/', views.chenaiJobs),
]