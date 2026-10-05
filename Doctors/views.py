from django.shortcuts import render, redirect
from patients.models import MedicalRecord
from .forms import MedicalRecordForm
from accounts.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404

# Create your views here.
@login_required
def doctors_dashboard(request):
    x = MedicalRecord.objects.get(id=1)
    if request.user.role == 'patients':
        raise Http404
    return render(request, 'doctors_dashboard.html', {'record':x})

@login_required
def add_medical_records(request):
    if request.user.role == 'patients':
            raise Http404
    if request.method != 'POST':
        forms = MedicalRecordForm()
    else:
        forms = MedicalRecordForm(data=request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('Doctors:doctors_dashboard')
    return render(request, 'add_medical_records.html', {'forms':forms})

@login_required
def edit_patient_record(request, medicalrecord_id):
    medical_record = MedicalRecord.objects.get(id=medicalrecord_id)
    records = MedicalRecord.objects.all()
    if request.user.role == 'patients':
            raise Http404
    if request.method != 'POST':
        form = MedicalRecordForm(instance=medical_record)
    else:
        form = MedicalRecordForm(data=request.POST, instance=medical_record)
        if form.is_valid():
            form.save()
            return redirect('Doctors:doctors_dashboard')
    context = {'form': form, 'medical_record': medical_record, 'record': records}
    return render(request, 'edit_patient_record.html', context)


def show_patients(request):
     patients = CustomUser.objects.all().filter(role='patients')
     context = {'patients': patients}
     return render(request, 'show_patients.html', context)


def show_patients_record(request, customuser_id):
     patient = CustomUser.objects.get(id=customuser_id)
     record = patient.medicalrecord_set.order_by("-id")
     context = {'patient':patient, 'records':record}
     return render(request, 'show_patients_record.html', context)
    
