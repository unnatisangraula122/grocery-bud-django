from django.urls import path
from . import views

app_name = 'grocery'

urlpatterns = [
    path('', views.index, name='index'),
    path('toggle/<int:item_id>/', views.toggle_completed, name='toggle'),
    path('delete/<int:item_id>/', views.delete_item, name='delete'),
    path('edit/<int:item_id>/', views.edit_item, name='edit'),
     path('add/', views.add_item, name='add'),
]