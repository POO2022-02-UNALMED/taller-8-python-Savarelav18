from deportista import Deportista
from persona import Persona

class Futbolista(Persona,Deportista):
    listaFutbolistas=[]
    def __init__(self,nombre,edad,altura,sexo,añosPracticando,golesMarcados,tarjetasRojas,piernaHabil):
        Persona.__init__(self,nombre,edad,altura,sexo)
        Deportista.__init__(self,añosPracticando)
        self._golesMarcados=golesMarcados
        self._tarjetasRojas=tarjetasRojas
        self._piernaHabil=piernaHabil
        self.listaFutbolistas.append(self)
    
    def __str__(self):
        return f"Mi nombre es {Persona.getNombre} soy profesional en el deporte {Deportista.getDeporte} Tengo {Persona.getEdad} años de edad y llevo {Deportista.getAñosPracticando} años en el deporte"
    
    def getTarjetasRojas(self):
        return self._tarjetasRojas
    
    def setTarjetasRojas(self,tarjetasRojas):
        self._tarjetasRojas=tarjetasRojas
    
    def getGolesMarcados(self):
        return self._golesMarcados
    
    def setGolesMarcados(self,golesMarcados):
        self._golesMarcados=golesMarcados
    
    def getPiernaHabil(self):
        return self._piernaHabil
    
    def setPiernaHabil(self,piernaHabil):
        self._piernaHabil=piernaHabil
    
    @classmethod
    def setListaFutbolistas(clc,listaFutbolistas):
        clc.listaFutbolistas=listaFutbolistas

    @classmethod
    def getListaFutbolistas(clc):
        return clc.listaFutbolistas
    
    