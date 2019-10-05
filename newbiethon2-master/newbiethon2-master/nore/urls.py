from django.urls import path
from . import views

urlpatterns=[
    path('list/', views.list, name="list"),
    path('show/<int:room_id>/', views.show, name='show'),
    path('new/', views.new, name='new'),
    path('roomcreate/', views.roomcreate, name='roomcreate'),
    path('search_map/', views.search_map, name='search_map'),
    path('noreroom_1/', views.noreroom_1, name='noreroom_1'),
    path('noreroom_2/', views.noreroom_2, name='noreroom_2'),
    path('noreroom_3/', views.noreroom_3, name='noreroom_3'),
    path('noreroom_4/', views.noreroom_4, name='noreroom_4'),
]