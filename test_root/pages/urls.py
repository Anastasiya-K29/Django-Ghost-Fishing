from django.urls import path
from . import views

urlpatterns = [
    path('<int:material>/<int:weight>/<int:years>/', views.ghost_gear, name='ghost_gear'),
    path('<str:pagename>/', views.index, name='index'),
    path('', views.index, name='index'),
]