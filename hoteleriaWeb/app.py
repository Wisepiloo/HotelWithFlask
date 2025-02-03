from flask import Flask, render_template, request, redirect, url_for
import requests
from datetime import datetime
app = Flask(__name__)

API_URL = "http://backend:3648/api"


def get_data(endpoint):
    try:
        response = requests.get(API_URL + endpoint)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        data = []

    return data


@app.route("/")
def index():
    hotels = get_data("/hoteles")[:3]
    regions = get_data("/hoteles/regiones")

    return render_template("index.html", hotels=hotels, regions=regions)


@app.route("/mi_reserva")
def mi_reserva():
    return render_template("login_mis_reservas.html", error = " ")


@app.route("/informacion_reserva", methods = ['POST' , 'GET'])
def informacion_reserva():
    if request.method == "POST":
        cancelar_apellido_cliente = request.form.get("cancelar_apellido_cliente")
        cancelar_id_reserva = request.form.get("cancelar_id_reserva")
        
        if cancelar_id_reserva is not None and cancelar_apellido_cliente is not None:
            requests.put(API_URL + f'/reserva/{cancelar_id_reserva}/{cancelar_apellido_cliente}')
            return redirect(url_for("mi_reserva"))

        id_reserva = request.form.get("nreserva")
        apellido_cliente = request.form.get("acliente")
        if not id_reserva.isdigit():
             return render_template("login_mis_reservas.html", error = "El ID de la reserva solo puede tener numeros.")
        datos = obtener_datos_reserva(id_reserva,apellido_cliente)
        
        if len(datos) == 0:
            return render_template("login_mis_reservas.html", error = "Hubo un error en la busqueda. Intente nuevamente.")
        else:  
            return render_template("ver_mis_reservas.html", reserva = datos[0], servicios_aparte = datos[1], servicios_incluidos = datos[2],habitacion = datos[3], hotel = datos[4], apellido_cliente = apellido_cliente)
    
    return redirect(url_for("mi_reserva"))
    
def reserva_realizada(id_reserva,apellido_cliente):
    datos = obtener_datos_reserva(id_reserva,apellido_cliente)
    return render_template("ver_mis_reservas.html", reserva = datos[0], servicios_aparte = datos[1], servicios_incluidos = datos[2],habitacion = datos[3], hotel = datos[4], apellido_cliente = apellido_cliente)


def obtener_datos_reserva(id_reserva,apellido_cliente):
        sa = []
        try:
            response_reserva = requests.get(API_URL + f"/reserva/{id_reserva}/{apellido_cliente}")
            response_reserva.raise_for_status()
            reserva = response_reserva.json()
            servicios_reserva = get_data(f"/reserva/servicios/{id_reserva}")

            for s in servicios_reserva:
                sr = get_data(f"/servicios/{s['id_servicio']}")
                sa.append(sr[0]['servicio'])

            habitacion = get_data(f"/habitacion/{reserva[0]['id_habitacion']}")

            servicios_incluidos = get_data(f"/servicios/habitacion/{habitacion[0]['id']}")

            id_hotel = habitacion[0]['id_hotel']
            hotel = get_data(f"/hoteles/{id_hotel}")
        except requests.exceptions.RequestException as e:
            return []
        return [ reserva, sa, servicios_incluidos, habitacion, hotel ]


@app.route("/hoteles/<id_hotel>")
def hoteles(id_hotel):
    if not id_hotel.isdigit():
        return render_template("info_hotel.html", params = [], servicios = [])
    id_hotel = int(id_hotel)
    try:
            #------------------INFORMACION DE TODOS LOS HOTELES------------------
            if id_hotel == 0:

                hoteles = get_data("/hoteles")

                id_hoteles = [hotel["id"] for hotel in hoteles]
                servicios = []
                
                for id in id_hoteles:
                    servicios_hotel = get_data(f"/servicios/hotel/{id}")
                    for servicio in servicios_hotel:
                        servicio["id_hotel"] = id
                        servicios.append(servicio)
            else:
            #----------------------INFORMACION DE UN SOLO HOTEL----------------------
                hoteles = get_data(f"/hoteles/{id_hotel}")
                
                servicios_hotel = get_data(f"/servicios/hotel/{id_hotel}")
                servicios = []
                for servicio in servicios_hotel:
                    servicio["id_hotel"] = id_hotel
                    servicios.append(servicio)

    except requests.exceptions.RequestException as e:
        params = []
        servicios = []
    params = []
    for hotel in hoteles:
            if hotel not in params:
                params.append(hotel)

    return render_template("info_hotel.html", params = params, servicios = servicios)


@app.route("/habitaciones", methods=["GET", "POST"])
def habitaciones():
    rooms = []
    meta_region = ""
    meta_start_date = ""
    meta_end_date = ""
    meta_room_type = ""

    if request.method == "POST":
        query_string = ""
        query = []
        if request.form.get("region") is not None:
            meta_region = request.form.get("region")
            query.append(f"region={meta_region}")

        if request.form.get("dates") is not None:
            dates = request.form.get("dates").split(" a ")
            meta_start_date = dates[0]
            meta_end_date = dates[1]
            query.append(f"llegada={meta_start_date}")
            query.append(f"salida={meta_end_date}")

        if request.form.get("type") is not None:
            meta_room_type = request.form.get("type")
            query.append(f"tipo={meta_room_type}")

        if len(query) > 0:
            query_string = "?" + "&".join(query)

        rooms = get_data("/habitaciones/disponibles" + query_string)

        for room in rooms:
            room["servicios"] = get_data("/servicios/habitacion/" + str(room["id"]))

    regions = get_data("/hoteles/regiones")
    room_types = get_data("/habitaciones/tipos/")

    return render_template(
        "habitaciones.html",
        regions=regions,
        room_types=room_types,
        rooms=rooms,
        meta_region=meta_region,
        meta_start_date=meta_start_date,
        meta_end_date=meta_end_date,
        meta_room_type=meta_room_type
    )

@app.route('/reservar/<id_room>/<start_date>/<end_date>')
def reservar(id_room,start_date, end_date):
        room = get_data("/habitacion/"+str(id_room) )
        servicios = get_data("/servicios/habitacion/"+str(id_room) )
        hotel = get_data(f"/hoteles/{room[0]["id_hotel"]}")
        region = hotel[0]["region"]
        fecha_inicio= datetime.strptime(start_date, '%Y-%m-%d')
        fecha_final= datetime.strptime(end_date, '%Y-%m-%d')
        diference = (fecha_final - fecha_inicio).days 
        return render_template("reservas.html", room=room[0] , region=region, start_date=start_date, end_date=end_date, diference_days=diference, servicios=servicios )

@app.route('/confirmReservation', methods=["GET","POST"]  )
def confirmReservation():
        if request.method == "POST":
            lastName = request.form.get("fsecondName")
            startDate = request.form.get("fstartDate")
            endDate = request.form.get("fendDate")
            room = request.form.get("fdataroom")
            price = request.form.get("fpriceFinal")

            json_data ={
                "id_habitacion": room , 
                "llegada": startDate, 
                "salida": endDate, 
                "cliente_apellido": lastName , 
                "precio": price
            }
            try:
                response = requests.post(API_URL + "/reserva",json=json_data).json()['id_reserva']    
            except requests.exceptions.RequestException as e:
                return server_error(e)
            return reserva_realizada(response,lastName)

@app.errorhandler(404)
def page_notfound(e):
    return render_template("error.html", error_code="404", error_description="Página no encontrada"), 404


@app.errorhandler(500)
def server_error(e):
    return render_template("error.html", error_code="500", error_description="Error del servidor"), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
