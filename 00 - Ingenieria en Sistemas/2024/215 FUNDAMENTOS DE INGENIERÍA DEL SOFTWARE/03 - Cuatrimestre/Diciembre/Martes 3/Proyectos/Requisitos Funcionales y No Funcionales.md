---
date: {{date}}
tags: [Tarea, Universidad, {{date:dddd}}]
cssclasses: [tarea, {{date:dddd}}, center-titles, center-images]
author: "youname"
institution: "Universidad TUP"
course: "Nombre del Curso"
professor: "Nombre del Profesor"
---

![[/99 - Meta/attachments/img/Pasted image 20240923160919.png]]

### [215 FUNDAMENTOS DE INGENIERÍA DEL SOFTWARE 25-1](https://moodle.tecplayacar.edu.mx/course/view.php?id=6032 "215 FUNDAMENTOS DE INGENIERÍA DEL SOFTWARE 25-1")
#### [PROF.-MARCO ANTONIO ANGEL GALEANA](https://moodle.tecplayacar.edu.mx/user/view.php?id=8662&course=6032)

![[/99 - Meta/attachments/img/Pasted image 20241001021632.png]]





## **Datos del Estudiante**

- **Equipo**: 
	- Jesús Uriel Santana Oliva
	- Jesús Juarez Martínez
	- Mayte Jiménez González 
	- Cristian Alejandro Hoil Reyes
- Grado : 1 -B
- **Institución**: Tec Playacar
- Fecha: Martes 03 del Diciembre del 2024
- Ubicacion : Playa del Carmen

###### **Actividad
- [ ] Revisión de formato APA.
- [ ] Finalizar la bibliografía.
- [ ] Verificar coherencia en la argumentación.
- [ ] Insertar gráficos relevantes.
- [ ] Requisitos Funcionales y No Funcionales del Proyecto XP

> [!success] Terminada
> Tarea Terminada
> 

---

### Tabla de Requisitos

|**Categoría**|**Requisito**|**Tipo**|
|---|---|---|
|**Funcionales**|El formulario debe permitir a los usuarios enviar comentarios, quejas, sugerencias o calificaciones anónimamente.|Funcional|
||Integrar campos dinámicos como selecciones múltiples y preguntas condicionales.|Funcional|
||Implementar categorías predefinidas (e.g., Producto, Servicio, Infraestructura).|Funcional|
||Generar un identificador único por envío para facilitar la organización interna.|Funcional|
||El formulario debe soportar múltiples idiomas según la localización del cliente.|Funcional|
||Los datos deben almacenarse en una base de datos SQL con relaciones óptimas y encriptación sensible.|Funcional|
||Implementar un sistema de análisis básico para mostrar estadísticas sobre las respuestas en tiempo real.|Funcional|
||Permitir al administrador configurar preguntas y secciones del formulario desde un panel de control.|Funcional|
||Los usuarios deben poder adjuntar imágenes relacionadas con sus comentarios o quejas.|Funcional|
||Los datos recopilados deben ser exportables en varios formatos (CSV, Excel, PDF).|Funcional|
|**No funcionales**|El formulario debe cargar en menos de 1.5 segundos para garantizar fluidez en la experiencia de usuario.|Rendimiento|
||Garantizar la compatibilidad con navegadores modernos y dispositivos móviles.|Compatibilidad|
||Implementar autenticación y autorización para el acceso administrativo.|Seguridad|
||Diseñar la aplicación para que pueda escalar horizontalmente según el aumento de tráfico.|Escalabilidad|
||El sistema debe soportar hasta 10,000 usuarios simultáneamente sin interrupciones.|Rendimiento|
||Aplicar principios de diseño UX/UI modernos para mejorar la accesibilidad.|Usabilidad|
||Los datos almacenados deben cifrarse con estándares como AES-256 para proteger información sensible.|Seguridad|
||Generar registros de auditoría que documenten los cambios realizados en el sistema administrativo.|Auditoría|
||La aplicación debe estar alojada con un tiempo de actividad garantizado del 99.9%.|Confiabilidad|

---


#### **Requisitos Funcionales**

1. **Envío de comentarios anónimos:**  
    El formulario permitirá a los usuarios enviar información valiosa sin revelar su identidad, lo cual fomenta honestidad y participación. Este anonimato será reforzado mediante la ausencia de datos identificables en el formulario.
    
2. **Campos dinámicos y condicionales:**  
    El diseño incluirá lógica dinámica para mostrar u ocultar preguntas basadas en las respuestas anteriores, mejorando la personalización y reduciendo el tiempo necesario para completar el formulario.
    
3. **Categorías predefinidas:**  
    Las categorías facilitarán la clasificación y análisis de los datos, permitiendo a la empresa identificar áreas específicas de mejora.
    
4. **Soporte multilingüe:**  
    Se detectará la ubicación del usuario para ofrecer automáticamente el idioma preferido, lo que aumenta la accesibilidad y la satisfacción del cliente.
    
5. **Base de datos en SQL:**  
    La estructura de la base de datos usará relaciones normalizadas para minimizar la redundancia y garantizar un rendimiento óptimo en las consultas.
    
6. **Panel administrativo:**  
    Se desarrollará un panel seguro para que los administradores gestionen preguntas, exporten datos y visualicen estadísticas.
    
7. **Adjunto de imágenes:**  
    Este componente permitirá a los usuarios proporcionar evidencia visual de problemas, aumentando la calidad de los reportes.
    

#### **Requisitos No Funcionales**

1. **Optimización del tiempo de carga:**  
    Implementaremos prácticas como minimización de recursos, _lazy loading_ y uso de CDN para reducir los tiempos de carga a menos de 1.5 segundos.
    
2. **Compatibilidad amplia:**  
    Usaremos librerías y frameworks modernos que sigan estándares de W3C para garantizar que la aplicación funcione sin problemas en navegadores modernos y dispositivos móviles.
    
3. **Seguridad avanzada:**  
    Los datos se protegerán con encriptación en tránsito (SSL/TLS) y en reposo (AES-256), previniendo accesos no autorizados.
    
4. **Escalabilidad:**  
    Diseñaremos el sistema para soportar escalamiento horizontal, agregando más servidores según sea necesario, y usaremos servicios de balanceo de carga para distribuir el tráfico.
    
5. **Registros de auditoría:**  
    Todas las acciones en el panel administrativo serán registradas con marcas de tiempo, usuario y descripción del cambio, garantizando la trazabilidad y cumplimiento normativo.
    
6. **Diseño centrado en el usuario:**  
    Se aplicarán principios de diseño UX/UI, como contrastes adecuados, fuentes legibles y navegación intuitiva para asegurar que los usuarios interactúen fácilmente con el formulario.
    

---
