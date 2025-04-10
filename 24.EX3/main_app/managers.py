from django.db import models
from django.db.models import Count


class AstronautManager(models.Manager):
    def get_astronauts_by_missions_count(self):
        """
        Retrieve and return all astronaut objects, ordered by:
        - Number of missions (descending)
        - Phone number (ascending)
        """
        return self.annotate(missions_count=Count('missions')) \
                   .order_by('-missions_count', 'phone_number')
