import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos desde el archivo CSV
df = pd.read_csv('prueba.csv')

# Gráfica de barras para la distribución de edad
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Edad')
plt.title('Distribución de Edad')
plt.xlabel('Edad')
plt.ylabel('Cantidad')
plt.show()

# Gráfica de pastel para la distribución de género
plt.figure(figsize=(8, 6))
df['Género'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Distribución de Género')
plt.ylabel('')
plt.show()

# Gráfica de barras para el presupuesto de dinero en la calle
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Dinero en la calle')
plt.title('Presupuesto de Dinero en la Calle')
plt.xlabel('Dinero en la calle')
plt.ylabel('Cantidad')
plt.show()

# Gráfica de barras para la opinión sobre Coca-Cola
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Opinión Coca-Cola')
plt.title('Opinión sobre Coca-Cola')
plt.xlabel('Opinión')
plt.ylabel('Cantidad')
plt.show()

# Gráfica de barras para las situaciones de consumo de Coca-Cola
plt.figure(figsize=(10, 6))
sns.countplot(data=df, y='Situaciones de consumo')
plt.title('Situaciones de Consumo de Coca-Cola')
plt.xlabel('Cantidad')
plt.ylabel('Situaciones de consumo')
plt.show()

# Gráfica de barras para los gustos de Coca-Cola
plt.figure(figsize=(10, 6))
df['Gustos de Coca-Cola'].str.split(',').explode().value_counts().plot(kind='bar')
plt.title('Aspectos Gustados de Coca-Cola')
plt.xlabel('Aspectos')
plt.ylabel('Cantidad')
plt.show()

# Gráfica de barras para los aspectos negativos de Coca-Cola
plt.figure(figsize=(10, 6))
df['Aspectos negativos'].str.split(',').explode().value_counts().plot(kind='bar')
plt.title('Aspectos Negativos de Coca-Cola')
plt.xlabel('Aspectos')
plt.ylabel('Cantidad')
plt.show()

# Gráfica de barras para la opinión sobre el sabor de Coca-Cola
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Sabor de Coca-Cola')
plt.title('Opinión sobre el Sabor de Coca-Cola')
plt.xlabel('Opinión')
plt.ylabel('Cantidad')
plt.show()

# Gráfica de barras para el nivel de dulzura de Coca-Cola
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Nivel de dulzura')
plt.title('Nivel de Dulzura de Coca-Cola')
plt.xlabel('Nivel de dulzura')
plt.ylabel('Cantidad')
plt.show()

# Gráfica de barras para la opinión sobre la diferenciación de Coca-Cola
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Diferenciación')
plt.title('Opinión sobre la Diferenciación de Coca-Cola')
plt.xlabel('Opinión')
plt.ylabel('Cantidad')
plt.show()

# Gráfica de barras para la opinión sobre la calidad/sabor reciente de Coca-Cola
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Calidad/Sabor reciente')
plt.title('Opinión sobre la Calidad/Sabor Reciente de Coca-Cola')
plt.xlabel('Opinión')
plt.ylabel('Cantidad')
plt.show()

# Gráfica de barras para la disposición a comprar baja en calorías
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Comprar baja en calorías')
plt.title('Disposición a Comprar Baja en Calorías')
plt.xlabel('Respuesta')
plt.ylabel('Cantidad')
plt.show()

# Gráfica de barras para las sugerencias para mejorar Coca-Cola
plt.figure(figsize=(10, 6))
df['Sugerencias para mejorar'].str.split(',').explode().value_counts().plot(kind='bar')
plt.title('Sugerencias para Mejorar Coca-Cola')
plt.xlabel('Sugerencias')
plt.ylabel('Cantidad')
plt.show()

# Gráfica de barras para la puntuación del refresco Coca-Cola
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Puntuación')
plt.title('Puntuación del Refresco Coca-Cola')
plt.xlabel('Puntuación')
plt.ylabel('Cantidad')
plt.show()