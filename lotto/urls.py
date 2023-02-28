from django.urls import path

from . import views

urlpatterns = [
    path('', views.ajax, name='ajax'),
    path('form/', views.form, name='form'),
]
