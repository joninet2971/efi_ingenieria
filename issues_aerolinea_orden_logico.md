# 🛫 Proyecto: Sistema de Gestión de Aerolínea - Issues Asignadas (Orden Lógico)

## 1. Crear repositorio y configurar proyecto Django

👤 **Responsable**: Integrante B
🏷️ **Etiquetas**: `backend`, `configuración`

📝 **Descripción:**
- Crear repositorio en GitHub
- Crear proyecto Django (`django-admin startproject`)
- Subirlo a GitHub
- Hacer primer commit

🔗 [Documentación Django](https://docs.djangoproject.com/en/stable/intro/tutorial01/)

---

## 2. Crear app principal `vuelos`

👤 **Responsable**: Integrante A
🏷️ **Etiquetas**: `backend`

📝 **Descripción:**
- Crear app Django: `python manage.py startapp vuelos`
- Registrar en `INSTALLED_APPS`
- Subir cambios

🔗 [Documentación Django](https://docs.djangoproject.com/en/stable/ref/applications/)

---

## 3. Diseñar template base con menú y estructura visual

👤 **Responsable**: Integrante B
🏷️ **Etiquetas**: `frontend`, `estructura`, `prioridad-media`

📝 **Descripción:**
👤 **Responsable**: Integrante A

📋 **Checklist**:
- [ ] Crear template base (`base.html`) con bloques de contenido
- [ ] Incluir barra de navegación (Inicio, Vuelos, Reservas, etc.)
- [ ] Aplicar estilos básicos con Bootstrap o CSS
- [ ] Incluir `extends` en las demás plantillas
- [ ] Verificar navegación entre vistas

🔗 [Documentación Django Templates](https://docs.djangoproject.com/en/stable/topics/templates/)


---

## 4. Definir modelos de Avión, Vuelo y Asiento

👤 **Responsable**: Integrante A
🏷️ **Etiquetas**: `backend`, `modelos`

📝 **Descripción:**
- Crear modelo `Avion`
- Crear modelo `Vuelo`
- Crear modelo `Asiento`
- Agregar relaciones FK

🔗 [Modelos Django](https://docs.djangoproject.com/en/stable/topics/db/models/)

---

## 5. Definir modelos de Pasajero, Reserva y Boleto

👤 **Responsable**: Integrante B
🏷️ **Etiquetas**: `backend`, `modelos`

📝 **Descripción:**
- Crear modelo `Pasajero`
- Crear modelo `Reserva`
- Crear modelo `Boleto`
- Validar restricciones de negocio

---

## 6. Crear y aplicar migraciones

👤 **Responsable**: Integrante A
🏷️ **Etiquetas**: `base de datos`

📝 **Descripción:**
- Revisar relaciones
- Ejecutar `makemigrations`
- Ejecutar `migrate`
- Verificar modelos en admin

---

## 7. Configurar sistema de login/logout

👤 **Responsable**: Integrante B
🏷️ **Etiquetas**: `autenticación`, `frontend`

📝 **Descripción:**
- Implementar login/logout
- Usar vistas genéricas o personalizadas

---

## 8. Crear sistema de roles para usuarios

👤 **Responsable**: Integrante A
🏷️ **Etiquetas**: `autenticación`

📝 **Descripción:**
- Agregar campo `rol` a modelo de usuario
- Limitar vistas según rol (admin/público)

---

## 9. CRUD completo de Vuelos (admin y público)

👤 **Responsable**: Integrante B
🏷️ **Etiquetas**: `backend`, `frontend`

📝 **Descripción:**
- Vista admin para crear/editar vuelos
- Vista pública para ver vuelos
- Validaciones de fechas

---

## 10. CRUD de Aviones con layout de asientos

👤 **Responsable**: Integrante A
🏷️ **Etiquetas**: `backend`, `frontend`

📝 **Descripción:**
- Crear formulario para registrar aviones
- Implementar layout visual de asientos (filas y columnas)

---

## 11. Gestión de Pasajeros y su historial de vuelos

👤 **Responsable**: Integrante B
🏷️ **Etiquetas**: `backend`, `frontend`

📝 **Descripción:**
- Registro de pasajeros
- Mostrar historial por pasajero

---

## 12. Sistema de Reservas con selección de asiento

👤 **Responsable**: Integrante A
🏷️ **Etiquetas**: `backend`, `frontend`

📝 **Descripción:**
- Mostrar asientos disponibles
- Marcar como reservado/ocupado
- Confirmar y guardar reserva

---

## 13. Generación automática de boletos electrónicos

👤 **Responsable**: Integrante B
🏷️ **Etiquetas**: `backend`

📝 **Descripción:**
- Generar boleto con código de barras
- Asociar boleto a reserva

🔗 [python-barcode](https://pypi.org/project/python-barcode/)

---

## 14. Reporte de pasajeros por vuelo

👤 **Responsable**: Integrante A
🏷️ **Etiquetas**: `reporte`

📝 **Descripción:**
- Listar pasajeros de un vuelo
- Exportar a PDF (opcional)

---

## 15. Validaciones en frontend y backend

👤 **Responsable**: Integrante B
🏷️ **Etiquetas**: `validaciones`

📝 **Descripción:**
- Validar documentos únicos
- Validar fechas lógicas
- Validar solo una reserva por pasajero por vuelo

---

## 16. Implementar pruebas unitarias básicas

👤 **Responsable**: Integrante A
🏷️ **Etiquetas**: `pruebas`

📝 **Descripción:**
- Pruebas para modelos
- Pruebas para vistas (opcional)

---

## 17. Documentar el proyecto

👤 **Responsable**: Integrante B
🏷️ **Etiquetas**: `documentación`

📝 **Descripción:**
- Crear README con instrucciones
- Documentar modelos y relaciones
- Instrucciones para pruebas

---

## 18. Deploy local y revisión final

👤 **Responsable**: Integrante A
🚨 **Alta Prioridad**

🏷️ **Etiquetas**: `prioridad-alta`

📝 **Descripción:**
- Probar flujo completo
- Corregir bugs
- Confirmar entregables

---

