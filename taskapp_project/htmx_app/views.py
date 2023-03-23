
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy

from taskapp.models import Task
from django.views.generic.edit import(
    CreateView,
    UpdateView,
    DeleteView,
) 
from django.views.generic import ListView

def home(request):
    task_list = Task.objects.all()
    return render(request,'htmx_app/homepage.html',{'task_list':task_list}) 


def add_todo(request): 
    title = request.POST.get('title')
    todo = Task.objects.create(headline=title)
    task_list = Task.objects.all()
    return render(request,'htmx_app/partials/todo_list.html',{'task_list':task_list}) 


class Task_Create_View(CreateView):
    model = Task
    fields = ['headline'] 
    # template_name ='htmx_app/task_create.html'
    success_url = reverse_lazy("htmx_app:home-view")

class Task_Update_View(UpdateView):
    model = Task
    fields = ['headline']
    template_name ='htmx_app/task_update.html'
    success_url = reverse_lazy("htmx_app:home-view")

# class Task_Delete_View(DeleteView):
#     model = Task
#     success_url = reverse_lazy("htmx_app:home-view")

    # def get_object(self):
    #     post =self.kwargs.get("id")
    #     return get_object_or_404(Task,id=post)


def delete_todo(request, pk):
    todo = Task.objects.get(pk=pk)
    todo.delete()
    task_list = Task.objects.all()
    return render(request,'htmx_app/partials/todo_list.html',{'task_list':task_list}) 


# class TaskListView(ListView):
#     paginate_by = 5
#     model = Task
#     template_name ='htmx_app/homepage.html'