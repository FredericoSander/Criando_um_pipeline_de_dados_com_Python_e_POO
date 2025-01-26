from processamento_dados import Dados

# Caminho dos dados
path_csv='data_raw/dados_empresaB.csv'
path_json ='data_raw/dados_empresaA.json'

# Extract
dados_empresaA = Dados(path_json, 'json')
print(f"O arquivo primeiro arquivo carregado possui {dados_empresaA.qtd_linhas} linhas")

dados_empresaB = Dados(path_csv, 'csv')
print(f"O arquivo segundo arquivo carregado possui {dados_empresaB.qtd_linhas} linhas")

# Transform

key_mapping = { 'Nome do Item':'Nome do Produto',
                'Classificação do Produto':'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda':'Data da Venda'}


dados_empresaB.rename_columns(key_mapping)
print(f"A coluna dos arquivos foram renomeadas para: {dados_empresaB.nome_colunas}")

dados_fusao = Dados.join(dados_empresaA,dados_empresaB)
# print(dados_fusao)
print(f"A nova base de dados possui as seguintes colunas: {dados_fusao.nome_colunas}")
print(f"A nova base de dados possui {dados_fusao.qtd_linhas} linhas")

# Load
path_dados_combinados = 'data_processed/dados_combinados.csv'
dados_fusao.salvando_dados(path_dados_combinados)
print(f"Seu arquivo csv está disponíel em: {path_dados_combinados}")

