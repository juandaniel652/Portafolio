from PIL import Image
import pillow_heif

# Asegúrate de que Pillow puede leer y escribir en el formato AVIF
pillow_heif.register_heif_opener()

def convertir_png_a_avif(ruta_png, ruta_avif, calidad=80):
    """
    Convierte una imagen PNG a formato AVIF con la calidad especificada.

    Args:
        ruta_png (str): La ruta al archivo de imagen PNG de entrada.
        ruta_avif (str): La ruta donde se guardará el archivo AVIF de salida.
        calidad (int): La calidad de compresión (0-100, por defecto 80).
    """
    try:
        # Abre la imagen PNG
        img = Image.open(ruta_png)

        # Guarda la imagen en formato AVIF con la calidad deseada
        img.save(ruta_avif, format="AVIF", quality=calidad)
        print(f"Imagen convertida a {ruta_avif} con éxito.")

    except FileNotFoundError :

        print(f"Error: El archivo {ruta_png} no fue encontrado.")

    except Exception as e :
        
        print(f"Ocurrió un error durante la conversión: {e}")

# --- Ejemplo de uso ---
# Reemplaza 'imagen_original.png' con la ruta de tu archivo PNG
# y 'imagen_convertida.avif' con el nombre de archivo de salida deseado.

lista_de_png = ['img/ventas/editar_producto.png', 'img/ventas/logo.png', 'img/ventas/mensaje_gurdado.png', 'img/ventas/pantalla_principal.png',
                'img/ventas/recaudacion_dias.png', 'img/ventas/recaudacion_mes.png', 'img/ventas/recaudacion_productos.png', 'img/ventas/recaudacion_total.png']
lista_de_avif = ['img/ventas/editar_producto.avif', 'img/ventas/logo.avif', 'img/ventas/mensaje_gurdado.avif', 'img/ventas/pantalla_principal.avif',
                 'img/ventas/recaudacion_dias.avif', 'img/ventas/recaudacion_mes.avif', 'img/ventas/recaudacion_productos.avif', 'img/ventas/recaudacion_total.avif']

for png, avif in zip(lista_de_png, lista_de_avif):
    convertor = convertir_png_a_avif(png, avif, calidad=80)