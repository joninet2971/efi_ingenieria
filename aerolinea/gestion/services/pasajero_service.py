from gestion.repositories.pasajero_repository import PasajeroRepository

class PasajeroService:
    """
    Servicio para la entidad Pasajero.
    Implementa la lógica de negocio relacionada con los pasajeros.
    """
    
    def __init__(self):
        self.repository = PasajeroRepository()
    
    def get_all_pasajeros(self):
        """Obtiene todos los pasajeros"""
        return PasajeroRepository.get_all()
    
    def get_pasajero_by_id(self, pasajero_id):
        """Obtiene un pasajero por su ID"""
        return PasajeroRepository.get_by_id(pasajero_id)
    
    def create_pasajero(self, data):
        """
        Crea un nuevo pasajero después de validar los datos
        
        Args:
            data (dict): Datos del pasajero a crear
            
        Returns:
            tuple: (pasajero, error_message)
        """
        # Validar que los campos obligatorios están presentes
        if not all(key in data for key in ['nombre', 'documento', 'email']):
            return None, "Los campos nombre, documento y email son obligatorios"
        
        # Validar que no existe otro pasajero con el mismo documento
        existing_pasajero = PasajeroRepository.get_by_documento(data['documento'])
        if existing_pasajero:
            return None, f"Ya existe un pasajero con el documento {data['documento']}"
        
        # Si todo está bien, crear el pasajero
        try:
            pasajero = PasajeroRepository.create(data)
            return pasajero, None
        except Exception as e:
            return None, f"Error al crear el pasajero: {str(e)}"
    
    def update_pasajero(self, pasajero_id, data):
        """
        Actualiza un pasajero existente después de validar los datos
        
        Args:
            pasajero_id (int): ID del pasajero a actualizar
            data (dict): Datos actualizados del pasajero
            
        Returns:
            tuple: (pasajero, error_message)
        """
        # Validar que el pasajero existe
        pasajero = PasajeroRepository.get_by_id(pasajero_id)
        if not pasajero:
            return None, f"No se encontró ningún pasajero con ID {pasajero_id}"
        
        # Validar que si se cambia el documento, no exista otro pasajero con ese documento
        if 'documento' in data and data['documento'] != pasajero.documento:
            existing_pasajero = PasajeroRepository.get_by_documento(data['documento'])
            if existing_pasajero and existing_pasajero.id != int(pasajero_id):
                return None, f"Ya existe un pasajero con el documento {data['documento']}"
        
        # Si todo está bien, actualizar el pasajero
        try:
            updated_pasajero = PasajeroRepository.update(pasajero_id, data)
            return updated_pasajero, None
        except Exception as e:
            return None, f"Error al actualizar el pasajero: {str(e)}"
    
    def delete_pasajero(self, pasajero_id):
        """
        Elimina un pasajero existente
        
        Args:
            pasajero_id (int): ID del pasajero a eliminar
            
        Returns:
            tuple: (success, error_message)
        """
        # Validar que el pasajero existe
        pasajero = PasajeroRepository.get_by_id(pasajero_id)
        if not pasajero:
            return False, f"No se encontró ningún pasajero con ID {pasajero_id}"
        
        # Aquí se podría agregar lógica para validar si el pasajero tiene reservas activas
        
        # Si todo está bien, eliminar el pasajero
        try:
            success = PasajeroRepository.delete(pasajero_id)
            if success:
                return True, None
            return False, "Error al eliminar el pasajero"
        except Exception as e:
            return False, f"Error al eliminar el pasajero: {str(e)}"
    
    def search_pasajeros(self, query):
        """Busca pasajeros que coincidan con el criterio de búsqueda"""
        return PasajeroRepository.search(query)
