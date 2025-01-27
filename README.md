# Documentação do Projeto de Processamento de Dados

## Índice 

* [Índice](#índice)
* [Descrição](#descrição)
* [Tecnologia Utiliadas](#tecnologias-utiliazdas)
* [Estrutura do Projeto](#estrutura-do-projeto)
* [Preparando o Ambiente](#preparando-o-ambiente)
* [Funcionalidades Principais](#funcionalidades-principais)
* [Fluxo do Processo ETL](#fluxo-do-processo-etl)
* [Resultado Final](#resultado-final)
* [Acesse o Projeto](#acesse-o-projeto)## Índice 


## Descrição
Este projeto tem como objetivo realizar o processo de ETL (Extração, Transformação e Carregamento) de dados provenientes de arquivos JSON e CSV. Os dados de duas empresas distintas são unificados, padronizados e salvos em um novo arquivo CSV para futuras análises.

## Tecnologias Utilizadas

- WSL Windows
- Linux Ubuntu 22.04
- Jupyter Notebook
- Python 3.10
- Bibliotecas: `csv`, `json`

## Estrutura do Projeto
O projeto é composto por dois scripts principais:
1. `processamento_dados.py`: Define a classe `Dados`, que contém os métodos necessários para manipulação dos dados.
2. `main.py`: Realiza a execução do pipeline ETL utilizando a classe `Dados`.

## Preparando o Ambiente
- O projeto possui um jupyter notebook com as orientações para a preparação e configuração do ambiente de trabalho. Para acessar o notebook clique [aqui](https://github.com/FredericoSander/Criando_um_pipeline_de_dados_com_Python_e_POO/blob/main/notebooks/preparando_ambiente.ipynb).

## Funcionalidades Principais
### 1. Extração dos Dados (Extract)
- Carregamento de arquivos JSON e CSV.
- Conversão dos arquivos em listas de dicionários para manipulação.

### 2. Transformação dos Dados (Transform)
- Renomeação de colunas para padronização.
- Unificação de dados de diferentes fontes.

### 3. Carregamento dos Dados (Load)
- Exportação dos dados processados para um arquivo CSV final.

## Fluxo do Processo ETL
### Extração dos Dados
```python
from processamento_dados import Dados

path_csv = 'data_raw/dados_empresaB.csv'
path_json = 'data_raw/dados_empresaA.json'

dados_empresaA = Dados(path_json, 'json')
print(f"O primeiro arquivo carregado possui {dados_empresaA.qtd_linhas} linhas")

dados_empresaB = Dados(path_csv, 'csv')
print(f"O segundo arquivo carregado possui {dados_empresaB.qtd_linhas} linhas")
```

### Transformação dos Dados
```python
key_mapping = {
    'Nome do Item': 'Nome do Produto',
    'Classificação do Produto': 'Categoria do Produto',
    'Valor em Reais (R$)': 'Preço do Produto (R$)',
    'Quantidade em Estoque': 'Quantidade em Estoque',
    'Nome da Loja': 'Filial',
    'Data da Venda': 'Data da Venda'
}

dados_empresaB.rename_columns(key_mapping)
print(f"As colunas dos arquivos foram renomeadas para: {dados_empresaB.nome_colunas}")

dados_fusao = Dados.join(dados_empresaA, dados_empresaB)
print(f"A nova base de dados possui as seguintes colunas: {dados_fusao.nome_colunas}")
print(f"A nova base de dados possui {dados_fusao.qtd_linhas} linhas")
```

### Carregamento dos Dados
```python
path_dados_combinados = 'data_processed/dados_combinados.csv'
dados_fusao.salvando_dados(path_dados_combinados)
print(f"Seu arquivo CSV está disponível em: {path_dados_combinados}")
```

## Resultado Final
Após a execução do pipeline ETL, os dados processados são salvos em `data_processed/dados_combinados.csv`, prontos para análise.

## Acesse o Projeto

- Você pode acessar a documentação da classe dados clicando [aqui](https://github.com/FredericoSander/Criando_um_pipeline_de_dados_com_Python_e_POO/blob/main/scripts/classe_dados.py).
- Você pode acessar o script da classe dados clicando [aqui](https://github.com/FredericoSander/Criando_um_pipeline_de_dados_com_Python_e_POO/blob/main/scripts/processamento_dados.py)
- Você pode acessar a documentação do processamento de dados clicando [aqui](https://github.com/FredericoSander/Criando_um_pipeline_de_dados_com_Python_e_POO/blob/main/scripts/processamento_dados.md).
- Você pode acessar o script do processamento de dados clicando [aqui](https://github.com/FredericoSander/Criando_um_pipeline_de_dados_com_Python_e_POO/blob/main/scripts/processamento_dados.py).


## Autor
| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/136928502?s=96&v=4" width=115><br><sub>Frederico Sander</sub>](https://github.com/FredericoSander)
| :---: | 

