  
from django.urls import path
from . import views

app_name = 'quiz'
urlpatterns = [

    path('', views.display, name='display'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('results/', views.ResultsView.as_view(), name='results'),
    path('vote/', views.vote, name='vote'),
]