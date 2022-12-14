# Generated by Django 4.1.2 on 2022-10-31 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Celebrities',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('place', models.CharField(max_length=50, null=True)),
                ('masterpiece', models.CharField(max_length=500, null=True)),
                ('person_link', models.URLField(default=None, max_length=500, null=True)),
                ('award_link', models.URLField(default=None, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'Знаменитость',
                'verbose_name_plural': 'Знаменитости',
                'db_table': 'hh_celebrities',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movieid', models.IntegerField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='posters/', verbose_name='Постер')),
                ('title', models.CharField(max_length=30)),
                ('year', models.IntegerField()),
                ('rating', models.FloatField(blank=True, null=True)),
                ('metascore', models.IntegerField(blank=True, default=None, null=True)),
                ('rank', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(max_length=500, null=True)),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('genres', models.CharField(max_length=100)),
                ('gross_earning_in_mil', models.FloatField(blank=True, default=None, null=True)),
                ('celebrities', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='hh.celebrities')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
                'db_table': 'hh_movies',
            },
        ),
    ]
