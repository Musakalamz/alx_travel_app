from django.urls import path
from . import views

app_name = 'listings'

urlpatterns = [
    path('', views.welcome_view, name='welcome'),
]