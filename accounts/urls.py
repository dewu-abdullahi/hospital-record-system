from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login_page/', views.login_page, name='login_page'),
    path('', include('django.contrib.auth.urls'))
    
]
