from django.db import models
import datetime
from django.utils import timezone
from tinymce.models import HTMLField

class naviBars(models.Model):
    def __str__(self):
        return (str(self.text) +" leading to " +str(self.link))
    text = models.CharField(max_length = 30)
    link = models.URLField()

class staticAssets(models.Model):
    def __str__(self):
        return str("Site assets " + str(self.topLeftLabel))
    topLeftLabel = models.CharField(max_length = 50)
    github_link = models.URLField()
    facebook_link = models.URLField()
    linkedin_link = models.URLField()
    copyright_text = models.CharField(max_length = 50)

class siteDetails(models.Model):
    class Meta:
        verbose_name_plural = "Site Detials"
    def __str__(self):
        return self.headline
    headline = models.CharField(max_length = 200)
    slogan = models.CharField(max_length = 200)
    homepicture = models.ImageField(upload_to ="sitePictures",default='defaultSitePic.jpg')

class category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"
    def __str__(self):
        return self.name
    name = models.CharField(max_length = 200)
    description = models.TextField()
    icon = models.ImageField()

class post(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length = 200)
    content = HTMLField('Content')
    featured_image = models.ImageField(upload_to ="postFeaturedImages",default='defaultPostPic.jpg')
    category = models.ForeignKey(category,on_delete=models.CASCADE)
    publish_date = timezone.now()

class aboutMe(models.Model):
    title = models.CharField(max_length = 200)
    content = HTMLField('Content')
    

