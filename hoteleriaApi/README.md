
# API hoteles


## Descripción

API que permite la busqueda de hoteles, realizar reservas, obtener detalles sobre habitaciones y servicios.


## Características
- **Busqueda :** Permite la busqueda de hoteles, habitaciones y servicios.

- **Reserva :** Permite la reserva de servicios y habitaciones.



## Endpoints
**GET :**

- **/api/hoteles/ :** Devuelve todos los hoteles. 
- **/api/hoteles/{id} :** Devuelve el hotel relacionado al id.
- **/api/hoteles/{region} :** Devuelve los hoteles en pertenecientes a una region.
- **/api/hoteles/regiones :** Devuelve todas las regiones que tienen hoteles.
- **/api/habitaciones/ :** Devuelve todas las habitaciones.
- **/api/habitaciones/{id_hotel} :** Devuelve todas las habitaciones pertenecientes a un hotel.
- **/api/habitacion/{id} :** Devuelve una habitacion en especifico.
- **/api/habitaciones/{tipo} :** Devuelve las habitaciones de un mismo tipo.
- **/api/habitaciones/tipos/ :** Devuelve todos los tipos de habitaciones.
- **/api/habitacion/{tipo}/{region} :** Devuelve todas las habitaciones con el tipo y region especificado.
- **/api/servicios/ :** Deveulve todos los servicios.
- **/api/servicios/{id} :** Devuelve el servicio relacionado al id.
- **/api/servicios/hotel/{id_hotel} :** Devuelve los servicios de pago que tiene un hotel.
- **/api/servicios/hotel/{id_hotel}/{id_servicio} :** Devuelve el servicio relacionado al hotel, usado mas para obtener el precio de un servicio en especifico.
- **/api/servicios/habitacion/{id_habitacion} :** Devuelve los servicios incluidos en una habitacion.
- **/api/reserva/{id}/{cliente}/ :** Devuelve la informacion de reserva de un cliente.
- **/api/reserva/servicios/{id_reserva} :** Devuelve los servicios reservados por el cliente.

**POST :**

- **/api/reserva/ :** Realiza la reserva de un cliente (JSON necesario).

- **/api/servicio/{id_reserva}/{id_servicio} :** Realiza la reserva de un servicio para un cliente existente.

**PUT :**

- **/api/reserva/{id}/{cliente}/ :** Cancela una reserva y sus servicios.

**DELETE :** 

- **/api/reserva/servicios/{id_reserva} :** Elimina los servicios reservados de una reserva.

- **/api/reserva/servicio/{id_reserva}/{id_servicio} :** Elimina un servicio reservado de una reserva.
## Archivos

**app.py**

- Define los endpoints, procesa las solicitudes HTTP y gestiona los errores.

**hoteles.py**
- Menaja las consultas (querys), la conexion con la base de datos y la devolucion de los resultados.

**hoteles.sql**

- Se encarga de definir la estructura de las tablas y asegurar que los datos se puedan almacenar de manera eficiente. 
## Requerimientos

blinker==1.9.0

certifi==2024.8.30

charset-normalizer==3.4.0

click==8.1.7

Flask==3.1.0

greenlet==3.1.1

idna==3.10

itsdangerous==2.2.0

Jinja2==3.1.4

MarkupSafe==3.0.2

mysql-connector-python==9.1.0

PyMySQL==1.1.1

python-dotenv==1.0.1

requests==2.32.3

SQLAlchemy==2.0.36

typing_extensions==4.12.2

urllib3==2.2.3

Werkzeug==3.1.3
