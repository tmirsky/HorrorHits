from django.urls import path

from .views import MovieListView, MovieDetailView

urlpatterns = [
    path('', MovieListView.as_view(), name='index'),
    path('<slug:movie_slug>', MovieDetailView.as_view(), name='movie')
]
