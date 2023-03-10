import replicate
import os
from dotenv import load_dotenv
import urllib.request
import requests
import random

load_dotenv()
REPLICATE_API_TOKEN=os.getenv("REPLICATE_API_TOKEN")
def creacionDeImagen(mensaje):
    model = replicate.models.get("tstramer/midjourney-diffusion")
    version = model.versions.get("436b051ebd8f68d23e83d22de5e198e0995357afef113768c20f0b6fcef23c8b")
# https://replicate.com/tstramer/midjourney-diffusion/versions/436b051ebd8f68d23e83d22de5e198e0995357afef113768c20f0b6fcef23c8b#input
    inputs = {
        'prompt': f'{mensaje}',
        'negative_prompt': 'penis',
        'width': 768,
        'height': 768,
        'prompt_strength': 0.3,
        'num_outputs': 1,
        'num_inference_steps': 150,
        'guidance_scale': 7.5,
        'scheduler': "DPMSolverMultistep",
    }

    # https://replicate.com/tstramer/midjourney-diffusion/versions/436b051ebd8f68d23e83d22de5e198e0995357afef113768c20f0b6fcef23c8b#output-schema

    output = version.predict(**inputs)
    return output[0]

def guardarImagen(url,nombre_de_archivo):
    urllib.request.urlretrieve(url, nombre_de_archivo)
    nombre_local_imagen = f'C:/Lautaro/Python-personal/Mastodon/img/{nombre_de_archivo}.png' # El nombre con el que queremos guardarla
    imagen = requests.get(url).content
    with open(nombre_local_imagen, 'wb') as handler:
        handler.write(imagen)


















# ingreso el prompt
    # 'prompt': f'{mensaje}',

    # Especificar cosas para no ver en la salida
    # 'negative_prompt': 'penis',

    # Ancho de la imagen de salida. El tamaño máximo es 1024x768 o 768x1024 debido a los límites de memoria
    # Valores permitidos: 128, 256, 384, 448, 512, 576, 640, 704, 768, 832, 896, 960,1024
    # Valor por defecto:768
    # 'width': 768,

    # Altura de la imagen de salida. El tamaño máximo es 1024x768 o 768x1024 debido a los límites de memoria
    # Valores permitidos: 128, 256, 384, 448, 512, 576, 640, 704, 768, 832, 896, 960,1024
    # 'height': 768,

    # Fortaleza rápida al usar la imagen de inicio. 1.0 corresponde a la destrucción total de la información en la imagen de inicio
    # 'prompt_strength': 0.8,

    # Número de imágenes a generar. Número por defecto es 1. Puede ir hasta 4
    # 'num_outputs': 1,

    # Número de pasos de eliminación de ruido
    # Valor por defecto:50. Va hasta 500
    # 'num_inference_steps': 50,

    # Guia sin clasificación. Por defecto 7.5 
    # Range: 1 to 20
    # 'guidance_scale': 7.5,

    # Elija un programador.
    # Valores permitidos: DDIM, K_EULER, DPMSolverMultistep, K_EULER_ANCESTRAL, PNDM,KLMS
    # Valor por defecto:DPMSolverMultistep
    # 'scheduler': "DPMSolverMultistep",

    # Semilla aleatoria. Dejar en blanco para aleatorizar la semilla
    # 'seed': ...,