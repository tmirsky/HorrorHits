from django.db import models

from django.urls import reverse


class Movie(models.Model):
    movieid = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30, verbose_name='Название')
    year = models.DateField(blank=False, null=False, verbose_name='Год производства')
    rating = models.FloatField(blank=True, null=True, verbose_name='Оценка')
    metascore = models.IntegerField(blank=True, null=True, default=None, verbose_name='Рейтинг Metascore')
    description = models.CharField(max_length=500, null=True, verbose_name='Описание')
    duration = models.IntegerField(blank=True, null=True, verbose_name='Продолжительность')
    genres = models.CharField(max_length=27, verbose_name='Жанр')
    image = models.ImageField(upload_to='posters/', verbose_name='Постер')
    # is_published = models.BooleanField(default=False, verbose_name='Опубликован')
    celebrities = models.ForeignKey('Celebrities', related_name='+', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie', kwargs={'movie_slug': self.slug})

    class Meta:
        db_table = 'hh_movies'
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ['title', '-year']


class Celebrities(models.Model):
    name = models.CharField(max_length=50, primary_key=True, verbose_name='Полное имя')
    date_of_birth = models.DateField(blank=False, null=True, verbose_name='Дата рождения')
    place = models.CharField(max_length=500, null=True, verbose_name='Страна')
    overview = models.CharField(max_length=500, null=True, verbose_name='Описание')
    biography = models.CharField(max_length=500, null=True, verbose_name='Биография')
    masterpiece = models.CharField(max_length=500, null=True, verbose_name='Лучшие работы')
    person_link = models.URLField(max_length=500, null=True, default=None)
    award_link = models.URLField(max_length=500, null=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'hh_celebrities'
        verbose_name = 'Знаменитость'
        verbose_name_plural = 'Знаменитости'
