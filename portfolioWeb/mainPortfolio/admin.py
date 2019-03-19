from django.contrib import admin
from django.http import HttpResponse

from .models import *
admin.site.register(facts)
admin.site.register(skills)
admin.site.register(aboutMe)
admin.site.register(header)
admin.site.register(expertises)
admin.site.register(qualifications)
admin.site.register(projects)
admin.site.register(socialLinks)

