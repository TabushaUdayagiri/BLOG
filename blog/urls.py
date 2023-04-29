from django.contrib import admin
from django.urls import path,include
from app1.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('app1/',include('app1.urls',namespace='app1')),
]
