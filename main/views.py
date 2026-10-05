from django.shortcuts import render
from patients.models import MedicalRecord

# Create your views here.
def homepage(request):
    record =  MedicalRecord.objects.get(id=1)
    return render(request, 'homepage.html', {'record':record})
