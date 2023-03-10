def funcionViernes(mje, *args):
    Toot.video(f'''{mje}''','video/viernes/graciasADiosEsViernes.mp4',*args)  

def funcionDiaria(mje,nombreImagen, *args):
    Toot.imagen(f'{mje}', f'img/{nombreImagen}.png',*args)


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

animalesYAcciones = {
    "leones": ["rugiendo", "cazando en equipo", "defendiendo su territorio", "cuidando a sus crías", "persiguiendo a su presa"],
    "delfines": ["nadando juntos", "saltando en el aire", "comunicándose a través de sonidos", "buscando pareja para aparearse", "sumergiéndose en el agua"],
    "gorilas": ["balanceándose de rama en rama", "jugando y peleando entre ellos", "comiendo hojas y frutas", "cuidando a sus crías", "marchando en fila india"],
    "cebras": ["pastando en la sabana", "corriendo por la pradera", "migrando a través de grandes distancias", "reproduciéndose en masa", "defendiendo a su manada"],
    "pingüinos": ["marchando en fila india", "nadando y sumergiéndose en el agua", "construyendo nidos elaborados", "cuidando a sus crías", "buscando pareja para aparearse"],
    "tigres": ["cazando en solitario", "defendiendo su territorio", "comunicándose a través de sonidos", "cuidando a sus crías", "persiguiendo a su presa"],
    "jirafas": ["pastando en la sabana", "balanceándose en los arboles", "corriendo en grupo", "defendiendo a su manada", "marchando en fila india"],
    "ballenas": ["migrando a través del océano", "nadando juntas en grupos", "comunicándose a través de sonidos", "buscando pareja para aparearse", "saltando fuera del agua"],
    "hienas": ["cazando en equipo", "comunicándose a través de sonidos", "defendiendo su territorio", "cuidando a sus crías", "persiguiendo a su presa"],
    "elefantes": ["pastando en la sabana", "balanceándose de rama en rama", "defendiendo a su manada", "cuidando a sus crías", "marchando en fila india"]
}
lugares = ["madriguera", "nido gigante", "cueva en la montaña", "madriguera subterránea", "gran colonia", "hogar de árbol", "agujero en el suelo", "madriguera de hielo", "escondite de rocas", "hamaca de madera"]





if __name__=="__main__":
    from datetime import datetime
    import Toot
    from imagenesIA import guardarImagen, creacionDeImagen
    import random
    animal = random.choice(list(animalesYAcciones.keys()))
    accion = random.choice(animalesYAcciones["leones"])
    lugar = random.choice(lugares)
    lugarSinEspacio = lugar.replace(" ", "_") 
    nombre = accion.replace(" ", "_")
    mensajedeldia = mensajeSegunElDia()
    mjeDelPrompt =f'Una imagen como si estuviera pintada con acuarelas de un grupo de {animal} que están {accion} en su {lugar}. Creado por midjourney'
    guardarImagen(creacionDeImagen(mjeDelPrompt),nombre)
    if diaDeHoy() == 'Viernes':
        # funcionViernes(mensajedeldia, 'viernes','Friday','shrek')
        funcionDiaria(mjeDelPrompt,nombre,animal,lugarSinEspacio)
    else:
        funcionDiaria(mjeDelPrompt,nombre,animal)