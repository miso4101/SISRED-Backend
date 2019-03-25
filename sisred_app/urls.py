from django.urls import path
from . import views

urlpatterns = [

    path('post_proyecto_red/', views.post_proyecto_red, name='agregar_proyecto_red'),
    path('detallered/', views.get_detallered, name='detallered'),
    path('detallered/metadata/', views.get_detallered_metadata, name='detallered'),
    path('detallered/personas/', views.get_detallered_personas, name='detallered'),
    path('detallered/recursos/', views.get_detallered_recursos, name='detallered'),
    path('detallered/proyectos/', views.get_detallered_proyectosred, name='detallered'),
    path('creacion/', views.create, name='creacion'),
    path('agregar/', views.add, name='agregr'),
    path('reds/asignados/<int:id>', views.get_reds_asignados, name='reds_asignados'),

]