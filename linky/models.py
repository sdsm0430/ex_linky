from django.db import models
from django.utils import timezone

class korean(models.Model):
    musical = models.CharField(null=True, max_length=50)
    actor = models.CharField(null=True, max_length=50)
    song = models.CharField(null=True, max_length=400)
    music = models.CharField(null=True, max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

class japanese(models.Model):
    musical = models.CharField(null=True, max_length=50)
    actor = models.CharField(null=True, max_length=50)
    song = models.CharField(null=True, max_length=400)
    music = models.CharField(null=True, max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

class chinese(models.Model):
    musical = models.CharField(null=True, max_length=50)
    actor = models.CharField(null=True, max_length=50)
    song = models.CharField(null=True, max_length=400)
    music = models.CharField(null=True, max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

class english(models.Model):
    musical = models.CharField(null=True, max_length=50)
    actor = models.CharField(null=True, max_length=50)
    song = models.CharField(null=True, max_length=400)
    music = models.CharField(null=True, max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

class TMWL_password(models.Model):
    password = models.CharField(null=True, max_length=200)

class TMWL_review(models.Model):
    review = models.CharField(null=True, max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)