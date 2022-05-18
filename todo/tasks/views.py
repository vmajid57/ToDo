from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import TaskForm

def task (request):
    template = loader.get_template('task.html')
    return HttpResponse(template.render())

def newTask(request):
    if request.method == "POST":
        newtaskForm = TaskForm(request.POST)

        if newtaskForm.is_valid():
            tname = newtaskForm.cleaned_data['taskName']
    else:
        newtaskForm= TaskForm()

    return render(request, 'task.html', {"tname" : tname})
