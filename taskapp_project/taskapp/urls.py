from django.urls import path
from . import views
from .views import(
    Task_Create_View,
    Task_Update_View,
    Task_Delete_View
)


app_name ='taskapp'

urlpatterns = [
    path('', views.home, name='home-view'),
    path('create/',Task_Create_View.as_view(),name='task-create'),
    path('update/<int:pk>/',Task_Update_View.as_view(),name='task-update'),
    path('delete/<int:pk>/',Task_Delete_View.as_view(),name='task-delete'),
  
]