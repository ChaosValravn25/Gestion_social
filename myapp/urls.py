from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path('', views.index, name='index'),
	path('about/', views.about, name='about'),
	path('divisiones/', views.division, name='divisiones'),
	path('divisiones/<int:division_id>/', views.division_detalle, name='division_detalle'),
	path('area_trabajo/', views.area_trabajo, name='area_trabajo'),
	path('crear_area/<int:division_id>/', views.crear_area, name='crear_area'),
	path('crear_division/', views.crear_division, name='crear_division'),
	path('crear_documento/', views.crear_documento, name='crear_documento'),
	path('crear_documento/<int:area_id>/', views.crear_documento, name='crear_documento'),
	path('eliminar_documento/<int:documento_id>/', views.eliminar_documento, name='eliminar_documento'),
	path('eliminar_area/<int:area_id>/', views.eliminar_area, name='eliminar_area'),
	#path('eliminar-areas-seleccionadas/', views.eliminar_areas_seleccionadas, name='eliminar_areas_seleccionadas'),
	
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
