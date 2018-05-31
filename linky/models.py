from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

class TMWL_korean(models.Model):
    STATUS_CHOICES = (
        ('draft', _('Draft')),
        ('published', _('Published')),
    )
    actor = models.CharField(null=True, max_length=50)
    song = models.CharField(null=True, max_length=400)
    music = models.CharField(null=True, max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

class TMWL_japanese(models.Model):
    STATUS_CHOICES = (
        ('draft', _('Draft')),
        ('published', _('Published')),
    )
    actor = models.CharField(null=True, max_length=50)
    song = models.CharField(null=True, max_length=400)
    music = models.CharField(null=True, max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

class TMWL_chinese(models.Model):
    STATUS_CHOICES = (
        ('draft', _('Draft')),
        ('published', _('Published')),
    )
    actor = models.CharField(null=True, max_length=50)
    song = models.CharField(null=True, max_length=400)
    music = models.CharField(null=True, max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

class TMWL_english(models.Model):
    STATUS_CHOICES = (
        ('draft', _('Draft')),
        ('published', _('Published')),
    )
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