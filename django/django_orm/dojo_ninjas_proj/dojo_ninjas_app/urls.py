from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('dojos',views.add_dojo),
    path('',views.dojos_list),
    path('ninja',views.add_ninja),
]