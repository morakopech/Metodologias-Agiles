import random

palabras_facil = [["azucar", "Se le puede agregar a la chocolatada"],["perro", "Animal doméstico al que le gusta jugar"], ["casa", "Lugar donde vives"], ["mate", "Bebida argentina por excelencia"]]
palabras_intermedio = [["travesia", "Largo viaje o trampolín de experiencias"],["aventura", "Viaje emocionante y arriesgado"], ["melodia", "Secuencia armoniosa de sonidos"] ]
palabras_dificil = [["efimero", "Que dura por un corto periodo de tiempo"],["magico", "Relacionado con la magia o algo extraordinario"], ["enigma", "Misterio o situación difícil de entender"]]

abecedario =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

class Ahorcado():
    def __init__(self):
        self.palabra_vacia = ""
        self.palabra_a_adivinar = ["", ""]
        self.intentos = 7
        self.intentos_restantes = 7
        self.letras_adivinadas = []
        self.letras_usadas = []
        self.palabra_a_mostrar = []
        self.juego_finalizado = False
        
    
    def iniciar(self, dificultad=None, palabra=None):
        self.intentos = 7
        self.letras_adivinadas = []
        self.fin_juego = False
        self.letras_usadas = []
        if palabra is None:
            self.palabra_a_adivinar = self.elegir_palabra(dificultad)
            self.palabra_mostrada = self.crear_lineas(self.palabra_a_adivinar[0])
        else:
            self.palabra_a_adivinar[0] = palabra
            self.palabra_mostrada = self.crear_lineas(palabra)
        self.pista = ''
        self.dificultad = dificultad
        self.intentos_restantes = 7
        
    
    
    def rayitas(self, palabra):
        r = len(palabra)
        self.palabra_vacia = '_ ' * r
        return self.palabra_vacia.strip()  # Elimina el espacio extra al final de palabra_vacia
    
    def validar_letra(self, letra):
        if (letra in self.palabra_a_adivinar): 
            self.letras_adivinadas += letra
            return True
        else:
            return False
    
    def validar_palabra(self, palabra):
        if (palabra == self.palabra_a_adivinar): return True
        else: return False
        
    def intento(self,letra):
        self.letras_usadas.append(letra) #para agregar la letra ya sea si va o no
        print(letra)
        if (self.validar_letra(letra)):
            self.revelar_letra_correcta(letra)
            print(self.palabra_a_mostrar)
            return True
        else:
            self.intentos_restantes -= 1
            return False
    
    def revelar_letra_correcta(self, letra):
        l_adivinadas = ""
        for l in self.palabra_a_adivinar: #[0]
            if l == letra or l in self.letras_usadas:
                l_adivinadas += l
            else:
                l_adivinadas += "_"
        self.palabra_a_mostrar = l_adivinadas ##VER TEST
    
    
    def letras_utilizadas(self, letra):
        if letra in self.letras_adivinadas:
            return True
        else: return False
        
    def validar_fin_del_juego(self):
        if self.intentos_restantes == 0 or ("".join(self.palabra_a_mostrar) == self.palabra_a_adivinar): #intentos
            self.juego_finalizado = True
        return self.juego_finalizado
    
    def elegir_palabra(self,dificultad):
        if dificultad == 'facil':
            return random.choice(palabras_facil)
        elif dificultad == 'media':
            return random.choice(palabras_intermedio)
        else:
            return random.choice(palabras_dificil)
    
    
    def obtener_pista(self):
        self.pista = self.palabra_a_adivinar[1]
        return self.pista