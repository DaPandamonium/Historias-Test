import random

# Plantilla personajes

class Personaje:
    def __init__(self, nombre, sexo, especie, fuerza, inteligencia, carisma, suerte):
        self.nombre = nombre
        self.sexo = sexo
        self.especie = especie
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.carisma = carisma
        self.suerte = suerte

    def golpe_de_suerte(self):
        milagro = random.randint(-10, 0)
        ventaja = milagro + self.suerte
        if ventaja >= 1:
            return(ventaja)
            
        else:
            ventaja == 0

# Distintos personajes

sandra = Personaje('Sandra', 'Mujer', 'Humana', 6, 8, 9, 5)

# Opertura
print('Bienvenida, ultimamente tu trabajo a sido muy duro, y el resto de tu vida tambien. No puedo hacer mucho, pero tampoco quiero no hacer nada. Asi que esto es tu opcion a una venganza dentro del marco de la ley. Espero que te guste y que perdones la infinidad de faltas de ortografia.')

#Explicacion del juego
print('Para avanzar en el juego tendras que escribir exactamente las palabras que aparezcan entre comillas ("Aqui") en la opcion que quieras escoger y pulsar "Enter"')