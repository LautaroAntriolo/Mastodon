import replicate
import os
from dotenv import load_dotenv

load_dotenv()
REPLICATE_API_TOKEN=os.getenv("REPLICATE_API_TOKEN")

model = replicate.models.get("tstramer/midjourney-diffusion")
version = model.versions.get("436b051ebd8f68d23e83d22de5e198e0995357afef113768c20f0b6fcef23c8b")
mensaje =input("ingrese un mensaje para el promp\n")
# https://replicate.com/tstramer/midjourney-diffusion/versions/436b051ebd8f68d23e83d22de5e198e0995357afef113768c20f0b6fcef23c8b#input
inputs = {
    # ingreso el prompt
    'prompt': f'{mensaje}',

    # Especificar cosas para no ver en la salida
    'negative_prompt': 'penis',

    # Ancho de la imagen de salida. El tamaño máximo es 1024x768 o 768x1024 debido a los límites de memoria
    # Valores permitidos: 128, 256, 384, 448, 512, 576, 640, 704, 768, 832, 896, 960,1024
    # Valor por defecto:768
    'width': 768,

    # Altura de la imagen de salida. El tamaño máximo es 1024x768 o 768x1024 debido a los límites de memoria
    # Valores permitidos: 128, 256, 384, 448, 512, 576, 640, 704, 768, 832, 896, 960,1024
    'height': 768,

    # Fortaleza rápida al usar la imagen de inicio. 1.0 corresponde a la destrucción total de la información en la imagen de inicio
    'prompt_strength': 0.8,

    # Número de imágenes a generar. Número por defecto es 1. Puede ir hasta 4
    'num_outputs': 1,

    # Número de pasos de eliminación de ruido
    # Valor por defecto:50. Va hasta 500
    'num_inference_steps': 50,

    # Guia sin clasificación. Por defecto 7.5 
    # Range: 1 to 20
    'guidance_scale': 7.5,

    # Elija un programador.
    # Valores permitidos: DDIM, K_EULER, DPMSolverMultistep, K_EULER_ANCESTRAL, PNDM,KLMS
    # Valor por defecto:DPMSolverMultistep
    'scheduler': "DPMSolverMultistep",

    # Semilla aleatoria. Dejar en blanco para aleatorizar la semilla
    # 'seed': ...,
}

# https://replicate.com/tstramer/midjourney-diffusion/versions/436b051ebd8f68d23e83d22de5e198e0995357afef113768c20f0b6fcef23c8b#output-schema

output = version.predict(**inputs)

print(output)