from django.urls import path

from app import views


app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),

    path('create_menu', views.create_menu, name='create_menu'),
    path('delete_menu', views.delete_menu, name='delete_menu'),

]
