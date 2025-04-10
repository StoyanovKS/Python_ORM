from django.db import models
from django.db.models import Count


class LabelManager(models.Manager):
    def get_labels_by_albums_count(self):
        """
        Returns labels ordered by number of albums (descending), then by name (ascending).
        """
        return self.annotate(album_count=Count('albums')) \
                   .order_by('-album_count', 'name')
