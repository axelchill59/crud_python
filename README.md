# crud_python
CRUD Python/TKinter/SQLite3

Este es un proyecto 'CRUD' orientado a una institución educativa. Permite un inicio de sesión seguro, con una interfaz multi-rol que permite:
    - Al iniciar como alumno: Inscribirse a mesas examinadoras, y modificar la contraseña (con parámetros seguros).
    - Al iniciar como admin: Permite crear Carreras, y sus respectivas materias. Añadir alumnos, e inscribirlos en una carrera y una materia. Además permite crear mesas examinadoras, a las cuales los alumnos con la materia regularizada podrán inscribirse.

La base de datos incluye:
    - Control de redundancia.
    - Datos validados.
    - Validación de fecha.
    - Información detallada de los campos.

La interfaz está creada con Tkinter, utilizando la librería 'ttk' para un estilo moderno.
La base de datos es controlada por la librería SQLite3.

Este proyecto fué creado en Microsoft Windows 11, utilizando Python3.13.1 y Sublime Text 3.

Axel Nicolas Reich, Argentina. Todos los derechos reservados. 2024-