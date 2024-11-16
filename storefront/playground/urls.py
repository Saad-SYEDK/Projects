from django.urls import path
from . import views

#URLConfs
urlpatterns = [
    path('hello/', views.say_hello)
]