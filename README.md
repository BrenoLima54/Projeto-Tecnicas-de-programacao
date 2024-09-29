# Data Quality Analysis

## Projeto desenvolvido por:
Breno Lima - https://github.com/BrenoLima54
Fernando Soutto - https://github.com/FeSoutto
Raul Felipe - https://github.com/raulcrvlh

Este projeto tem como objetivo fornecer uma análise de qualidade de dados de forma rápida e eficiente utilizando a linguagem Python. A classe `DataQuality` permite realizar diversas análises e gerar relatórios detalhados sobre um conjunto de dados fornecido.

## Funcionalidades

- **Informações Gerais**: Exibe o número de linhas e colunas do DataFrame, além de listar as colunas categóricas e numéricas.
- **Primeiras Linhas**: Mostra as primeiras `n` linhas do DataFrame.
- **Últimas Linhas**: Mostra as últimas `n` linhas do DataFrame.
- **Amostra Aleatória**: Exibe uma amostra aleatória de `n` linhas do DataFrame.
- **Contagem de Dados Nulos**: Conta e exibe a quantidade de valores nulos em cada coluna.
- **Contagem de Valores Únicos**: Conta e exibe a quantidade de valores únicos em cada coluna.
- **Valores Mais Comuns**: Mostra os valores mais comuns em cada coluna categórica.
- **Análise Numérica**: Gera estatísticas descritivas e histogramas para colunas numéricas.
- **Análise Categórica**: Exibe a contagem de valores para cada coluna categórica.
- **Relatório Completo**: Gera um relatório completo com todas as análises acima.

## Como Usar

1. Clone o repositório para sua máquina local.
2. Instale as dependências necessárias:
    ```bash
    pip install pandas numpy matplotlib tabulate ipython
    ```
3. Importe a classe `DataQuality`, crie uma instância passando o caminho do arquivo CSV e gere o relatório:

    ```python
    from dataquality import DataQuality

    dq = DataQuality('caminho/para/seu/arquivo.csv')
    dq.report()
  



