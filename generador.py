"""Módulo propio: generación de códigos QR con qrcode."""

from pathlib import Path

import qrcode


def generar_qr(texto: str, archivo: str, color: str) -> Path:
    """Genera un código QR y lo guarda como imagen PNG.

    Args:
        texto (str): Texto o URL que se codificará en el QR.
        archivo (str): Ruta y nombre del archivo PNG.
        color (str): Color del QR, en inglés (ej: "Blue").

    Returns:
        Path: Ruta absoluta del archivo generado. Si el nombre ya
        existía, se le agrega un número al final.

    Raises:
        OSError: Si no se puede guardar la imagen.
    """
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(texto)
    qr.make(fit=True)

    imagen = qr.make_image(
        fill_color=color,
        back_color="white"
    )

    ruta = obtener_ruta_libre(Path(archivo).resolve())
    imagen.save(ruta)

    return ruta


def obtener_ruta_libre(ruta: Path) -> Path:
    """Devuelve una ruta que no exista, agregando un número si hace falta.

    Si "mi_qr.png" ya existe, prueba "mi_qr_1.png", "mi_qr_2.png", etc.

    Args:
        ruta (Path): Ruta deseada para el archivo.

    Returns:
        Path: La misma ruta si está libre, o una con un número al final.
    """
    ruta_nueva = ruta
    numero = 1

    while ruta_nueva.exists():
        ruta_nueva = ruta.with_name(f"{ruta.stem}_{numero}{ruta.suffix}")
        numero += 1

    return ruta_nueva