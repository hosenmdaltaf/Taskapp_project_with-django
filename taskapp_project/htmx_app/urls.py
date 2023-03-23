from django.urls import path
from . import views
from .views import(
    Task_Create_View,
    Task_Update_View,
    # Task_Delete_View,
    add_todo,
    delete_todo
    # TaskListView
)

app_name ='htmx_app'

urlpatterns = [
    path('', views.home, name='home-view'),
    # path('task_list/',TaskListView.as_view(),name='task_list'),
    path('create/',Task_Create_View.as_view(),name='task-create'),
    path('update/<int:pk>/',Task_Update_View.as_view(),name='task-update'),
    # path('delete/<int:pk>/',Task_Delete_View.as_view(),name='task-delete'),
    path('add-todo/', add_todo, name='add_todo'),
    path('delete/<int:pk>/', delete_todo, name='delete_todo'),
  
]