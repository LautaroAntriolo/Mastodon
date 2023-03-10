from datetime import datetime
import Toot

def funcionViernes():
    Toot.video('''Gracias a Dios es viernes''','video/viernes/graciasADiosEsViernes.mp4', 'viernes','Friday','shrek')  

def funcionDiaria():
    Toot.imagen("Vamos a ver como se publica esta imagen", 'img/imagenHormigas1.png', 'hormigas','IA','mdjurnie')
# funcionViernes()

# funcionViernes()
nameDias ={
        'Lunes':1,
        'Martes':2,
        'Miercoles':3,
        'Jueves':4,
        'Viernes':5,
        'Sabado':6,
        'Domingo':7
    }
def diaDeHoy():
    dia = datetime.now().weekday()
    return list(nameDias.keys())[dia]

def mensajeSegunElDia():
    posicionDeHoy = nameDias[diaDeHoy()]
    if posicionDeHoy == 5:
        return "¡Es hoy! Gracias a Dios es Vierness"
    elif posicionDeHoy < 5:
        return f'faltan {5-posicionDeHoy} para el Viernes.'
    elif posicionDeHoy == 6:
        return f'Paso {abs(5-posicionDeHoy)} día viernes, ya volvera...'
    elif posicionDeHoy == 7:
        return f'Pasaron {abs(5-posicionDeHoy)} días del viernes, hoy es Domingo de recuperación.'
