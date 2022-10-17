class Deportista:
    def __init__(self,añosPracticando):
        self._deporte="Futbol"
        self._añosPracticando=añosPracticando
    
    def getDeporte(self):
        return self._deporte
    
    def setDeporte(self,deporte):
        self._deporte = deporte
    
    def getAñosParticipando(self):
        return self._añosPracticando
    
    def setAñosParticipando(self,añosPracticando):
        self._añosPracticando = añosPracticando