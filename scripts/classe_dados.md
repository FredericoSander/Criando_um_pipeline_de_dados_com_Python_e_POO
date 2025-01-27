# Documentação da Classe `Dados`


## Índice 

* [Índice](#índice)
* [Introdução](#introdução)
* [Inicialização da Classe](#inicialização-da-classe)
* [Métodos](#métodos)
* [Exemplo de Uso](#exemplo-de-uso)
* [Conclusão](#conclusão)

## Introdução
A classe `Dados` permite a manipulação de arquivos de dados nos formatos **CSV** e **JSON**, além de possibilitar a leitura de listas diretamente da memória.
Com esta classe, é possível carregar, renomear colunas, unir conjuntos de dados e exportar as informações processadas para um novo arquivo CSV.

## Inicialização da Classe
```python
Dados(path: str, tipo_dados: str)
```
### Parâmetros:
- `path` (*str*): Caminho do arquivo CSV ou JSON a ser carregado, ou uma lista em memória se `tipo_dados` for 'list'.
- `tipo_dados` (*str*): Tipo do arquivo, podendo ser `'csv'`, `'json'` ou `'list'`.

### Atributos:
- `path` (*str*): Caminho do arquivo ou indicação de que é uma lista em memória.
- `tipo_dados` (*str*): Tipo dos dados fornecidos.
- `dados` (*list*): Lista contendo os dados lidos.
- `nome_colunas` (*list*): Lista com os nomes das colunas extraídas do conjunto de dados.
- `qtd_linhas` (*int*): Número de registros lidos.

## Métodos

### `leitura_json()`
Lê dados de um arquivo JSON e retorna uma lista de dicionários.
```python
def leitura_json(self) -> list
```

### `leitura_csv()`
Lê dados de um arquivo CSV e retorna uma lista de dicionários.
```python
def leitura_csv(self) -> list
```

### `leitura_dados()`
Chama o método adequado para leitura de dados com base no tipo (`csv`, `json`, `list`).
```python
def leitura_dados(self) -> list
```

### `get_columns()`
Retorna uma lista com os nomes das colunas do conjunto de dados carregado.
```python
def get_columns(self) -> list
```

### `rename_columns(key_mapping: dict)`
Renomeia as colunas do conjunto de dados com base no dicionário `key_mapping`.
```python
def rename_columns(self, key_mapping: dict) -> None
```
- **Parâmetro:** `key_mapping` (*dict*): Dicionário com as colunas antigas como chave e os novos nomes como valores.

### `size_data()`
Retorna o número de linhas presentes no conjunto de dados.
```python
def size_data(self) -> int
```

### `join(dadosA, dadosB)`
Combina dois objetos da classe `Dados` em uma única lista de dados.
```python
def join(dadosA: Dados, dadosB: Dados) -> Dados
```
- **Parâmetros:**
  - `dadosA` (*Dados*): Primeiro conjunto de dados.
  - `dadosB` (*Dados*): Segundo conjunto de dados.
- **Retorno:** Um novo objeto `Dados` contendo os dados combinados.

### `transformando_dados_tabela()`
Transforma os dados carregados em uma estrutura tabular, incluindo cabeçalho.
```python
def transformando_dados_tabela(self) -> list
```
- **Retorno:** Lista bidimensional onde a primeira linha contém os nomes das colunas.

### `salvando_dados(path: str)`
Salva os dados transformados em formato CSV no caminho especificado.
```python
def salvando_dados(self, path: str) -> None
```
- **Parâmetro:** `path` (*str*): Caminho do arquivo onde os dados serão salvos.

## Exemplo de Uso
```python
# Criando um objeto Dados a partir de um CSV
meus_dados = Dados("dados.csv", "csv")

# Obtendo nomes das colunas
titulos = meus_dados.get_columns()
print(titulos)

# Renomeando colunas
mapa_colunas = {"nome": "Nome Completo", "idade": "Idade (anos)"}
meus_dados.rename_columns(mapa_colunas)

# Salvando os dados em um novo arquivo CSV
meus_dados.salvando_dados("novo_dados.csv")
```

## Conclusão
A classe `Dados` é uma ferramenta poderosa para manipulação de arquivos CSV e JSON, permitindo leitura, transformação e exportação dos dados de maneira eficiente. É uma solução ideal para projetos que envolvem engenharia de dados e análise de informações.

## Autor
| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/136928502?s=96&v=4" width=115><br><sub>Frederico Sander</sub>](https://github.com/FredericoSander)
| :---: | 

