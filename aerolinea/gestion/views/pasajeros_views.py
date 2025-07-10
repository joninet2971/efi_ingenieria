from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse

from gestion.services.pasajero_service import PasajeroService

class PasajerosViews:
    """
    Vistas para la gestión de Pasajeros.
    Incluye todas las operaciones CRUD para la entidad Pasajero.
    """
    
    @staticmethod
    def listar_pasajeros(request):
        """Vista para listar todos los pasajeros"""
        service = PasajeroService()
        pasajeros = service.get_all_pasajeros()
            
        context = {
            'pasajeros': pasajeros
        }
        return render(request, 'gestion/pasajeros/listar.html', context)
    
    @staticmethod
    def detalle_pasajero(request, pasajero_id):
        """Vista para mostrar los detalles de un pasajero específico"""
        service = PasajeroService()
        pasajero = service.get_pasajero_by_id(pasajero_id)
        
        if not pasajero:
            messages.error(request, f"No se encontró ningún pasajero con ID {pasajero_id}")
            return redirect('gestion:pasajeros_listar')
        
        context = {
            'pasajero': pasajero
        }
        return render(request, 'gestion/pasajeros/detalle.html', context)
    
    @staticmethod
    def crear_pasajero(request):
        """Vista para crear un nuevo pasajero"""
        if request.method == 'POST':
            # Extraer datos del formulario
            data = {
                'nombre': request.POST.get('nombre'),
                'documento': request.POST.get('documento'),
                'email': request.POST.get('email'),
                'telefono': request.POST.get('telefono'),
                'fecha_nacimiento': request.POST.get('fecha_nacimiento'),
                'tipo_documento': request.POST.get('tipo_documento')
            }
            
            # Crear pasajero utilizando el servicio
            service = PasajeroService()
            pasajero, error = service.create_pasajero(data)
            
            if pasajero:
                messages.success(request, "Pasajero creado exitosamente")
                return redirect('gestion:pasajeros_detalle', pasajero_id=pasajero.id)
            else:
                messages.error(request, error)
                return render(request, 'gestion/pasajeros/crear.html', {'data': data})
        
        # GET request - mostrar formulario vacío
        return render(request, 'gestion/pasajeros/crear.html')
    
    @staticmethod
    def editar_pasajero(request, pasajero_id):
        """Vista para editar un pasajero existente"""
        service = PasajeroService()
        pasajero = service.get_pasajero_by_id(pasajero_id)
        
        if not pasajero:
            messages.error(request, f"No se encontró ningún pasajero con ID {pasajero_id}")
            return redirect('gestion:pasajeros_listar')
        
        if request.method == 'POST':
            # Extraer datos del formulario
            data = {
                'nombre': request.POST.get('nombre'),
                'documento': request.POST.get('documento'),
                'email': request.POST.get('email'),
                'telefono': request.POST.get('telefono'),
                'fecha_nacimiento': request.POST.get('fecha_nacimiento'),
                'tipo_documento': request.POST.get('tipo_documento')
            }
            
            # Actualizar pasajero utilizando el servicio
            updated_pasajero, error = service.update_pasajero(pasajero_id, data)
            
            if updated_pasajero:
                messages.success(request, "Pasajero actualizado exitosamente")
                return redirect('gestion:pasajeros_detalle', pasajero_id=pasajero.id)
            else:
                messages.error(request, error)
                return render(request, 'gestion/pasajeros/editar.html', {'pasajero': pasajero, 'data': data})
        
        # GET request - mostrar formulario con datos del pasajero
        return render(request, 'gestion/pasajeros/editar.html', {'pasajero': pasajero})
    
    @staticmethod
    def eliminar_pasajero(request, pasajero_id):
        """Vista para eliminar un pasajero"""
        service = PasajeroService()
        
        if request.method == 'POST':
            # Eliminar pasajero utilizando el servicio
            success, error = service.delete_pasajero(pasajero_id)
            
            if success:
                messages.success(request, "Pasajero eliminado exitosamente")
            else:
                messages.error(request, error)
                
            return redirect('gestion:pasajeros_listar')
        
        # GET request - mostrar página de confirmación
        pasajero = service.get_pasajero_by_id(pasajero_id)
        
        if not pasajero:
            messages.error(request, f"No se encontró ningún pasajero con ID {pasajero_id}")
            return redirect('gestion:pasajeros_listar')
            
        return render(request, 'gestion/pasajeros/eliminar.html', {'pasajero': pasajero})
