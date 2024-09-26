# Passos para desenvolver o projeto

# 1 . Importar bibliotecas
import pandas as pd
# import tabulate as tab # essa bibliote permite formatar o print do df
# import seaborn as sns # caso seja necessário para gráficos

# 2. Cirar classe DataQuality
class DataQuality:
    def __init__(self, diretorio:str) -> None:
        # o construtor recebe um diretorio em formato de string
        self.df = pd.read_csv(diretorio) # leitura do diretorio
        # self.df_categ = self.df.select_dtypes(exclude=np.number)
        # self.df_num = self.df.select_dtypes(include=np.number)
        
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