from django.shortcuts import render
from .models import MedicalRecord
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.
@login_required
def patients_dashboard(request):
    return render(request, 'patients/patients_dashboard.html')

@login_required
def view_record(request):
    records = MedicalRecord.objects.filter(user = request.user)
    context = {'records':records}
    return render(request, 'patients/records.html', context)




    
