from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('signup/', views.user_register, name='user_register'),
    path('logout/', views.user_logout, name='logout')
]
