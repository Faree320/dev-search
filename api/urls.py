from django.urls import path
from .views import getRoutes, getProjects, getProject

urlpatterns = [
    path('', getRoutes),
    path('projects/', getProjects),
    path('projects/<str:pk>', getProject),
]
