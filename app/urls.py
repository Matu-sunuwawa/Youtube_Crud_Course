from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lists/', views.lists, name='lists'),
    path('add_list/', views.addlist, name='add_list'),
    path('update_list/<str:pk>/',views.updatelist, name='update_list'),
    path('delete_list/<str:pk>/', views.deletelist, name='delete_list'),
]
