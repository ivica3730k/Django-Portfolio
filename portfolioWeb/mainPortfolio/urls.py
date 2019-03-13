from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls import url
from .import views
from django.conf import settings
from django.conf.urls.static import static
from filebrowser.sites import site


urlpatterns = [
    url(r'^tinymce/',include('tinymce.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^admin/filebrowser/', site.urls),
    path('post/<int:post_id>',views.postEntry),
    path('',views.index),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT )
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT )

