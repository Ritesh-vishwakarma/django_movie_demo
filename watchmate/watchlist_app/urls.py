from django.urls import path
from . import views


urlpatterns = [
    path("", views.showHello),
    path("list/", views.show_list)
    
]
