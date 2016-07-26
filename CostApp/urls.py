from django.conf.urls import url

from CostApp import views

urlpatterns = [
    url(r'add/', views.Add, name='Add'),
]