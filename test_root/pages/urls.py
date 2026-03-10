from django.urls import path
from . import views

urlpatterns = [
    path('request-info/', views.request_info, name='request_info'),
    path('<int:material>/<int:weight>/<int:years>/', views.ghost_gear, name='ghost_gear'),
    path('<str:pagename>/', views.index, name='index'),
    path('', views.index, name='index'),
]