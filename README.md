# Estancias del Sol

Este proyecto fue desarrollado por alumnos de la Facultad de Ingeniería de Buenos Aires, en la materia de Introducción al Desarrollo de Software. El objetivo principal es diseñar un software para una cadena de hoteles en Argentina. El sistema incluye un sitio web que ofrece información detallada sobre las distintas ubicaciones, permite consultar la disponibilidad de habitaciones según las fechas seleccionadas y brinda la opción de realizar reservas.

## Diagrama de arquitectura

```mermaid
architecture-beta
    group frontend[frontend]
    group backend[backend]
    
    service serverFrontend(server) in frontend
    service serverBackend(server) in backend
    service db(database) in backend
    service user[user]
    
    user:B --> T:serverFrontend
    serverFrontend:R --> L:serverBackend
    serverBackend:R --> L:db
```

## Tecnologías usadas

- Flask
- HTML
- CSS
- Javascript
- MySQL
