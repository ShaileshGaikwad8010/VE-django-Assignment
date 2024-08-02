from django.urls import path
from . import views

app_name = 'analysis'
urlpatterns = [
    path('', views.upload_file, name='upload'),
    path('analysis/', views.analyze_file, name='analysis'),
]
