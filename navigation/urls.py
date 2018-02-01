from django.urls import path , include
from . import views

urlpatterns = [
    path('navigation/',views.navigation,name='navigation'),
    path('register/',views.register,name='register'),
    path('store/',views.store,name='store'),
    path('login/' , views.login,name='login'),
    path('login_check/' , views.login_check,name='login_check'),
    path('logout/' , views.logout,name='logout'),
]
