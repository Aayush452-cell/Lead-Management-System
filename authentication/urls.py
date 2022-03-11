from django.urls import path
from . import views


urlpatterns = [
    path('', views.user_login, name='login'),
    path('index/', views.index,name='index'),
    path('signup/', views.user_register, name='user_register'),
    path('logout/', views.user_logout, name='logout'),
    path('filter/<str:pk>',views.filtering,name='filtering')
]
