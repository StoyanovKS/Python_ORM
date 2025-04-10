from django.db import models
from django.db.models import Count
from django.core.validators import (
    MinValueValidator, MaxValueValidator, MinLengthValidator
)
from .mixins import NameMixin, BirthDateMixin, NationalityMixin


class DirectorManager(models.Manager):
    def get_directors_by_movies_count(self):
        return self.annotate(movie_count=Count('movies')) \
                   .order_by('-movie_count', 'full_name')
    
class Director(NameMixin, BirthDateMixin, NationalityMixin):
    years_of_experience = models.SmallIntegerField(
        default=0,
        validators=[MinValueValidator(0)]
    )
    objects = DirectorManager()

    def __str__(self):
        return self.full_name


class Actor(NameMixin, BirthDateMixin, NationalityMixin):
    is_awarded = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class Movie(models.Model):
    GENRE_CHOICES = [
        ('Action', 'Action'),
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('Other', 'Other'),
    ]

    title = models.CharField(
        max_length=150,
        validators=[MinLengthValidator(5)]
    )
    release_date = models.DateField()
    storyline = models.TextField(null=True, blank=True)

    genre = models.CharField(
        max_length=6,
        choices=GENRE_CHOICES,
        default='Other'
    )

    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=0.0,
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(10.0)
        ]
    )

    is_classic = models.BooleanField(default=False)
    is_awarded = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)

    director = models.ForeignKey(
        Director,
        on_delete=models.CASCADE,
        related_name='movies'
    )
    starring_actor = models.ForeignKey(
        Actor,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='starring_movies'
    )
    actors = models.ManyToManyField(
        Actor,
        related_name='movies'
    )

    def __str__(self):
        return self.title


