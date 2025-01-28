# Curso Profesional de Git

Git es una herramienta esencial en el desarrollo de software moderno y la colaboración en equipos. Diseñado por Linus Torvalds en 2005, Git permite gestionar versiones de código de manera eficiente, garantizar la integridad de los datos y facilitar flujos de trabajo distribuidos. Este curso tiene como objetivo enseñarte desde los conceptos básicos hasta las funcionalidades avanzadas de Git, explicándolo de manera profesional y detallada.

# Temario del Curso

### 1. Introducción a Git

- ¿Qué es Git?
    
    - Sistema de control de versiones distribuido.
        
    - Diseñado para desarrolladores, pero aplicable a diversas disciplinas.
        
- Beneficios principales:
    
    - Ahorro de tiempo en colaboraciones.
        
    - Integridad de los datos.
        
    - Flexibilidad en flujos de trabajo.
        
- Historia de Git:
    
    - Creado por Linus Torvalds en 2005.
        
    - Licenciado bajo GPL v2.0.
        

[**Ver video de introducción**](https://backtrackacademy.com/video/01-introduccion-f18baaac-4bc7-4f84-978b-636d4bf77239)


### 2. Instalación de Git

#### Instalación en sistemas basados en Linux (ejemplo con Fedora):

1. Actualizar el sistema:
    
    ```
    sudo dnf update
    ```
    
2. Instalar Git:
    
    ```
    sudo dnf install git
    ```
    
3. Verificar la instalación:
    
    ```
    git --version
    ```
    

#### Instalación en otros sistemas operativos:

- Windows: Descargar el instalador desde [git-scm.com](https://git-scm.com/).
- macOS: Usar Homebrew: 
    ```
    brew install git
    ```
#### Configuración inicial:

- Configurar nombre de usuario: 
    ```
    git config --global user.name "Tu Nombre"
    ```
- Configurar correo electrónico:
    ```
    git config --global user.email "tuemail@dominio.com"
    ```

---

### 3. Conceptos básicos de Git

#### ¿Cómo funciona Git?

- Git rastrea cambios en los archivos y permite crear puntos de referencia llamados _commits_.
    
- Usa un modelo distribuido: todos los usuarios tienen una copia completa del repositorio.
    

#### Flujo de trabajo básico:

1. Crear un nuevo repositorio:
    
    ```
    git init
    ```
    
2. Agregar archivos al área de preparación:
    
    ```
    git add archivo.txt
    ```
    
3. Crear un commit:
    
    ```
    git commit -m "Mensaje del commit"
    ```
   
4. Ver el estado del repositorio:
   
    ```
    git status
    ```

#### Repositorios remotos:

- Conectar a un repositorio remoto en GitHub:
   
    ```
    git remote add origin https://github.com/usuario/repositorio.git
    ```
   
- Subir cambios al remoto:
   
    ```
    git push -u origin main
    ```
   

[**Ver video: Los repositorios en Git**](https://backtrackacademy.com/video/03-los-repositorios-en-git)

---

### 4. Autenticación en GitHub con SSH

#### Configurar una clave SSH:

1. Crear el directorio:
    
    ```
    mkdir ~/.ssh
    cd ~/.ssh
    ```
    
2. Generar la clave SSH:
    
    ```
    ssh-keygen -t rsa -b 4096 -C "tuemail@dominio.com"
    ```
    
3. Mostrar la clave pública para agregarla en GitHub:
    
    ```
    cat ~/.ssh/id_rsa.pub
    ```
    

#### Agregar la clave en GitHub:

1. Acceder a tu cuenta en [GitHub](https://github.com).
    
2. Ir a **Settings > SSH and GPG keys**.
    
3. Hacer clic en **New SSH key** y pegar la clave generada.
    

---

### 5. Trabajo en equipo con Git

#### Flujos de trabajo distribuidos:

- Trabajar en ramas (branches):
    
    ```
    git branch nueva-rama
    git checkout nueva-rama
    ```
    
- Fusionar ramas:
    
    ```
    git merge nueva-rama
    ```
    
- Resolver conflictos:
    
    - Git marca las diferencias entre versiones y permite elegir qué cambios conservar.
        

#### Buenas prácticas:

- Escribir mensajes de commit descriptivos.
    
- Actualizar frecuentemente desde el repositorio remoto:
    
    ```
    git pull origin main
    ```
    

---

### Conclusión

Git es una herramienta poderosa que facilita la colaboración en proyectos, garantiza la integridad de los datos y permite trabajar en equipo de manera eficiente. Dominar Git te abrirá puertas en el ámbito profesional y potenciará tus habilidades como desarrollador.

---

### Referencias

- [Documentación oficial de Git](https://git-scm.com/doc)
    
- [Backtrack Academy: Curso de Git](https://backtrackacademy.com)