from django.contrib import admin
from django.urls import include, path
from Todo.views import Create,Update,deleteTask

urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('',Create, name='home'),
    path('updatepost/<str:id>',Update, name='Update'),
    path('deletetaks/<id>',deleteTask,name='Delete_task'),
]