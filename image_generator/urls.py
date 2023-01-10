from django.urls import path
from . import views

urlpatterns = [
    path('', views.handle_form_submission, name='images'),
]