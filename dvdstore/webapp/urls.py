from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clerk/', views.clerk, name='clerk'),
    path('index/', views.index, name='index')
]
