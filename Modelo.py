import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
import joblib

nltk.download('omw-1.4')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    tokens = word_tokenize(text.lower(), language='spanish')
    stop_words = set(stopwords.words('spanish'))
    tokens = [token for token in tokens if token not in stop_words]
    lemmatizer = nltk.WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return " ".join(tokens)

def entrenar_modelo():
    train_data = pd.read_csv('csv/Pregunta10.csv')
    X_train = train_data['respuesta_LN']
    y_train = train_data['respuesta']
    calificacion_train = train_data['calificacion']

    X_train = [preprocess_text(text) for text in X_train]

    vectorizer = TfidfVectorizer()
    X_train = vectorizer.fit_transform(X_train)

    model = SVC()
    model.fit(X_train, y_train)

    # Guardar el modelo entrenado en un archivo
    joblib.dump(model, 'modelo_entrenado.joblib')

    return vectorizer, y_train

def clasificar_respuesta(respuesta, vectorizer, y_train):
    model = joblib.load('modelo/modelo_entrenado.joblib')

    respuesta_preprocesada = preprocess_text(respuesta)
    respuesta_transformada = vectorizer.transform([respuesta_preprocesada])
    categoria_predicha = model.predict(respuesta_transformada)[0]

    train_data = pd.read_csv('csv/Pregunta10.csv')
    calificacion_train = train_data['calificacion']
    calificacion_predicha = calificacion_train[y_train == categoria_predicha].iloc[0]

    return categoria_predicha, calificacion_predicha

# Entrenar el modelo y guardar el vectorizador
vectorizer, y_train = entrenar_modelo()

respuesta = "Me lo recomendaron"
categoria_predicha, calificacion_predicha = clasificar_respuesta(respuesta, vectorizer, y_train)

print("Categoría predicha:", categoria_predicha)
print("Calificación predicha:", calificacion_predicha)