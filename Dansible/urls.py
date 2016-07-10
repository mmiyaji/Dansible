from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
#    url(r'^(/)?', include('mainapp.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('mainapp.urls')),
]
