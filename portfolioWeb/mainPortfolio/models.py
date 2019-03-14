from django.db import models
import datetime
from django.utils import timezone
from tinymce.models import HTMLField

class header(models.Model):
    def __str__(self):
        return str(self.heading)
    class Meta:
        verbose_name_plural = "Headers"
    intro = models.CharField(max_length = 100)
    heading = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    image = models.ImageField()

class aboutMe(models.Model):
    def __str__(self):
        return str(self.short)
    class Meta:
        verbose_name_plural = "About Me"
    text = models.TextField()
    short = models.CharField(max_length = 100)
    image = models.ImageField()

class skills(models.Model):
    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name_plural = "Skills"
    name = models.TextField()
    description = models.TextField()
    label = models.TextField()

class facts(models.Model):
    def __str__(self):
        return str(self.description)
    class Meta:
        verbose_name_plural = "Facts"
    count_to_number = models.IntegerField()
    description = models.TextField()
    
    
