## Autores

- *Nahuel Argandoña* 🇦🇷 - 🐣 [Mi Github](https://github.com/Aubar48)
- *Gastón Cane* 🇦🇷 - 🐣 [Mi Github](https://github.com/GasmauC)
- *Eric Heredia* 🇦🇷 - 🐣 [Mi Github](https://github.com/Eric-Heredia)
- *Sofia Auzqui* 🇦🇷 - 🐣 [Mi Github](https://github.com/Sofyauzqui)

<figure><img src="./ispc.jpeg" alt="logo" style="height: 200px;"></figure>

Este proyecto tiene una segunda parte que es este: https://github.com/GasmauC/IoT

## Evidencia de Aprendizaje 2: Sistema de Monitoreo IoT con Sensor PIR
Descripción del Proyecto
Este proyecto desarrolla un sistema de monitoreo basado en el uso de un sensor de luminosidad (fotoresistor) y un sensor de movimiento PIR, junto con un microcontrolador, para capturar datos y almacenarlos en una base de datos en la nube mediante una API RESTful. La información obtenida puede ser utilizada para análisis posteriores en tiempo real, facilitando la interacción con la base de datos desde cualquier lugar.

Objetivos
Objetivo General
Desarrollar un sistema de monitoreo que detecte el movimiento a través de un sensor PIR y almacene los datos obtenidos en una base de datos en la nube para análisis y consulta en tiempo real.

Objetivos Específicos
Implementar un sistema de detección de movimiento usando un sensor PIR y un microcontrolador conectado a una red Wi-Fi.
Configurar una API RESTful utilizando Flask para gestionar las solicitudes de almacenamiento y recuperación de datos.
Almacenar los datos del sensor en una base de datos MySQL alojada en Clever Cloud.
Metodología
Diseño del Sistema
El sistema está compuesto por un microcontrolador que se conecta a una red Wi-Fi y un sensor PIR que detecta el movimiento. Al detectar movimiento, se envían datos a una API, la cual interactúa con una base de datos MySQL para almacenar la información. La API también permite consultar los datos almacenados para su análisis.

Tecnologías Utilizadas
Microcontrolador: Para la captura de datos desde el sensor PIR.
Sensor PIR: Para la detección de movimiento.
API RESTful: Implementada con Flask para la interacción con la base de datos.
MySQL: Base de datos para el almacenamiento de los datos.
Clever Cloud: Hosting de la base de datos MySQL.
Wokwi: Simulador de hardware para probar el sistema.
Enlaces Importantes
Simulador en Wokwi: Permite la simulación del sistema sin necesidad de hardware físico.
Código en GitHub: Repositorio del código fuente del proyecto.
API Online en Render: API para interactuar con el sistema IoT, recibir datos y almacenarlos en la base de datos.
Base de Datos MySQL en Clever Cloud: Servicio de hosting para la base de datos MySQL.

3.1. Diseño del Sistema
El sistema está compuesto por un microcontrolador que se conecta a una red
Wi-Fi y utiliza un sensor PIR para detectar movimiento. Cuando se detecta
movimiento, se envían datos a una API, que a su vez interactúa con una base
de datos para almacenar la información. La API también permite recuperar los
datos almacenados.


Enlaces del proyecto https://wokwi.com/projects/406401817182924801
Simulador en Wokwi
Este simulador permite probar el funcionamiento del sistema de sensores y microcontrolador sin necesidad de hardware físico.

Código del proyecto en GitHub https://github.com/Aubar48/iot_lot_2
Aquí se encuentra el código completo, incluyendo la conexión entre el simulador y la base de datos MySQL.

API Online en Render https://iot-lot-2.onrender.com/data
La API permite interactuar con el sistema, recibir datos de los sensores y enviarlos a la base de datos. Puedes probar las respuestas del servidor con este enlace.

Clever Cloud - Base de Datos MySQL https://www.clever-cloud.com/product/mysql/
La base de datos MySQL está alojada en Clever Cloud, donde se almacenan los datos enviados por el sistema IoT.


Instalación
Simulador Wokwi
Abre el enlace al simulador.
Ejecuta el simulador para ver el sistema funcionando.
Código API
Clona este repositorio:
bash
Copiar código
git clone https://github.com/Aubar48/iot_lot_2
Instala las dependencias:
bash
Copiar código
npm install
Ejecuta el servidor:
bash
Copiar código
npm start
Base de Datos MySQL