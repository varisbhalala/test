from django.urls import path , include
from . import views

urlpatterns = [
    path('navigation/',views.navigation,name='navigation'),
    path('register/',views.register,name='register'),
    path('store/',views.store,name='store'),
]
