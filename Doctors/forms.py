from django import forms
from patients.models import MedicalRecord
from accounts.models import CustomUser

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = [ 'user', 'patient_name', 'doctors_name',  'genotype',  'diagnosis', 'treatment', 'symptoms', 'sex']
        labels  = { 'Name': 'patient_name', 'doctors_name': 'Doctor', 'genotype':'genotype', 'diagnosis': 'diagnosis', 'treatment':'treatment', 'symptoms':'symptoms', 'sex':'sex'}
        widgets = {'diagnosis': forms.Textarea(attrs={'cols': 80}), 'treatment': forms.Textarea(attrs={'cols': 80}), 'symptoms': forms.Textarea(attrs={'cols': 80})}

        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['user'].queryset = CustomUser.objects.filter(
            role = 'patients'
            )
