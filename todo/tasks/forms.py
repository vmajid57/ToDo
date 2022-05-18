from django import forms
from .models import Task

class TaskForm(forms.Form):
    taskName = forms. CharField(max_length = 255)
    description = forms.CharField(max_length = 500)
    tagName = forms. CharField(max_length = 255)
    groupName = forms. CharField(max_length = 255)
