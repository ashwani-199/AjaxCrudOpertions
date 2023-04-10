from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='enroll.index'),
    path('add', views.add, name='enroll.add'),
    path('edit', views.edit, name='enroll.edit'),
    path('delete', views.delete, name='enroll.delete'),

    path('home', views.home, name='home'),
    path('home/add-vegetable', views.add_vegetable, name='add'),
    path('home/delete', views.vege_delete, name='delete'),
]