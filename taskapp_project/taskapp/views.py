from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy

from .models import Task
from django.views.generic.edit import(
    CreateView,
    UpdateView,
    DeleteView
) 

def home(request):
    task_list = Task.objects.all()
    
    return render(request,'taskapp/homepage.html',{'task_list':task_list})  #'


class Task_Create_View(CreateView):
    model = Task
    fields = ['headline']
    template_name ='taskapp/task_create.html'
    success_url = reverse_lazy("taskapp:home-view")


class Task_Update_View(UpdateView):
    model = Task
    fields = ['headline']
    template_name ='taskapp/task_update.html'
    success_url = reverse_lazy("taskapp:home-view")

class Task_Delete_View(DeleteView):
    model = Task
    # success_url = reverse_lazy('taskapp:home-view')
    success_url = reverse_lazy("taskapp:home-view")

    # def get_object(self):
    #     post =self.kwargs.get("id")
    #     return get_object_or_404(Task,id=post)