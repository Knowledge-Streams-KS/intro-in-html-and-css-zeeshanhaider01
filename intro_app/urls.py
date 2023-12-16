from django.urls import path
from intro_app import views

urlpatterns=[
    path("page/",views.display)
]