**PROYECTO DE INGENIERÍA DE REQUISITOS: CLASES DE COMPUTACIÓN**




**ÍNDICE**

1. Introducción
2. Objetivos del Proyecto
    1. Objetivo General
    2. Objetivos Específicos
3. Alcance del Proyecto
4. Análisis de Requisitos
    1. Requisitos Funcionales
    2. Requisitos No Funcionales
5. Diseño del Sistema
    1. Arquitectura del Sistema
    2. Diagrama de Casos de Uso
    3. Especificaciones Técnicas
6. Plan de Implementación
    1. Cronograma de Desarrollo
    2. Tecnologías Utilizadas
    3. Desarrollo de Módulos
7. Plan de Validación y Pruebas
    1. Estrategias de Pruebas
    2. Criterios de Aceptación
8. Plan de Mantenimiento y Soporte
9. Conclusiones y Recomendaciones
10. Referencias

---

### 1. **Introducción**

En un mundo cada vez más digitalizado, la educación en tecnología y computación se ha convertido en una necesidad fundamental. Este proyecto se centra en diseñar, desarrollar e implementar un sistema integral que permita ofrecer clases de computación tanto en formato presencial como virtual.

El objetivo es proporcionar un entorno de aprendizaje interactivo, escalable y accesible que cumpla con los principios establecidos por la ingeniería de requisitos, garantizando la satisfacción de las necesidades técnicas y pedagógicas de los usuarios finales.

---

### 2. **Objetivos del Proyecto**

#### 2.1 Objetivo General

Diseñar e implementar un sistema educativo profesional para impartir clases de computación, cumpliendo con los estándares de la ingeniería de requisitos y asegurando la calidad educativa.

#### 2.2 Objetivos Específicos

- Realizar un análisis detallado de los requisitos funcionales y no funcionales del sistema.
- Diseñar un entorno de aprendizaje accesible y adaptable.
- Garantizar la seguridad de la información y la experiencia del usuario mediante estándares técnicos reconocidos.
- Implementar herramientas tecnológicas avanzadas para la gestión y evaluación de clases.
- Validar la funcionalidad y usabilidad del sistema a través de pruebas rigurosas.

---

### 3. **Alcance del Proyecto**

Este proyecto incluye:

- **Diseño e implementación del sistema**: Desarrollo de una plataforma digital que permita la gestión de clases, inscripciones, evaluaciones y comunicación entre estudiantes y profesores.
- **Contenido educativo estructurado**: Creación de materiales de aprendizaje organizados en módulos progresivos.
- **Capacitación**: Formación inicial para profesores y administradores en el uso del sistema.
- **Soporte continuo**: Implementación de un plan de mantenimiento y actualización del sistema.

Limitaciones:

- El sistema estará inicialmente disponible en español y para usuarios en América Latina.
- No se desarrollará hardware asociado al proyecto.

---

### 4. **Análisis de Requisitos**

#### 4.1 Requisitos Funcionales

1. **Gestión de usuarios**:
    - Registro de estudiantes y profesores con diferentes niveles de acceso.
    - Recuperación de contraseñas y administración de perfiles.
2. **Administración de clases**:
    - Creación, programación y asignación de clases por parte de los administradores.
    - Gestión de inscripciones de estudiantes.
3. **Contenido educativo**:
    - Acceso a materiales didácticos como tutoriales, ejercicios prácticos y videos.
    - Integración de evaluaciones automatizadas con retroalimentación personalizada.
4. **Sistema de evaluación**:
    - Cuestionarios automáticos y reportes de progreso en tiempo real.
    - Estadísticas de rendimiento de estudiantes y profesores.

#### 4.2 Requisitos No Funcionales

1. **Rendimiento**:
    - Capacidad de respuesta en menos de 2 segundos para operaciones críticas.
    - Soporte para hasta 1000 usuarios simultáneos.
2. **Seguridad**:
    - Cumplimiento de estándares como ISO 27001 para la protección de datos.
    - Encriptación de datos sensibles con algoritmos AES-256.
3. **Usabilidad**:
    - Interfaz intuitiva diseñada con principios de UX/UI.
    - Compatibilidad con navegadores modernos y dispositivos móviles.
4. **Escalabilidad**:
    - Capacidad de ampliación modular para futuras funcionalidades.
5. **Disponibilidad**:
    - Garantía de disponibilidad del 99.9% mediante el uso de infraestructura en la nube.

---

### 5. **Diseño del Sistema**

#### 5.1 Arquitectura del Sistema

El sistema se basará en una arquitectura distribuida con los siguientes componentes clave:

- **Frontend**: Diseñado con React.js para una interfaz de usuario interactiva.
- **Backend**: Implementado con Node.js y Express para manejar la lógica del negocio.
- **Base de datos**: MongoDB, optimizada para almacenamiento de datos estructurados y no estructurados.
- **Infraestructura**: Desplegado en AWS con balanceo de carga y escalado automático.

#### 5.2 Diagrama de Casos de Uso

Se creará un diagrama detallado que ilustre las interacciones entre los actores (estudiantes, profesores, administradores) y las funcionalidades del sistema.

#### 5.3 Especificaciones Técnicas

- **Librerías y Frameworks**: React.js, Bootstrap, Express.js, Mongoose.
- **APIs**: Integración con servicios de correo electrónico y notificación push.
- **Seguridad**: Implementación de autenticación OAuth 2.0 y JWT para sesión segura.

---

### 6. **Plan de Implementación**

#### 6.1 Cronograma de Desarrollo

1. **Mes 1**: Recopilación de requisitos y diseño inicial.
2. **Mes 2**: Desarrollo del frontend y backend.
3. **Mes 3**: Integración de módulos y pruebas iniciales.
4. **Mes 4**: Validación, capacitación y lanzamiento del sistema.

#### 6.2 Tecnologías Utilizadas

- **Frontend**: React.js, CSS3, HTML5
- **Backend**: Node.js, Express
- **Base de datos**: MongoDB
- **DevOps**: AWS, Docker, Jenkins

#### 6.3 Desarrollo de Módulos

1. **Gestión de Usuarios**: Registro, inicio de sesión y perfiles.
2. **Módulo Educativo**: Contenidos y evaluaciones.
3. **Analítica**: Reportes de rendimiento.

---

### 7. **Plan de Validación y Pruebas**

#### 7.1 Estrategias de Pruebas

- **Pruebas Unitarias**: Validar funcionalidad individual de los componentes.
    
- **Pruebas de Integración**: Comprobar la interoperabilidad entre módulos.
    
- **Pruebas de Carga**: Simulación de 1000 usuarios concurrentes.
    

#### 7.2 Criterios de Aceptación

- **Cumplimiento de Requisitos**: El sistema debe cumplir todos los requisitos funcionales y no funcionales definidos en la etapa de análisis.
    
- **Pruebas de Usuario**: Validación por parte de un grupo piloto de estudiantes y profesores, con un índice de satisfacción mínimo del 90%.
    
- **Estabilidad**: El sistema debe mantenerse estable durante pruebas de carga y condiciones adversas.
    
- **Interfaz Intuitiva**: La experiencia de usuario debe alinearse con los principios de usabilidad definidos.
    

---

### 8. **Plan de Mantenimiento y Soporte**

- **Actualizaciones Periódicas**: Revisión trimestral para incorporar mejoras y nuevas funcionalidades.
    
- **Monitorización Activa**: Uso de herramientas como New Relic para identificar y resolver problemas de rendimiento.
    
- **Soporte al Usuario**: Implementación de un sistema de ticketing para resolver consultas y problemas.
    
- **Documentación**: Manuales de usuario y guías de referencia actualizados continuamente.
    

---

### 9. **Conclusiones y Recomendaciones**

Este proyecto establece una solución integral para impartir clases de computación, alineada con los principios de la ingeniería de requisitos. Se recomienda mantener un enfoque centrado en el usuario y garantizar la adaptabilidad del sistema para futuras demandas tecnológicas y pedagógicas.

---

### 10. **Referencias**

1. Sommerville, I. (2015). _Software Engineering_ (10th Edition). Pearson.
    
2. Pressman, R. S. (2020). _Software Engineering: A Practitioner's Approach_ (8th Edition). McGraw-Hill.
    
3. ISO/IEC 25010:2011. Systems and Software Engineering — Systems and Software Quality Requirements and Evaluation (SQuaRE).