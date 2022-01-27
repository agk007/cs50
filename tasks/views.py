from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
tasks=["foo","bar","boo"]

class NewTaskForm(forms.Form):
    task=forms.CharField(label="new task")
def index(request):
    return render(request,"tasks/index.html",{
        "tasks":tasks
    })

def add(request):
    if request.method == "POST":
        form =NewTaskForm(request.POST)  #collcet and store all data enterd through site
        if form.is_valid():
            task=form.cleaned_data["task"]
            tasks.append(task)
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request,"tasks/add.html",{
                "form":form
            })
    return render(request,"tasks/add.html",{
        "form":NewTaskForm()
    })
print(*tasks)