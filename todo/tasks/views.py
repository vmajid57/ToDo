from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import TaskForm

def task (request):
    template = loader.get_template('task.html')
    return HttpResponse(template.render())

def newTask(request):
    if request.method == "POST":
        newtaskForm = TaskForm(request.POST)

        if newtaskForm.is_valid():









def login(request):
   username = "not logged in"

   if request.method == "POST":
      #Get the posted form
      MyLoginForm = LoginForm(request.POST)

      if MyLoginForm.is_valid():
         username = MyLoginForm.cleaned_data['username']
   else:
      MyLoginForm = Loginform()

   return render(request, 'loggedin.html', {"username" : username})
