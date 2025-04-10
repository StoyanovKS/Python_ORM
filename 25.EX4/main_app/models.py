from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
from .managers import LabelManager

class Label(models.Model):
    name = models.CharField(
        max_length=140,
        validators=[MinLengthValidator(2)]
    )
    headquarters = models.CharField(
        max_length=150,
        default='Not specified'
    )
    market_share = models.FloatField(
        default=0.1,
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(100.0)
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)


    objects = LabelManager()
    
    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(
        max_length=140,
        validators=[MinLengthValidator(2)]
    )
    nationality = models.CharField(
        max_length=3,
        validators=[
            MinLengthValidator(3),
            MaxLengthValidator(3)
        ]
    )
    awards = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    ALBUM_TYPES = [
        ('Single', 'Single'),
        ('Soundtrack', 'Soundtrack'),
        ('Remix', 'Remix'),
        ('Other', 'Other'),
    ]

    title = models.CharField(
        max_length=150,
        validators=[MinLengthValidator(1)]
    )
    release_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    type = models.CharField(
        max_length=10,
        choices=ALBUM_TYPES,
        default='Other'
    )
    is_hit = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    label = models.ForeignKey(
        Label,
        on_delete=models.SET_NULL,
        null=True,
        related_name='albums'
    )

    artists = models.ManyToManyField(
        Artist,
        related_name='albums'
    )

    def __str__(self):
        return self.title
