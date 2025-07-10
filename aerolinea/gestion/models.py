from django.db import models

class Avion(models.Model):
    modelo = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    filas = models.IntegerField()
    columnas = models.IntegerField()

    def __str__(self):
        return f"{self.modelo} ({self.capacidad} pasajeros)"

class Vuelo(models.Model):
    avion = models.ForeignKey(Avion, on_delete=models.CASCADE, related_name='vuelos')
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    fecha_salida = models.DateTimeField()
    fecha_llegada = models.DateTimeField()
    duracion = models.IntegerField()
    estado = models.CharField(max_length=50)
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Vuelo {self.id} - {self.origen} a {self.destino}"

class Pasajero(models.Model):
    nombre = models.CharField(max_length=100)
    documento = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    tipo_documento = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.documento})"

class Asiento(models.Model):
    avion = models.ForeignKey(Avion, on_delete=models.CASCADE, related_name='asientos')
    numero = models.CharField(max_length=10)
    fila = models.IntegerField()
    columna = models.IntegerField()
    tipo = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"Asiento {self.numero} - Avión {self.avion.modelo}"

class Reserva(models.Model):
    vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE, related_name='reservas')
    pasajero = models.ForeignKey(Pasajero, on_delete=models.CASCADE, related_name='reservas')
    asiento = models.OneToOneField(Asiento, on_delete=models.SET_NULL, blank=True, null=True)
    estado = models.CharField(max_length=50)
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    codigo_reserva = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"Reserva {self.codigo_reserva} - Vuelo {self.vuelo.id}"

class Boleto(models.Model):
    reserva = models.OneToOneField(Reserva, on_delete=models.CASCADE, related_name='boleto')
    codigo_barra = models.CharField(max_length=100, unique=True)
    fecha_emision = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return f"Boleto {self.codigo_barra} - Reserva {self.reserva.codigo_reserva}"

