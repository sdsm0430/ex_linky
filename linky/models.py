from django.db import models
from django.utils import timezone

class TheManWhoLaugh(models.Model):
    actor = models.CharField(null=True, max_length=50)
    song = models.CharField(null=True, max_length=400)
    music = models.CharField(null=True, max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()