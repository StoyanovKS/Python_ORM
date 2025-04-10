from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, RegexValidator
from .managers import AstronautManager  # Import the custom manager


class TimestampMixin(models.Model):
    """
    A mixin to automatically update the 'updated_at' field whenever an object is saved.
    """
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Astronaut(TimestampMixin):
    """
    Represents an astronaut, storing personal details and their spaceflight experience.
    """
    name = models.CharField(
        max_length=120,
        validators=[MinLengthValidator(2)]
    )
    phone_number = models.CharField(
        max_length=15,
        unique=True,
        validators=[
            RegexValidator(regex=r'^\d+$', message="Phone number must contain only digits.")
        ]
    )
    is_active = models.BooleanField(default=True)
    date_of_birth = models.DateField(null=True, blank=True)
    spacewalks = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])

    # Attach custom manager
    objects = AstronautManager()

    def __str__(self):
        return self.name


class Spacecraft(TimestampMixin):
    """
    Represents a spacecraft, including technical specifications and launch information.
    """
    name = models.CharField(
        max_length=120,
        validators=[MinLengthValidator(2)]
    )
    manufacturer = models.CharField(max_length=100)
    capacity = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    weight = models.FloatField(validators=[MinValueValidator(0.0)])
    launch_date = models.DateField()

    def __str__(self):
        return self.name


class Mission(TimestampMixin):
    """
    Represents a space mission, including associated spacecraft and astronauts.
    """
    STATUS_CHOICES = [
        ("Planned", "Planned"),
        ("Ongoing", "Ongoing"),
        ("Completed", "Completed"),
    ]

    name = models.CharField(
        max_length=120,
        validators=[MinLengthValidator(2)]
    )
    description = models.TextField(null=True, blank=True)
    status = models.CharField(
        max_length=9,
        choices=STATUS_CHOICES,
        default="Planned"
    )
    launch_date = models.DateField()

    # Foreign Key to Spacecraft (One Spacecraft can be used in many Missions)
    spacecraft = models.ForeignKey(
        Spacecraft,
        on_delete=models.CASCADE,
        related_name="missions"
    )

    # Many-to-Many Relationship with Astronauts (A Mission has multiple Astronauts)
    astronauts = models.ManyToManyField(
        Astronaut,
        related_name="missions"
    )

    # Foreign Key to Astronaut (Mission Commander)
    commander = models.ForeignKey(
        Astronaut,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="commanded_missions"
    )

    def __str__(self):
        return f"{self.name} - {self.get_status_display()}"
