# Manipulacao de dados com Pandas    

    A manipulação de dados com a biblioteca Pandas em Python é uma habilidade fundamental na engenharia de dados. Pandas oferece estruturas de dados poderosas e flexíveis, como o DataFrame, que facilitam a manipulação e análise de dados.

Aqui estão algumas operações essenciais que você pode realizar com Pandas:

### **Leitura e Escrita de Dados**

Pandas suporta vários formatos de arquivo, como CSV, Excel, JSON, SQL, entre outros.

**Leitura de Dados:**

**`pd.read_csv('arquivo.csv')`, `pd.read_excel('arquivo.xlsx')`, etc.**

**Escrita de Dados:**

**`df.to_csv('arquivo.csv')`, `df.to_excel('arquivo.xlsx')`, etc.**

### **Inspeção e Limpeza de Dados**

**Visualizar Dados:**

**`df.head()` para as primeiras linhas, `df.tail()` para as últimas.**

**Verificar Tipos de Dados:**

**`df.dtypes`**

**Estatísticas Resumidas:**

**`df.describe()`**

**Tratamento de Valores Ausentes:**

**`df.dropna()` para remover, `df.fillna(value)` para substituir.**

**Remover Duplicatas:**

**`df.drop_duplicates()`**

### **Seleção e Filtragem**

**Seleção de Colunas:**

**`df['coluna']` ou `df[['col1', 'col2']]`**

**Seleção de Linhas por Índice:**

**`df.iloc[0]` (primeira linha), `df.loc['index']` (por índice nomeado)**

**Filtragem Condicional:**

**`df[df['coluna'] > valor]`**

### **Transformações e Agregações**

**Aplicar Funções:**

**`df['coluna'].apply(lambda x: x*2)`**

**Agrupações e Resumos:**

**`df.groupby('coluna').sum()` ou `df.groupby('coluna').mean()`**

**Unir e Combinar Dados:**

**`pd.merge(df1, df2, on='coluna')`, `df1.join(df2)`, `pd.concat([df1, df2])`**

### **Manipulação de Datas e Horas**

**Conversão de Strings para Datetime:**

**`pd.to_datetime(df['coluna'])`**

**Extração de Componentes de Data:**

**`df['coluna'].dt.year`, `.dt.month`, `.dt.day`, etc.**

### **Visualização de Dados**

Pandas integra-se bem com bibliotecas de visualização como Matplotlib e Seaborn, permitindo gráficos direto dos DataFrames:

**Plotagem Básica:**

**`df.plot()`, `df['coluna'].hist()`, etc.**

**Exemplo Prático:**

```python
import pandas as pd

# Lendo um arquivo CSV
df = pd.read_csv('arquivo.csv')

# Visualizando as primeiras linhas
print(df.head())

# Filtrando dados
filtered_df = df[df['idade'] > 30]

# Agrupando e calculando a média
mean_df = df.groupby('departamento')['salario'].mean()

# Salvando os resultados
mean_df.to_csv('media_salario_por_departamento.csv')
```

---

# **Trabalhando com JSON e XML em Python**

Trabalhar com JSON e XML em Python é uma tarefa comum, especialmente na engenharia de dados, onde frequentemente se lida com diferentes formatos de dados.

Vamos abordar como você pode manipular esses dois tipos de dados em Python.

## **Trabalhando com JSON**

JSON (JavaScript Object Notation) é um formato leve de troca de dados. Em Python, você pode usar a biblioteca `json` para manipular dados JSON.

### **Lendo JSON**

```python
import json

# Lendo JSON de um arquivo
with open('dados.json', 'r') as file:
    data = json.load(file)

# Ou carregando JSON de uma string
json_string = '{"nome": "João", "idade": 30}'
data = json.loads(json_string)

data = {'nome': 'Maria', 'idade': 25}

# Escrevendo JSON em um arquivo
with open('saida.json', 'w') as file:
    json.dump(data, file)

# Convertendo para uma string JSON
json_string = json.dumps(data)
```

---

# Trabalhando com XML

XML (eXtensible Markup Language) é outro formato comumente usado para o armazenamento e transporte de dados. Em Python, a biblioteca xml.etree.ElementTree é frequentemente usada para analisar e manipular dados XML.

import xml.etree.ElementTree as ET

### Carregar e analisar um arquivo XML
tree = ET.parse('dados.xml')
root = tree.getroot()

### Navegando pelos elementos
for child in root:
    print(child.tag, child.attrib)

### Buscando elementos específicos
for elem in root.findall('tag_especifica'):
    print(elem.attrib)

### **Escrevendo XML**

```python
root = ET.Element("raiz")
doc = ET.SubElement(root, "doc")

# Adicionando elementos
campo1 = ET.SubElement(doc, "campo1")
campo1.text = "dado1"
campo2 = ET.SubElement(doc, "campo2")
campo2.text = "dado2"

# Criando uma árvore e salvando em um arquivo
tree = ET.ElementTree(root)
tree.write("saida.xml")
```

### Dicas Adicionais

Tratamento de Erros: Sempre bom usar tratamento de exceções ao ler arquivos para lidar com erros de leitura ou formatação.

Uso de Bibliotecas Avançadas: Para tarefas mais complexas, você pode considerar bibliotecas como lxml para XML e pandas para JSON (especialmente se os dados JSON estiverem em formato tabular).