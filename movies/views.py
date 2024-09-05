from django.shortcuts import render, get_object_or_404

from .models import ListMovies
# Create your views here.

def index(request):
    return render(request, 'movies/index.html', {})

def about(request):
    return render(request, 'movies/about.html', {})

def movie_list(request):
    movies =  ListMovies.objects.all()
    print(movies)
    content = {
        'movies':movies
    }
    return render(request, 'movies/movies.html', content)

# displays the datails of the specific movie
# gets the movie primarykey to identify the movie that user wants to specify
def movie_details(request, pk):
    movie = get_object_or_404(ListMovies, pk=pk)
    content = {
        'movies' : movie
    }
    
    return render(request, 'movies/moviesdetail.html', content)
