from django.urls import path
from . import views
#from .views import room_create, room_list, room_delete, room_update

urlpatterns = [
    # FBV Urls
    path('', views.dashboard, name='dashboard'),
]