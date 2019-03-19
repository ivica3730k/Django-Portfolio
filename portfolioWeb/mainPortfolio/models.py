from django.db import models
import datetime
from django.utils import timezone
from tinymce.models import HTMLField

class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

class header(models.Model):
    def __str__(self):
        return str(self.heading)
    class Meta:
        verbose_name = "Header"
        verbose_name_plural = "Site headers"
    intro = models.CharField(max_length = 100)
    heading = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    image = models.ImageField()

class aboutMe(models.Model):
    def __str__(self):
        return str(self.short)
    class Meta:
        verbose_name = "About Me"
        verbose_name_plural = "About Me"
    mainHeadline = models.CharField(max_length = 100)
    shortIntro = HTMLField('About me - short intro')
    mainContent = HTMLField('About me - main content')
    short = models.CharField(max_length = 100)
    image = models.ImageField()

class skills(models.Model):
    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "My Skills"
    name = models.TextField()
    description = models.TextField()
    label = models.TextField()

class facts(models.Model):
    def __str__(self):
        return str(self.description)
    class Meta:
        verbose_name = "Fact about me"
        verbose_name_plural = "Facts about me"
    count_to_number = models.IntegerField()
    description = models.TextField()
    
class expertises(models.Model):
    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name = "Experties"
        verbose_name_plural = "My Expertises"
    name = models.CharField(max_length = 100)
    percentage = IntegerRangeField(min_value=0,max_value=100)
    
class qualifications(models.Model):
    def __str__(self):
        return str(self.title)
    class Meta:
        verbose_name = "Qualification"
        verbose_name_plural = "My Qualifications"
    title = models.CharField(max_length = 100)
    content = HTMLField('About qualification')

class projects(models.Model):
    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "My Projects"
    name = models.CharField(max_length = 100)
    description = HTMLField('Describe your project:')

class socialLinks(models.Model):
    def __str__(self):
        return str("Social link set")
    class Meta:
        verbose_name = "Social link-set"
        verbose_name_plural = "My Social links"
    facebook = models.URLField()
    twitter = models.URLField()
    linkedin = models.URLField()
    github = models.URLField()
    youtube = models.URLField()
    