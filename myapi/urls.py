from django.urls import include, path
from rest_framework import routers
from . import views

from django.urls import path


# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('', views.apioverview, name="api-overview"),
    path('list/', views.taskList, name="list"),
    path('detail/<str:pk>/', views.taskDetail, name="detail"),
    path('create/', views.taskcreate, name="create"),
    path('update/<str:pk>', views.taskupdate, name="update"),
    path('delete/<str:pk>', views.taskdelete, name="delete")
]