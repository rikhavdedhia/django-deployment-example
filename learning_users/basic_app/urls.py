from django.urls import path
from basic_app import views

#template tagging
app_name = 'basic_app'

urlpatterns = [
    path('register/', views.register,name = 'register'),
    path('index/', views.index, name = 'index'),
    path('', views.index, name = 'index'),
    path('logout/', views.user_logout, name = 'logout'),
    path('user_login/', views.user_login, name = 'user_login')
]
