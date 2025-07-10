from gestion.models import Pasajero

class PasajeroRepository:
    """
    Repositorio para la entidad Pasajero.
    Se encarga de todas las operaciones de acceso a datos relacionadas con los pasajeros.
    """
    
    @staticmethod
    def get_all():
        """Obtiene todos los pasajeros"""
        return Pasajero.objects.all()
    
    @staticmethod
    def get_by_id(pasajero_id):
        """Obtiene un pasajero por su ID"""
        try:
            return Pasajero.objects.get(id=pasajero_id)
        except Pasajero.DoesNotExist:
            return None
    
    @staticmethod
    def get_by_documento(documento):
        """Obtiene un pasajero por su número de documento"""
        try:
            return Pasajero.objects.get(documento=documento)
        except Pasajero.DoesNotExist:
            return None
    
    @staticmethod
    def create(data):
        """Crea un nuevo pasajero"""
        pasajero = Pasajero(
            nombre=data['nombre'],
            documento=data['documento'],
            email=data['email'],
            telefono=data.get('telefono', None),
            fecha_nacimiento=data.get('fecha_nacimiento', None),
            tipo_documento=data.get('tipo_documento', None)
        )
        pasajero.save()
        return pasajero
    
    @staticmethod
    def update(pasajero_id, data):
        """Actualiza un pasajero existente"""
        pasajero = PasajeroRepository.get_by_id(pasajero_id)
        if not pasajero:
            return None
            
        # Actualizar los campos
        if 'nombre' in data:
            pasajero.nombre = data['nombre']
        if 'documento' in data:
            pasajero.documento = data['documento']
        if 'email' in data:
            pasajero.email = data['email']
        if 'telefono' in data:
            pasajero.telefono = data['telefono']
        if 'fecha_nacimiento' in data:
            pasajero.fecha_nacimiento = data['fecha_nacimiento']
        if 'tipo_documento' in data:
            pasajero.tipo_documento = data['tipo_documento']
            
        pasajero.save()
        return pasajero
    
    @staticmethod
    def delete(pasajero_id):
        """Elimina un pasajero por su ID"""
        pasajero = PasajeroRepository.get_by_id(pasajero_id)
        if pasajero:
            pasajero.delete()
            return True
        return False
    
    @staticmethod
    def search(query):
        """Busca pasajeros que coincidan con el criterio de búsqueda"""
        return Pasajero.objects.filter(
            nombre__icontains=query
        ) | Pasajero.objects.filter(
            documento__icontains=query
        ) | Pasajero.objects.filter(
            email__icontains=query
        )
