## Descripción
Aplicación de consola desarrollada en Python que permite generar imágenes QR a partir de un texto o URL ingresados por el usuario.

## Requisitos
Python 3.10 o superior
pip


## Estructura 
generador_qr/
├── main.py            # punto de entrada: pide los datos y maneja errores
├── generador.py       # módulo propio: genera y guarda el QR
├── requirements.txt   # dependencias congeladas con pip freeze
└── README.txt			# información y forma de uso de la aplicación


## Crear entorno virtual
Windows
python -m venv .venv
.venv\Scripts\activate
Linux / Mac
python -m venv .venv
source .venv/bin/activate


## Instalar dependencias
pip install qrcode pillow	
pip install -r requirements.txt


## Generar archivo de dependencias
pip freeze > requirements.txt


## Ejecutar el programa
python main.py


## Uso
Ingresar un texto o URL.
Ingresar el nombre del archivo de salida.
Elegir un color para el QR (opcional).
El programa generará la imagen y mostrará la ubicación donde fue guardada.
Si el nombre de la imagen ya existe en esa ubicación, se guardará con un número al final.
(Ej. Imagen --> Imagen.png, Imagen_1.png, etc.)


## Librerías de terceros usadas

- [qrcode](https://pypi.org/project/qrcode/) → genera el código QR.
- [pillow](https://pypi.org/project/pillow/) → crea y guarda la imagen PNG.


## Integrantes
Cecilia Muo
Daiana Rizzardi
Lucía Ballester Gañez
