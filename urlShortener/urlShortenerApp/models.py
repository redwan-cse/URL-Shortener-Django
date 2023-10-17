from django.db import models

# Create your models here.
class ShortenedURL(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=10, unique=True)

    def get_absolute_url(self):
        return self.short_url