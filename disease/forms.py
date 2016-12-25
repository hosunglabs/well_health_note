from django import forms

from .models import Disease

class PostForm(forms.ModelForm):

    class Meta:
        model = Disease
        fields = ('name', 'definition', 'definition_image', 'symptom', 'symptom_image', 'diagnosis', 'diagnosis_image', 'treatment', 'treatment_image', 'prognosis', 'prognosis_image', 'common', 'common_image', 'drug', 'drug_image', 'article')
