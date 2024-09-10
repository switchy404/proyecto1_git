import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/Nicolas/Downloads/SeoulBikeData_utf8.csv")

# Alistamiento de Datos -------------------------------------------------------

duplicates = len(df[df.duplicated()])
missing_values = df.isnull().sum().sum()

# Categóricas a Numéricas
df['Seasons'] = df['Seasons'].map({'Winter': 3, 'Spring': 2, 'Summer':1, 'Autumn':0})
df['Holiday'] = df['Holiday'].map({'Holiday': 1, 'No Holiday': 0})
df["Functioning Day"] = df['Functioning Day'].map({'Yes':1,'No':0})

# Análisis Exploratorio de datos -------------------------------------------------------

df.head()
variables = ['Hour', 'Temperature(C)', 'Rented Bike Count']
df[variables].describe()

# Histograma de las bicicletas alquiladas.
sns.histplot(df['Rented Bike Count'], kde=True)
plt.title('Distribución de bicicletas alquiladas. ')
plt.show()

# Histograma de la temperatura.
sns.histplot(df['Temperature(C)'], kde=True)
plt.title('Distribución de la temperatura. ')
plt.show()

# Diagrama de caja para la cantidad de bicicletas alquiladas por estación.
sns.boxplot(x='Seasons', y='Rented Bike Count', data=df)
plt.title('Bicicletas alquiladas por estación')
plt.show()

# Diagrama de caja para la temperatura.
sns.boxplot(x='Seasons', y='Temperature(C)', data=df)
plt.title('Temperatura por estación')
plt.show()

# Relación entre la temperatura y las bicicletas alquiladas.
sns.scatterplot(x='Temperature(C)', y='Rented Bike Count', data=df)
plt.title('Relación entre la temperatura y las bicicletas alquiladas')
plt.show()

# Diagrama de violín para la temperatura y las bicicletas alquiladas.
sns.violinplot(x='Seasons', y='Rented Bike Count', data=df)
plt.title('Distribución de bicicletas alquiladas por estación')
plt.show()