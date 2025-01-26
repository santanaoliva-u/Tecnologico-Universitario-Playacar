
# Calificacion  10


![[/99 - Meta/attachments/img/Pasted image 20240923160919.png]]
### [213 FUNDAMENTOS DE REDES 25-1](https://moodle.tecplayacar.edu.mx/course/view.php?id=6030 "213 FUNDAMENTOS DE REDES 25-1")
#### [PROF.-HECTOR LEONEL PEREZ RAMIREZ](https://moodle.tecplayacar.edu.mx/user/view.php?id=9023&course=6030)


![[/99 - Meta/attachments/img/Pasted image 20241001021632.png]]





## **Datos del Estudiante**

---
<center>
  <div style="display: inline-block; padding: 15px; border: 2px solid #ccc; border-radius: 10px; background: transparent; box-shadow: 0 0 15px rgba(255,255,255,0.3); text-align: center; transition: transform 0.3s, box-shadow 0.3s;">
    <img src="https://avatars.githubusercontent.com/u/47199647?v=4" alt="Foto del Estudiante" style="width: 80px; height: 80px; border-radius: 50%; margin-bottom: 10px; border: 2px solid #ccc; transition: transform 0.3s;">
    <div style="font-family: Arial, sans-serif; color: #ccc;">
      <strong style="color: #fff;">Alumno:</strong> Jesús Uriel Santana Oliva<br>
      <strong style="color: #fff;">Curso:</strong> Fundamentos en Redes<br> 
      <strong style="color: #fff;">Grado:</strong> 1 - B
    </div>
  </div>
</center>

<br>


###### **Actividad
- [x] Revisión de formato APA. ✅ 2024-12-11
- [x] Finalizar la bibliografía. ✅ 2024-12-11
- [x] Verificar coherencia en la argumentación. ✅ 2024-12-11
- [x] Insertar gráficos relevantes. ✅ 2024-12-11

![[../../../../../99 - Meta/attachments/img/Pasted image 20241211151330.png]]

### **Definición de Ethernet**

Ethernet es una tecnología de red de área local (LAN, por sus siglas en inglés) que permite la comunicación entre dispositivos a través de un medio de transmisión, como cables de par trenzado, fibra óptica o conexiones inalámbricas. Fue desarrollada en la década de 1970 por **Robert Metcalfe** y desde entonces se ha convertido en uno de los estándares más utilizados para interconectar computadoras, impresoras, servidores y otros dispositivos en redes domésticas, empresariales e industriales.

---

### **Funcionamiento básico de Ethernet**

El funcionamiento de Ethernet se basa en la **transmisión de paquetes de datos**. Estos paquetes contienen información como la dirección MAC de origen y destino, el tamaño del paquete y los datos que se están transfiriendo. A continuación, se detalla el proceso:

1. **Acceso al medio (CSMA/CD)**:
    
    - **CSMA/CD (Acceso Múltiple con Escucha de Portadora y Detección de Colisiones)** permite a los dispositivos verificar si el medio de transmisión está libre antes de enviar datos.
    - Si dos dispositivos envían datos al mismo tiempo, se produce una **colisión**.
    - Cuando se detecta una colisión, ambos dispositivos se detienen y esperan un tiempo aleatorio antes de volver a intentar la transmisión.
2. **División de la información en tramas (frames)**:
    
    - La información que se quiere enviar se fragmenta en **tramas Ethernet**.
    - Cada trama tiene una **cabezera (header)** que incluye la dirección MAC de origen y destino, un campo de control de errores (CRC) y los **datos de la carga útil (payload)**.
3. **Transmisión de la información**:
    
    - La trama se envía a través del cable o medio de transmisión.
    - Los dispositivos de la red (switches y routers) se encargan de recibir la trama, verificarla y reenviarla al destinatario correspondiente.
4. **Recepción y verificación**:
    
    - El dispositivo receptor recibe la trama, verifica la dirección MAC de destino y confirma si está destinada para él.
    - Si los datos llegan con errores (detectados por el campo CRC), se solicita una retransmisión.

---

### **Importancia de Ethernet en la conectividad**

La importancia de Ethernet radica en su **eficiencia, escalabilidad y simplicidad** para conectar dispositivos en redes locales. Algunas de sus principales ventajas incluyen:

1. **Alta velocidad y rendimiento**:
    
    - Ethernet permite **velocidades de transmisión desde 10 Mbps hasta 1 Gbps o más**, facilitando la transferencia de grandes volúmenes de datos.
    - Las versiones más avanzadas, como **Gigabit Ethernet (1000 Mbps)** y **10 Gigabit Ethernet (10 Gbps)**, son esenciales en entornos empresariales y centros de datos.
2. **Fiabilidad y detección de errores**:
    
    - El uso de **CRC (Comprobación de Redundancia Cíclica)** permite la detección de errores en las tramas.
    - La capacidad de retransmitir datos en caso de errores garantiza la **integridad de la información**.
3. **Facilidad de instalación y costo reducido**:
    
    - Es una de las tecnologías más **económicas** y **fáciles de implementar**, ya que no requiere infraestructura costosa.
    - Los **cables de par trenzado (UTP)** son baratos y ampliamente disponibles.
4. **Estandarización universal**:
    
    - Ethernet está definido por el estándar **IEEE 802.3**, lo que garantiza la interoperabilidad entre diferentes dispositivos y fabricantes.
    - Es compatible con una gran variedad de dispositivos, desde computadoras hasta impresoras, cámaras de seguridad y dispositivos IoT.
5. **Conectividad y escalabilidad**:
    
    - Permite la **interconexión de dispositivos** en una red local (LAN) y la conexión a Internet mediante un router.
    - Los switches Ethernet permiten **expandir la red** con facilidad, añadiendo más dispositivos según sea necesario.
6. **Soporte para redes cableadas e inalámbricas**:
    
    - Aunque el Wi-Fi es una alternativa inalámbrica, la conexión Ethernet sigue siendo más **estable y rápida**, especialmente en entornos críticos como servidores, centros de datos y redes industriales.

