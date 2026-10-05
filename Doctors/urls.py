from django.urls import path
from . import views

app_name = 'Doctors'

urlpatterns = [
    path('doctors_dashboard/', views.doctors_dashboard, name='doctors_dashboard'),
     path('add_medical_records/', views.add_medical_records, name='add_medical_records'),
    path('edit_patient_record/<int:medicalrecord_id>/', views.edit_patient_record, name='edit_patient_record'),
    path('show_patients/', views.show_patients, name='show_patients'),
    path('show_patients_record/<int:customuser_id>', views.show_patients_record, name='show_patients_record')
]

