from django.urls import path
from . import views

app_name = 'patients'


urlpatterns = [
    path('patients_dashboard/', views.patients_dashboard, name='patients_dashboard'),
    path('view_record/', views.view_record, name='view_record')
]