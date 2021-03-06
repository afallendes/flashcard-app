from django.urls import path

from frontend import views

urlpatterns = [
    path('', views.hello_world, name='hello_world')
]
