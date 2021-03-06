from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls import url
from .import views
from django.conf import settings
from django.conf.urls.static import static
from filebrowser.sites import site


urlpatterns = [

    path('',views.index),
    path('about/',views.about),
    path('mywork/',views.mywork),
    url(r'^tinymce/',include('tinymce.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^admin/filebrowser/', site.urls),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT )
urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT )

