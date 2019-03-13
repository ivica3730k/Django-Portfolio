from django.contrib import admin
from django.http import HttpResponse

from .models import siteDetails
from .models import category
from .models import post
from .models import staticAssets
from .models import naviBars

admin.site.register(siteDetails)
admin.site.register(category)
admin.site.register(post)
admin.site.register(staticAssets)
admin.site.register(naviBars)