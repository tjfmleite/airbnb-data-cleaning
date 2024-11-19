
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


file_name = "listings.csv"  
data = pd.read_csv(file_name)


print("\nDataset - Primeiras Linhas:")
print(data.head())

print("\nInformações do Dataset:")
print(data.info())

# Verificar valores ausentes
print("\nValores Ausentes (Total por Coluna):")
missing_values = data.isnull().sum()
missing_values = missing_values[missing_values > 0].sort_values(ascending=False)
print(missing_values)

# Visualizar a distribuição de valores ausentes
plt.figure(figsize=(10, 6))
sns.barplot(x=missing_values.index, y=missing_values)
plt.xticks(rotation=90)
plt.title("Valores Ausentes por Coluna")
plt.ylabel("Número de Valores Ausentes")
plt.show()

# Tratamento de valores ausentes
# Estratégia: Preencher valores numéricos com a mediana e valores categóricos com a moda
for column in data.columns:
    if data[column].dtype == 'object':
        data[column].fillna(data[column].mode()[0], inplace=True)
    else: 
        data[column].fillna(data[column].median(), inplace=True)

# Confirmar que todos os valores ausentes foram tratados
print("\nValores Ausentes Após Tratamento:")
print(data.isnull().sum().sum())  # Deve ser 0

# Verificar duplicates
duplicates = data.duplicated().sum()
print(f"\nNúmero de Linhas Duplicadas: {duplicates}")

# Remover duplicates 
if duplicates > 0:
    data = data.drop_duplicates()
    print("\nLinhas duplicadas removidas.")

# Identificar colunas com baixa variabilidade
low_variability = data.nunique()[data.nunique() < 10].index
print("\nColunas com baixa variabilidade:")
print(low_variability)

# Remover colunas irrelevantes ou com baixa variabilidade
data = data.drop(columns=low_variability)
print("\nColunas removidas com baixa variabilidade.")

# Identificar e remover outliers em uma variável de interesse
variable = "price"  
sns.boxplot(data=data, x=variable)
plt.title(f"Outliers na Variável {variable}")
plt.show()

# Remoção de outliers usando o IQR (Interquartile Range)
Q1 = data[variable].quantile(0.25)
Q3 = data[variable].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

data_cleaned = data[(data[variable] >= lower_bound) & (data[variable] <= upper_bound)]
print(f"\nNúmero de Linhas Após Remoção de Outliers em {variable}: {len(data_cleaned)}")

# Exportar o dataset limpo
data_cleaned.to_csv("listings_cleaned.csv", index=False)
print("\nDataset limpo salvo como 'listings_cleaned.csv'.")


print("\nEstatísticas Descritivas do Dataset Limpo:")
print(data_cleaned.describe())
