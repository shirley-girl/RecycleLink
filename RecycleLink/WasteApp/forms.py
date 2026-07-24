from django import forms
from .models import WasteRequest, Company

class WasteRequestForm(forms.ModelForm):
    class Meta:
        model = WasteRequest
        # We only want the user to fill these three; the rest (user, status, date) are automatic
        fields = ['waste_type', 'location', 'contact_phone', 'preferred_pickup_date', 'description', 'assigned_company']
        
        widgets = {
            'waste_type': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Kilimani, Nairobi'}),
            'contact_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 0712345678'}),
            'preferred_pickup_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe the waste you want collected.', 'rows': 4}),
            'assigned_company': forms.Select(attrs={'class': 'form-control'}),
        }
        

    def __init__(self, *args, **kwargs):
        super(WasteRequestForm, self).__init__(*args, **kwargs)
        self.fields['assigned_company'].queryset = Company.objects.filter(is_verified=True)
        self.fields['assigned_company'].label = "Chose a Service Provider"
        self.fields['assigned_company'].empty_label = "Select a Company(optional)"