from Pregunta import RegistroPregunta
from Modelo import clasificar_respuesta

class Calificar:
    def __init__(self):
        self.registros = []

    def ingresar_registros(self, numero_pregunta, respuesta):
        for i in range(8):
            #Se requiere que se ajuste el metodo clasificar_respuesta 
            clasificacion, calificacion = clasificar_respuesta(nueva_respuesta_LN = respuesta[i], numero_pregunta = numero_pregunta[i])

            registro = RegistroPregunta(numero_pregunta, calificacion, clasificacion)
            self.registros.append(registro)

    def calcular_promedio(self):
        suma_calificaciones = sum(registro.get_calificacion() for registro in self.registros)
        promedio_calificaciones = suma_calificaciones / len(self.registros)
        return promedio_calificaciones

    def ejecutar(self, numero_pregunta, respuesta):
        self.ingresar_registros(numero_pregunta = numero_pregunta, respuesta = respuesta)
        promedio = self.calcular_promedio()
        return round(promedio)
