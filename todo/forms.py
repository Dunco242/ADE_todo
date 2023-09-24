from django import forms
from .models import Task
import json

from crispy_forms.helper  import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class DateInput(forms.DateInput):
    input_type = 'date'

    
class TaskForm(forms.ModelForm):
	task_name = forms.CharField(
                            widget=forms.TextInput(attrs={'id': 'floatingInput', 'class': 'form-control mb-3'}),
                            required=False)
	task_description = forms.CharField(
                            widget=forms.TextInput(attrs={'id': 'floatingInput', 'class': 'form-control mb-3'}),
                            required=False)
	due_date = forms.DateTimeField(widget=DateInput(attrs={'class': 'form-control mb-3'}),)
	task_priority = forms.IntegerField()

	class Meta:
		model=Task
		fields=['task_name','task_description','due_date','task_priority']