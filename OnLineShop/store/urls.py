from django.contrib import admin
from django.urls import path,include
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',home_page,name='home'),
    path('user/',user_page,name='user-page'),
    path('register/',register,name='register'),
    path('login/',login_page,name='login'),
    path('logout/',logout_page,name='logout'),
    path('account/',account_settings,name='settings'),
    path('product/',products_page,name='products'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='store/reset_password.html'),name='password_reset'),
    path('reset_password_done/',auth_views.PasswordResetDoneView.as_view(template_name='store/reset_password_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='store/reset_password_form.html'),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='store/reset_password_send.html'),name='password_reset_complete'),
    path('customer/<int:pk>/',customer_page,name='customer'),
    path('create_order/<int:pk>/',create_order,name='create_order'),
    path('update_order/<int:pk>/',update_order,name='update_order'),
    path('delete_order/<int:pk>/',delete_order,name='delete_order'),

]