from django.urls import path , include
from . import views

urlpatterns = [
    path('navigation/',views.navigation,name='navigation'),
    path('register/',views.register,name='register'),
    path('store/',views.store,name='store'),
    path('login/' , views.login,name='login'),
    path('login_check/' , views.login_check,name='login_check'),
    path('logout/' , views.logout,name='logout'),
    path('publisher_panel/', views.publisher_panel, name='publisher_panel'),
    path('advertiser_panel/', views.advertiser_panel, name='advertiser_panel'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('check_email/', views.check_email, name='check_email'),
    path('new_password/', views.new_password, name='new_password'),
    path('save_password/', views.save_password, name='save_password'),
]
