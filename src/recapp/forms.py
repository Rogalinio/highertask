from django import forms
from .models import Grade

class GradeModelForm(forms.ModelForm):
    #value = forms.IntegerField(widget=forms.TextInput(attrs={"placeholder": "Your mark"}))
    class Meta:
        model = Grade
        fields = [
            'value',
            'task',
            'candidate',
            'recruiter'
        ]
        unique_together = ('candidate','task')