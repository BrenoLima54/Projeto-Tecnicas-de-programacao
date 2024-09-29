# Passos para desenvolver o projeto

# 1 . Importar bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import tabulate as tab # essa bibliote permite formatar o print do df
# import seaborn as sns # caso seja necessário para gráficos

# 2. Cirar classe DataQuality
class DataQuality:
    def __init__(self, diretorio:str) -> None:
        self.df = pd.read_csv(diretorio) # leitura do diretorio
        self.df_categ = self.df.select_dtypes(exclude=np.number)
        self.df_num = self.df.select_dtypes(include=np.number)

    def header(self, n=5) -> None:
        print("Dataframe - Cabeçalho:")
        head_df = self.df.head(n)
        print(tab.tabulate(head_df, headers='keys', showindex='always' , tablefmt='fancy_grid'))

        print("\nDataframe Categórico:")
        categ_df = self.df_categ.head(n)
        print(tab.tabulate(categ_df, headers='keys', showindex='always' , tablefmt='fancy_grid'))

        print("\nDataframe Numérico:")
        num_df = self.df_num.head(n)
        print(tab.tabulate(num_df, headers='keys', showindex='always' , tablefmt='fancy_grid'))
    
    def count_nulls(self) -> None:
        print("Contagem de valores nulos:")
        df_nulos = self.df.isnull().sum().reset_index()
        df_nulos.columns = ['Coluna', 'Quantidade']
        print(tab.tabulate(df_nulos, headers='keys', showindex='never' , tablefmt='fancy_grid'))

    def count_unique(self) -> None:
        print("Contagem de valores únicos:")
        df_unicos = self.df.nunique().reset_index()
        df_unicos.columns = ['Coluna', 'Quantidade']
        print(tab.tabulate(df_unicos, headers='keys', showindex='never' , tablefmt='fancy_grid'))

        
    # 3. Criar métodos: 
    # Mostrar Cabeçalho (método head())
    # Mostrar fim do df (método tail())
    # Somatória dos valores nulos
    # Somatória dos valores únicos
    # Análise dos dados categóricos geral ou por coluna (podemos definir a melhor forma)
        # df_categ.value_counts()
    # Análise dos dados numéricos 
        # df_num.describe()
        # df_num.corr() -> da pra fazer heatmap
    # Gráficos
    # Método para gerar relatório completo