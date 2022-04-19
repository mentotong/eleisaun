
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admeleisauntl/', admin.site.urls),
    path('', include(('website.urls', 'website'), namespace='website')),
]
