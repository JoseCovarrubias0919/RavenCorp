import pickle

def predecir_valores(texto):
    # Cargar el modelo desde el archivo .pkl
    with open('modelo.pkl', 'rb') as file:
        svm = pickle.load(file)

    # Cargar el vectorizador desde el archivo .pkl
    with open('vectorizer.pkl', 'rb') as file:
        vectorizer = pickle.load(file)

    # Preprocesar el texto de entrada utilizando el vectorizador
    X = vectorizer.transform([texto])

    # Realizar la predicción
    prediccion = svm.predict(X)

    return prediccion


# Ejemplo de uso
texto = "35,Masculino,20,Me gusta,En comidas familiares,La marca y la historia,No encuentro aspectos negativos,Bueno,Dulce pero equilibrado,Sí,No,Tener más opciones sin cafeína"
resultado = predecir_valores(texto)
print("La predicción es:", resultado)