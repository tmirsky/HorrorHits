from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Movie


class Mixin:

    content = {
    }


class MovieListView(Mixin, ListView):
    model = Movie
    template_name = 'hh/index.html'
    context_object_name = 'movie'

    def get_queryset(self):
        return Movie.objects.all().order_by()

    def get_context_data(self, *, object_list=None, **kwargs):
        return super(MovieListView, self).get_context_data() | self.content


class MovieDetailView(DetailView):
    model = Movie

# Create your views here.
