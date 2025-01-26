# Documentação do Script de Processamento de Dados

## Descrição
Este script realiza a extração, transformação e carregamento de dados (ETL) de arquivos nos formatos JSON e CSV. Ele combina os dados de duas empresas distintas, realiza a padronização de colunas e salva os dados processados em um novo arquivo CSV.

## Dependências
- `processamento_dados.Dados` (classe necessária para manipulação dos dados)
- Arquivos de entrada:
  - `data_raw/dados_empresaA.json` (dados da Empresa A no formato JSON)
  - `data_raw/dados_empresaB.csv` (dados da Empresa B no formato CSV)

## Etapas do Processo

### 1. Extração dos Dados (Extract)
Carregamento dos arquivos de entrada:
```python
from processamento_dados import Dados

# Caminho dos dados
path_csv = 'data_raw/dados_empresaB.csv'
path_json = 'data_raw/dados_empresaA.json'

# Extração dos dados
dados_empresaA = Dados(path_json, 'json')
print(f"O primeiro arquivo carregado possui {dados_empresaA.qtd_linhas} linhas")

dados_empresaB = Dados(path_csv, 'csv')
print(f"O segundo arquivo carregado possui {dados_empresaB.qtd_linhas} linhas")
```

### 2. Transformação dos Dados (Transform)
Renomeação das colunas para padronização:
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
```

Fusão dos dados das duas empresas:
```python
dados_fusao = Dados.join(dados_empresaA, dados_empresaB)
print(f"A nova base de dados possui as seguintes colunas: {dados_fusao.nome_colunas}")
print(f"A nova base de dados possui {dados_fusao.qtd_linhas} linhas")
```

### 3. Carregamento dos Dados (Load)
Salvar os dados processados em um novo arquivo CSV:
```python
path_dados_combinados = 'data_processed/dados_combinados.csv'
dados_fusao.salvando_dados(path_dados_combinados)
print(f"Seu arquivo CSV está disponível em: {path_dados_combinados}")
```

## Resultado Final
Após a execução do script, um novo arquivo CSV contendo os dados combinados e padronizados estará disponível em `data_processed/dados_combinados.csv`.

## Autor
- Desenvolvido por [Seu Nome]

