from django import forms
from .models import Grade

class GradeModelForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = '__all__'
        unique_together = (('task', 'candidate'),)



