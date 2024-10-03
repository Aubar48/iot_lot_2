from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configuración de la conexión a la base de datos
db_config = {
    "host": "bxy5ofa8ezud0x0caavs-mysql.services.clever-cloud.com",
    "user": "uupemiqze1zhijfn",
    "password": "XnExGlv7QzWuydrfjtLK",  # Reemplaza con tu contraseña
    "database": "bxy5ofa8ezud0x0caavs",
}

# Ruta para insertar datos
@app.route("/data", methods=["POST"])
def insert_data():
    if request.is_json:
        data = request.get_json()
        sensor = data.get("sensor")
        value = data.get("value")

        if sensor is None or value is None:
            return jsonify({"status": "error", "message": "Both 'sensor' and 'value' are required"}), 400

        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            cursor.execute("INSERT INTO sensor_data (sensor, value) VALUES (%s, %s)", (sensor, value))
            conn.commit()

            cursor.close()
            conn.close()

            return jsonify({"status": "success"}), 201

        except mysql.connector.Error as err:
            return jsonify({"status": "error", "message": str(err)}), 500
    else:
        return jsonify({"status": "error", "message": "Request must be JSON"}), 400


# Ruta para mostrar los datos almacenados
@app.route("/data", methods=["GET"])
def get_data():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Ejecutar consulta para obtener todos los datos
        cursor.execute("SELECT id, sensor, value, timestamp FROM sensor_data")
        rows = cursor.fetchall()

        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()

        # Formatear los datos como una lista de diccionarios
        results = []
        for row in rows:
            results.append({
                "id": row[0],
                "sensor": row[1],
                "value": row[2],
                "timestamp": row[3].strftime("%Y-%m-%d %H:%M:%S")  # Formato de fecha
            })

        return jsonify({"status": "success", "data": results}), 200

    except mysql.connector.Error as err:
        return jsonify({"status": "error", "message": str(err)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
