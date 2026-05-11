from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            'title', 'min_salary', 'max_salary', 'status', 
            'experience_required', 'city', 'country', 'description'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'id': 'jobtitle'}),
            'min_salary': forms.NumberInput(attrs={'id': 'min-salary', 'min': '6000', 'max': '100000'}),
            'max_salary': forms.NumberInput(attrs={'id': 'max-salary', 'min': '6000', 'max': '100000'}),
            'status': forms.Select(attrs={'id': 'jobstatus'}),
            'experience_required': forms.NumberInput(attrs={'id': 'years_of_experience', 'min': '0'}),
            'city': forms.TextInput(attrs={'id': 'city'}),
            'country': forms.TextInput(attrs={'id': 'country'}),
            'description': forms.Textarea(attrs={'id': 'job_description', 'cols': '40', 'rows': '10'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        min_s = cleaned_data.get("min_salary")
        max_s = cleaned_data.get("max_salary")

        if min_s and max_s and max_s < min_s:
            raise forms.ValidationError("Max salary can't be lower than min salary")
        return cleaned_data