from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('delete/<int:id>/', views.delete_record , name='deleterec'),
    path('edit/<int:id>/', views.edit_record , name='editrec')
]
