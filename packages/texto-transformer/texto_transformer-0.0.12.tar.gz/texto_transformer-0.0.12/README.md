<!--- BADGES: START --->
[![Github Actions Status for osmarbraz/texto-transformer](https://github.com/osmarbraz/texto-transformer/workflows/Integra%C3%A7%C3%A3o%20continua%20em%20Python/badge.svg)](https://github.com/osmarbraz/texto-transformer/actions) 
[![GitHub - License](https://img.shields.io/github/license/osmarbraz/texto-transformer?logo=github&style=flat&color=green)][#github-license]
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/texto-transformer?logo=pypi&style=flat&color=blue)][#pypi-package]
[![PyPI - Package Version](https://img.shields.io/pypi/v/texto-transformer?logo=pypi&style=flat&color=orange)][#pypi-package]

[#github-license]: https://github.com/osmarbraz/texto-transformer/blob/master/LICENSE
[#pypi-package]: https://pypi.org/project/texto-transformer/
<!--- BADGES: END --->

# Texto-Transformer: Framework para processamento de textos utilizando modelos de linguagem baseados em Transformer

Este framework realiza o processamento de textos utilizando modelos de linguagem baseados em transformer. Permite gerar embeddings de textos, sentenças, palavras e tokens utilizando modelos de linguagem baseados em Transformer. Utiliza modelos de linguagem como BERT/Albert/DistilBERT e etc. Os embeddings de textos, sentenças e palavras podem ser consolidados utilizando as estratégias de pooling média e máximo dos tokens.

## Instalação

Recomendamos **Python 3.6**, **[Transformers 4.26.1](https://huggingface.co/transformers)**, **[PyTorch 2.0.1](https://pytorch.org)**, **[spaCy 3.5.2](https://spacy.io)**, **[SciPy 1.10.1](https://scipy.org)**, **[NumPy 1.22.4](https://numpy.org)**, **[Sentence Piece 0.1.99](https://github.com/google/sentencepiece)** e **[Protocol Buffers 3.20.3](https://protobuf.dev/)**. 

**Instalação com pip**

Para instalar o pacote utilizando o **pip**, basta executar o comando abaixo:

<pre><code>$ pip install texto-transformer</code></pre>

**Instalação dos fontes**

Você também pode clonar a versão mais recente do [repositório](https://github.com/osmarbraz/texto-transformer.git) e instalá-la diretamente do código-fonte:

<pre><code>$ pip install -e .</code></pre>

O comando deve ser executado no diretório onde foi realizado o download do repositório.

## Exemplos 

### Uso simples

````python
# Importa a classe
from textotransformer import TextoTransformer

# Instância uma objeto e baixa o modelo de linguagem
modelo = TextoTransformer("neuralmind/bert-base-portuguese-cased")

# Alguns textos a serem codificados
textos = ["Bom Dia, professor.",
          "Qual o conteúdo da prova?",
          "Vai cair tudo na prova?",
          "Aguardo uma resposta, João."]

# Recupera os embeddings consolidados dos textos
embeddings_texto = modelo.getEmbeddingTexto(textos)      

# Mostra os textos e seus embeddings
for texto, embedding in zip(textos, embeddings_texto):
    print("Texto:", texto)
    print("Embedding:", embedding)

#Resultado
#Texto: Bom Dia, professor.
#Embedding: tensor([ 1.3736e-01,  6.1996e-02,  3.2554e-01, -3.1146e-02,  3.5892e-01,...
#Texto: Qual o conteúdo da prova?
#Embedding: tensor([ 8.3348e-02, -1.8269e-01,  5.9241e-01, -9.5235e-02,  5.0978e-01,...
#Texto: Vai cair tudo na prova?
#Embedding: tensor([ 1.3447e-01,  1.1854e-01,  6.0201e-02,  1.0271e-01,  2.6321e-01,...
#Texto: Aguardo uma resposta, João.
#Embedding: tensor([ 3.7160e-02, -7.3645e-02,  3.3942e-01,  8.0847e-02,  3.8259e-01,...
````

### Recuperando embeddings de diversas granularidades

````python
# Importa a classe
from textotransformer import TextoTransformer

# Instância uma objeto e baixa o modelo de linguagem
modelo = TextoTransformer("neuralmind/bert-base-portuguese-cased")

# Texto a ser codificado
texto = "Você gosta de sorvete de manga? Sim, adoro muito."

# Recupera os embeddings consolidados do texto
embeddings_texto = modelo.getEmbeddingTexto(texto)
print("Um texto de tamanho     :",len(embeddings_texto))

# Recupera os embeddings consolidados das sentenças do texto
embeddings_sentenca = modelo.getEmbeddingSentenca(texto)
print("Quantidade de sentenças  :",len(embeddings_sentenca))
print("Cada sentença de tamanho :",len(embeddings_sentenca[0]))

# Recupera os embeddings consolidados das palavras do texto
embeddings_palavra = modelo.getEmbeddingPalavra(texto)
print("Quantidade de palavras   :",len(embeddings_palavra))
print("Cada palavra de tamanho  :",len(embeddings_palavra[0]))

# Recupera os embeddings dos tokens do texto
embeddings_token = modelo.getEmbeddingToken(texto)
print("Quantidade de tokens     :",len(embeddings_token))
print("Cada token de tamanho    :",len(embeddings_token[0]))

#Resultado
#Um texto de tamanho      : 768
#Quantidade de sentenças  : 2
#Cada sentença de tamanho : 768
#Quantidade de palavras   : 12
#Cada palavra de tamanho  : 768
#Quantidade de tokens     : 15
#Cada token de tamanho    : 768
````

**Os exemplos podem ser executados através deste notebook no GoogleColab [ExemplosTextoTransformer.ipynb](https://github.com/osmarbraz/texto-transformer/blob/main/notebooks/ExemplosTextoTransformer.ipynb).**

## Classe principal

A classe principal **TextoTransformer** carrega e cria um objeto para manipular um modelo de linguagem baseado e transformer. Permite recuperar e manipular embeddings recuperados de tokens, palavras, sentenças e textos.
     
### Parâmetros inicialização

Aqui os parâmetros a serem especificados para instanciar a classe TextoTransformer.

- `pretrained_model_name_or_path` - Se for um caminho de arquivo no disco, carrega o modelo a partir desse caminho. Se não for um caminho, ele primeiro faz o download do repositório de modelos do Huggingface com esse nome. Valor default: `neuralmind/bert-base-portuguese-cased`.
- `modelo_spacy` - Nome do modelo spaCy a ser instalado e carregado pela ferramenta de pln spaCy. Valor default 'pt_core_news_lg'.
- `abordagem_extracao_embeddings_camadas` - Especifica a abordagem padrão para a extração dos embeddings das camadas do transformer. Valor default '2'. Valores possíveis: 0-Primeira/1-Penúltima/2-Ùltima/3-Soma 4 últimas/4-Concat 4 últimas/5-Todas.
- `device` - Dispositivo (como 'cuda' / 'cpu') que deve ser usado para o processamento. Se `None`, verifica se uma GPU pode ser usada. Se a GPU estiver disponível será usada no processamento. Valor default 'None'.
    
### Métodos principais

Aqui os métodos principais para recuperar embeddings de textos, sentenças, palavras e tokens. Os métodos para recuperar os embeddings de textos, sentenças e palavras consolidados podem utilizar as estratégias de pooling média (MEAN) e máximo (MAX) dos embeddings de seus tokens.

- `getEmbeddingTexto(texto: Union[str, List[str]], estrategia_pooling: int)`
    - Retorna uma lista dos embeddings consolidados dos textos.
    - Parâmetros:
        - `texto`: Um texto ou uma lista de textos para obter os embeddings.
        - `estrategia_pooling`: Especifica a estratégia de pooling dos tokens do texto. Valores possívels 0 - MEAN ou 1 - MAX. Valor default 0(MEAN).

- `getEmbeddingSentenca(texto: Union[str, List[str]], estrategia_pooling: int)` 
    - Retorna uma lista dos embeddings consolidados das sentenças dos textos.    
    - Parâmetros:
        - `texto`: Um texto ou uma lista de textos para obter os embeddings.
        - `estrategia_pooling`: Especifica a estratégia de pooling dos tokens do texto. Valores possívels 0 - MEAN ou 1 - MAX. Valor default 0(MEAN).

- `getEmbeddingPalavra(texto: Union[str, List[str]], estrategia_pooling: int)` 
    - Retorna uma lista dos embeddings consolidados das palavras dos textos.
    - Parâmetros:
        - `texto`: Um texto ou uma lista de textos para obter os embeddings.
        - `estrategia_pooling`: Especifica a estratégia de pooling dos tokens do texto. Valores possívels 0 - MEAN ou 1 - MAX. Valor default 0(MEAN).

- `getEmbeddingToken(texto: Union[str, List[str]])` 
    - Retorna uma lista dos embeddings dos tokens dos textos.
    - Parâmetros:
        - `texto`: Um texto ou uma lista de textos para obter os embeddings. 

### Mensuração

Permite realizar a mensuração entre embeddings de diversas granularidades utilizando funções de similaridade e distância. As funções de similaridade do cosseno, produto cartesiano, distância Euclidiana e distância de Manhattan estão no pacote `mensurador.medidas`.

## Modelos Pré-treinados

Testamos o framework com os modelos Albert, BERT, DistilBERT, GTPT2, OpenAIGPT, Roberta, XLMRoberta, XLMNet e T5.

A lista completa dos modelos de linguagem pré-treinados podem ser consultados no site da [Huggingface](https://huggingface.co/models).

A lista completa dos modelos da ferramenta de PLN spaCy podem ser consultados no [site](https://spacy.io/models).

## Dependências

- transformers==4.26.1
- spacy==3.5.2
- tqdm==4.65.0
- torch==2.0.1
- scipy==1.10.1
- numpy==1.22.4
- sentencepiece==0.1.99
- protobuf==3.20.3

## Licença

Esse projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.