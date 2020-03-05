from django.urls import path

from candidates import views

urlpatterns = [
    path('', views.index, name='index')
]