from django.urls import path     
from . import views
urlpatterns = [
    path('', views.counter),
    path('destroy_session', views.destroy),
    path('plus_two', views.plus_two)
    ]