from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('profile/<str:pk>/', views.profile, name='profile'),
    path('profile_update/', views.profile_update, name='profile_update'),

    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),

    path('algorithm_create/', views.algorithm_create, name='algorithm_create'),
    path('algorithm_update/<str:pk>/', views.algorithm_update, name='algorithm_update'),
    path('algorithm_delete/<str:pk>/', views.algorithm_delete, name='algorithm_delete'),

]