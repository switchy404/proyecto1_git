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

# DeQu, este archivo ya sirve por completo :cat:

# Calcular la correlación entre las variables numéricas
correlation_matrix = data[['Rented_Bike_Count', 'Temperature', 'Hour', 'Season', 'Holiday']].corr()

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Matriz de Correlación')
plt.show()

# Relación entre temperatura y bicicletas alquiladas
sns.scatterplot(x='Temperature', y='Rented_Bike_Count', data=data)
plt.title('Relación entre temperatura y bicicletas alquiladas')
plt.show()

# Relación entre hora del día y bicicletas alquiladas
sns.scatterplot(x='Hour', y='Rented_Bike_Count', data=data)
plt.title('Relación entre hora del día y bicicletas alquiladas')
plt.show()

# Pairplot para ver relaciones entre múltiples variables
sns.pairplot(data[['Rented_Bike_Count', 'Temperature', 'Hour', 'Season', 'Holiday']])
plt.show()

# Matriz de correlación para todas las variables numéricas
corr_matrix = data[['Rented_Bike_Count', 'Temperature', 'Hour', 'Season', 'Holiday']].corr()

# Heatmap de la matriz de correlación
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Matriz de Correlación entre Variables')
plt.show()
