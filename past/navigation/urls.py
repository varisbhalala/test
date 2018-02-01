from django.urls import path , include
from . import views

urlpatterns = [
    path('navigation/',views.navigation,name='navigation'),
]
