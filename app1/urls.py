from django.urls import path
from app1 import views

app_name = 'app1'

urlpatterns = [
    path('signup',views.user_signup,name='signup'),
    path('login',views.user_login,name='login'),
    path('dashboard',views.user_dashboard,name='dashboard'),
    path('logout',views.user_logout,name='logout'),
    path('changepwd',views.user_change_pwd,name='changepwd'),
]