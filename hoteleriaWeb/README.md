
# ESTANCIAS DEL SOL - APP WEB.

Aquí se explicará qué es lo que cada vista hace y como afectan a la experiencia del usuario.


## Vistas
- Base
- Inicio
- Informacion del hotel
- Habitaciones
- Reservar
- Buscar mi reserva
- Mi reserva
- Error




## Explicación de las vistas:

- Base: Archivo base del diseño de la Web.  Contiene todo el código HTML que se repite en las vistas, como por ejemplo el header, el footer, y los links de los archivos 'js' y 'css'.
    - Header: Contiene botones para redireccionarnos a 'Inicio', 'Ver mi reserva' e 'Informacion hoteles'.






#### ¿Por qué creamos un archivo 'Base'?

Este archivo lo creamos por una cuestión de evitar repetir código en todas las vistas, y de esta manera nos ahorramos muchísimo tiempo y espacio, además de que nos facilita la lectura de los archivos en caso de que queramos cambiar algo.



- Inicio: Página principal del proyecto. En esta vista encontraremos:

    - Formulario para reservar: Aqui el usuario podrá ingresar en qué ciudad y entre qué fechas quiere reservar una habitación, siendo redireccionado a "Habitaciones", donde encontrará las habitaciones disponibles que cumplan sus requisitos. En caso de no elegir ninguna opción, al hacer click en "Reserva Online", se mostrarán TODAS las habitaciones disponibles de TODOS los hoteles.
    
    - Sucursales: En este apartado, el usuario podrá ver las locaciones que nuestro hotel tiene disponibles, junto a una pequeña descripción. Además, tiene la opción de 'Más información', donde se redireccionará a 'Información del hotel', y podrá ver datos más específicos del hotel, como ser la dirección y los servicios disponibles.

- Información del hotel: Aquí se enseña más a detalle la información acerca de la sucursal seleccionada: Los servicios disponibles, dirección y la descripción del hotel en cuestión. Si se busca un hotel inexistente, no se mostrará nada por pantalla. Si se accede desde el 'Header' ,  esta vista nos enseñará la información de TODOS los hoteles disponibles.
- Habitaciones: Esta vista nos muestra las habitaciones disponibles de los distintos hoteles, mostrando el tipo, cantidad de personas, servicios disponibles y precio por noche. Además, cuenta con un buscador que filtra las habitaciones por fecha de disponibilidad, sucursal, cantidad de personas y por tipo. Cada habitación tiene un botón que nos lleva a 'reservar'.

- Reservar: Esta vista, nos enseña por pantalla toda la información de la habitación que el usuario ha seleccionado para reservar, el periodo de fechas seleccionado, y el precio final que pagaría por la estancia (precio por noche multiplicado por cantidad de noches).  Además, cuenta con un formulario en el cual el usuario deberá ingresar su apellido, y finalmente tendrá el botón para confirmar la reserva.


- Ver mi reserva: Esta vista nos presenta un formulario en el cual se solicita el ID de la reserva(numérico), y el apellido de quien haya hecho la reserva. En caso de que no exista ninguna reserva con los campos ingresados, se le informará al  usuario en pantalla. Si son correctos los datos, se redireccionará al usuario a 'mi_reserva'.

- ver_mis_reservas.html: En esta vista se muestra toda la información de la reserva que el usuario ha hecho (ID de la reserva, nombre del titular, fecha de Check-in y Check-Out, numero y tipo de habitación, hotel, servicios disponibles, servicios contratados), y además tiene la opción de 'cancelar reserva', en caso de que se la quiera dar de baja, y quedando disponible nuevamente la habitación previamente reservada.

- error.html: Esta vista muestra por pantalla, en caso de que exista, un error en la página (404, 500, etc).