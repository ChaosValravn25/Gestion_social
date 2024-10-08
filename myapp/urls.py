from django.urls import path
from . import views


urlpatterns = [
	path('', views.index, name='index'),
	path('about/', views.about, name='about'),
	path('divisiones/', views.division, name='divisiones'),
	path('divisiones/<int:division_id>/', views.division_detalle, name='division_detalle'),
	path('area_trabajo/', views.area_trabajo, name='area_trabajo'),
	path('crear_area/', views.crear_area, name='crear_area'),
	path('crear_division/', views.crear_division, name='crear_division'),
	
]