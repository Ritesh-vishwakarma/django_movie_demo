from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from watchlist_app.models import Movie




def showHello(request):
    return HttpResponse('hello world')
def show_list(request):
    movies = Movie.objects.all()
    data = {
        "movies": list(movies.values())
    }
    return JsonResponse(data)
    
