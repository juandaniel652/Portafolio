# Primero instala la librería si no la tienes
# pip install qrcode[pil]

import qrcode

URL_PORTAFOLIO = "https://juan-dominguez.netlify.app/" 

# URL de tu portafolio
url_portafolio = URL_PORTAFOLIO  # reemplaza con tu link real

# Crear QR
qr = qrcode.QRCode(
    version=1,  # tamaño del QR (1 es el más pequeño)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # tolerancia a errores
    box_size=10,  # tamaño de cada caja
    border=4,  # grosor del borde
)
qr.add_data(url_portafolio)
qr.make(fit=True)

# Generar imagen
img = qr.make_image(fill_color="black", back_color="white")

# Guardar como archivo
img.save("img/qr_portafolio.png")

print("QR generado y guardado como 'qr_portafolio.png'")