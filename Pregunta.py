class RegistroPregunta:
    def __init__(self, numero_pregunta, calificacion, clasificacion):
        self._numero_pregunta = numero_pregunta
        self._calificacion = calificacion
        self._clasificacion = clasificacion
    
    # Getter para el número de pregunta
    def get_numero_pregunta(self):
        return self._numero_pregunta
    
    # Setter para el número de pregunta
    def set_numero_pregunta(self, numero_pregunta):
        self._numero_pregunta = numero_pregunta
    
    # Getter para la calificación
    def get_calificacion(self):
        return self._calificacion
    
    # Setter para la calificación
    def set_calificacion(self, calificacion):
        self._calificacion = calificacion
    
    # Getter para la clasificación
    def get_clasificacion(self):
        return self._clasificacion
    
    # Setter para la clasificación
    def set_clasificacion(self, clasificacion):
        self._clasificacion = clasificacion