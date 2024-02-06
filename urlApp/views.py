from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hydJobs(request):

    s = '<h1>Hydrabad jobs information</h1>'
    return HttpResponse(s)

def puneJobs(request):

    s = '<h1>Hydrabad jobs information</h1>'
    return HttpResponse(s)

def mumbaiJobs(request):

    s = '<h1>Hydrabad jobs information</h1>'
    return HttpResponse(s)

def chenaiJobs(request):

    s = '<h1>Hydrabad jobs information</h1>'
    return HttpResponse(s)