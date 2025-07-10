from django.urls import path
from .views.home_views import home
from .views.pasajeros_views import PasajerosViews

app_name = 'gestion'

urlpatterns = [
    # Vista principal
    path('', home, name='home'),
    
    # CRUD de Pasajeros
    path('pasajeros/', PasajerosViews.listar_pasajeros, name='pasajeros_listar'),
    path('pasajeros/crear/', PasajerosViews.crear_pasajero, name='pasajeros_crear'),
    path('pasajeros/<int:pasajero_id>/', PasajerosViews.detalle_pasajero, name='pasajeros_detalle'),
    path('pasajeros/<int:pasajero_id>/editar/', PasajerosViews.editar_pasajero, name='pasajeros_editar'),
    path('pasajeros/<int:pasajero_id>/eliminar/', PasajerosViews.eliminar_pasajero, name='pasajeros_eliminar'),
]
