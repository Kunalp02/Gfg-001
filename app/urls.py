from django.contrib import admin
from django.urls import path, include
from . import views     

urlpatterns = [
    path('', views.show_all, name="show_all"),
    path('show_indians/', views.show_indians, name="show_indians"),
    path('show_non_indians/', views.show_non_indians, name="show_non_indians")
]
