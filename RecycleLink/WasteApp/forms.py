from django import forms
from .models import WasteRequest, Company

class WasteRequestForm(forms.ModelForm):
    class Meta:
        model = WasteRequest
        # We only want the user to fill these three; the rest (user, status, date) are automatic
        fields = ['waste_type', 'quantity', 'location', 'assigned_company']
        
        widgets = {
            'waste_type': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Estimated weight in kg'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Kilimani, Nairobi'}),
        }

    def __init__(self, *args, **kwargs):
        super(WasteRequestForm, self).__init__(*args, **kwargs)
        self.fields['assigned_company'].queryset = Company.objects.filter(is_verified=True)
        self.fields['assigned_company'].label = "Chose a Service Provider"
        self.fields['assigned_company'].empty_label = "Select a Company(optional)"