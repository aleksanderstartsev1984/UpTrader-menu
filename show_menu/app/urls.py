from django.urls import path

from app import views


app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),

    path('create_test_menu', views.create_test_menu, name='create_test_menu'),
    path('delete_test_menu', views.delete_test_menu, name='delete_test_menu'),

]
