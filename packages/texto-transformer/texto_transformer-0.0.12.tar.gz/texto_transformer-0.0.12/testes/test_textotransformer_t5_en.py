# Import das bibliotecas.

# Biblioteca de logging
import logging
# Biblioteca de testes unitários
import unittest
# Biblioteca de aprendizado de máquina
import torch 

# Biblioteca texto-transformer
from textotransformer.textotransformer import TextoTransformer
from textotransformer.modelo.transformert5 import TransformerT5
from textotransformer.mensurador.medidas import similaridadeCosseno, produtoEscalar, distanciaEuclidiana, distanciaManhattan
from textotransformer.util.utiltexto import getIndexTokenTexto

# Objeto de logger
logger = logging.getLogger(__name__)

class TestTextTransformer_t5_en(unittest.TestCase):
    
    # Inicialização do modelo para os testes
    @classmethod     
    def setUpClass(self):
        logger.info("Inicializando o modelo para os métodos de teste")
        # Instancia um objeto da classe TextoTransformer e recupera o MCL especificado
        self.modelo = TextoTransformer("t5-small", 
                                       modelo_spacy="en_core_web_sm") 
    
    # Testes TextoTransformer_t5
    def test_textotransformer(self):
        logger.info("Testando o construtor de TextoTransformer_t5")
                
        self.assertIsNotNone(self.modelo)
        self.assertIsInstance(self.modelo.getTransformer(), TransformerT5)
    
    # Testes removeTokensEspeciais
    def test_removeTokensEspeciais(self):
        logger.info("Testando o removeTokensEspeciais")
        
        # Valores de entrada                
        lista_tokens = ['I', 'like', 'mango', 'ice', 'cream', '.', '</s>']
        
        # Valores de saída
        lista_tokens_saida = self.modelo.getTransformer().removeTokensEspeciais(lista_tokens)
        
        # Lista esperada
        lista_tokens_esperado = ['I', 'like', 'mango', 'ice', 'cream', '.']
        
        # Testa as listas
        self.assertListEqual(lista_tokens_saida, lista_tokens_esperado) 
    
    # Testes getSaidaRede 
    def test_getSaidaRede(self):
        logger.info("Testando o getSaidaRede")
        
        # Valores de entrada                
        texto = "I play bass in a jazz band."
        
        # Tokeniza o texto
        texto_tokenizado = self.modelo.getTransformer().tokenize(texto)
        
        # Valores de saída
        saida = self.modelo.getSaidaRede(texto_tokenizado)
        
        # Testa o tamanho do dicionário
        self.assertEqual(len(saida), 6) 
        
    # Testes getSaidaRedeCamada
    def test_getSaidaRedeCamada(self):
        logger.info("Testando o getSaidaRedeCamada")
         
        # Valores de entrada       
        texto = "I play bass in a jazz band."
        
        texto_tokenizado = self.modelo.getTransformer().tokenize(texto)
        
        # Valores de saída
        saida = self.modelo.getSaidaRedeCamada(texto_tokenizado, 2) # Camada 2 - Ultima camada dos transformers
        
        # Testa o tamanho do dicionário
        self.assertEqual(len(saida), 8)
    
    # Testes getCodificacaoCompleta string
    def test_getCodificacaoCompleta_string(self):
        logger.info("Testando o getCodificacaoCompleta com string")
        
        # Valores de entrada        
        texto = "I play bass in a jazz band."

        saida = self.modelo.getCodificacaoCompleta(texto)
        
        # Testa o tamanho do dicionário
        self.assertEqual(len(saida), 6)
        
        # Testa o nome das chaves
        self.assertTrue("token_embeddings" in saida)
        self.assertTrue("input_ids" in saida)
        self.assertTrue("attention_mask" in saida)
        self.assertTrue("tokens_texto_mcl" in saida)
        self.assertTrue("texto_original" in saida)
        self.assertTrue("all_layer_embeddings" in saida)
        
        # Testa a saida dos valores das chaves
        self.assertEqual(len(saida['token_embeddings']), 10)
        self.assertEqual(len(saida['input_ids']), 10)
        self.assertEqual(len(saida['attention_mask']), 10)
        self.assertEqual(len(saida['tokens_texto_mcl']), 10)        
        self.assertEqual(saida['texto_original'], texto)
        self.assertEqual(len(saida['all_layer_embeddings']), 6) # Camadas
        self.assertEqual(len(saida['all_layer_embeddings'][0]), 10) # tokens
        self.assertEqual(len(saida['all_layer_embeddings'][0][0]), 512) # dimensões
        
        # Testa o tipo das saida dos valores das chaves                
        self.assertIsInstance(saida['token_embeddings'], torch.Tensor)
        self.assertIsInstance(saida['token_embeddings'][0], torch.Tensor)
        
        self.assertIsInstance(saida['all_layer_embeddings'], list)
        self.assertIsInstance(saida['all_layer_embeddings'][0], torch.Tensor)
        self.assertIsInstance(saida['all_layer_embeddings'][0][0], torch.Tensor)
                
    # Testes getCodificacaoCompleta lista de string
    def test_getCodificacaoCompleta_list_string(self):
        logger.info("Testando o getCodificacaoCompleta com lista de strings")
        
        # Valores de entrada        
        texto = ["Fresh sea bass is a great delicacy.","I play bass in a jazz band."]

        # Valores de saída
        saida = self.modelo.getCodificacaoCompleta(texto)
        
        # Testa o tamanho do dicionário
        self.assertEqual(len(saida), 6)
        
        # Testa o nome das chaves
        self.assertTrue("token_embeddings" in saida)
        self.assertTrue("input_ids" in saida)
        self.assertTrue("attention_mask" in saida)
        self.assertTrue("tokens_texto_mcl" in saida)
        self.assertTrue("texto_original" in saida)
        self.assertTrue("all_layer_embeddings" in saida)
                
        # Testa a saida dos valores das chaves
        self.assertEqual(len(saida['token_embeddings']), 2) # Textos
        self.assertEqual(len(saida['token_embeddings'][0]), 12) # tokens
        self.assertEqual(len(saida['token_embeddings'][0][0]), 512) # embeddings
        self.assertEqual(len(saida['token_embeddings'][1]), 10) # tokens
        self.assertEqual(len(saida['token_embeddings'][1][0]), 512) # embeddings
        self.assertEqual(len(saida['input_ids']), 2)
        self.assertEqual(len(saida['attention_mask']), 2)        
        self.assertEqual(len(saida['tokens_texto_mcl']), 2)
        self.assertEqual(saida['texto_original'][0], texto[0])
        self.assertEqual(saida['texto_original'][1], texto[1])
        self.assertEqual(len(saida['all_layer_embeddings']), 2) # Textos
        self.assertEqual(len(saida['all_layer_embeddings'][0]), 6) # Camadas do transformer
        self.assertEqual(len(saida['all_layer_embeddings'][0][0]), 12) # 12 tokens
        self.assertEqual(len(saida['all_layer_embeddings'][0][0][0]), 512) # embeddings
        self.assertEqual(len(saida['all_layer_embeddings'][1][0]), 10) # 10 tokens
        self.assertEqual(len(saida['all_layer_embeddings'][1][0][0]), 512) # embeddings
                
        # Testa o tipo das saida dos valores das chaves        
        self.assertIsInstance(saida['token_embeddings'], list)
        self.assertIsInstance(saida['token_embeddings'][0], torch.Tensor)
        self.assertIsInstance(saida['token_embeddings'][0][0], torch.Tensor)
        self.assertIsInstance(saida['token_embeddings'][1][0], torch.Tensor)
        
        self.assertIsInstance(saida['all_layer_embeddings'], list)
        self.assertIsInstance(saida['all_layer_embeddings'][0], list)
        self.assertIsInstance(saida['all_layer_embeddings'][0][0], torch.Tensor)
        self.assertIsInstance(saida['all_layer_embeddings'][0][0][0], torch.Tensor)
        self.assertIsInstance(saida['all_layer_embeddings'][1], list)
        self.assertIsInstance(saida['all_layer_embeddings'][1][0], torch.Tensor)
        self.assertIsInstance(saida['all_layer_embeddings'][1][0][0], torch.Tensor)
            
    # Testes getCodificacao
    def test_getCodificacao_string(self):
        logger.info("Testando o getCodificacao(texto)")
        
        # Valores de entrada
        texto = "Adoro sorvete de manga."
        
        # Valores de saída
        saida = self.modelo.getCodificacao(texto)
        
        # Testa o tamanho do dicionário
        self.assertEqual(len(saida), 4) 
        
       # Testa a saida dos valores das chaves
        self.assertTrue("tokens_texto_mcl" in saida)
        self.assertTrue("token_embeddings" in saida)
        self.assertTrue("input_ids" in saida)
        self.assertTrue("texto_original" in saida)
    
    # Testes getCodificacaoGranularidade0
    def test_getCodificacao_granularidade_0(self):
        logger.info("Testando o getCodificacao(texto,granularidade_texto=0)")
        
        # Valores de entrada
        texto = "Adoro sorvete de manga."
        
        # Valores de saída
        saida = self.modelo.getCodificacao(texto,granularidade_texto=0)
        
        # Testa o tamanho do dicionário
        self.assertEqual(len(saida), 4) 
        
        # Testa o nome das chaves
        self.assertTrue("tokens_texto_mcl" in saida)
        self.assertTrue("token_embeddings" in saida)
        self.assertTrue("input_ids" in saida)
        self.assertTrue("texto_original" in saida)

    # Testes getCodificacaoTexto string
    def test_getCodificacaoTexto_string(self):
        logger.info("Testando o getCodificacaoTexto com string")             
        
        # Valores de entrada
        texto = "Adoro sorvete de manga."
        
        # Valores de saída
        saida = self.modelo.getCodificacaoTexto(texto)
        
        # Testa o tamanho do dicionário
        self.assertEqual(len(saida), 4) 
        
        # Testa o nome das chaves
        self.assertTrue("texto_original" in saida)
        self.assertTrue("tokens_texto_mcl" in saida)        
        self.assertTrue("texto_embeddings_MEAN" in saida)
        self.assertTrue("texto_embeddings_MAX" in saida)
                
        # Testa a saida dos valores das chaves
        self.assertEqual(len(saida['texto_original']), 23)
        self.assertEqual(len(saida['tokens_texto_mcl']), 11)
        # Testa a quantidade de embeddings
        self.assertEqual(len(saida['texto_embeddings_MEAN']), 512)
        self.assertEqual(len(saida['texto_embeddings_MAX']), 512)
        self.assertEqual(saida['texto_original'], texto)
        
        # Testa o tipo das saida dos valores das chaves        
        self.assertIsInstance(saida['texto_embeddings_MEAN'], torch.Tensor)        
        self.assertIsInstance(saida['texto_embeddings_MAX'], torch.Tensor)
        
    # Testes getCodificacaoTexto lista_string
    def test_getCodificacaoTexto_lista_string(self):
        logger.info("Testando o getCodificacaoTexto com lista de string")             
        
        # Valores de entrada
        texto = ["Fresh sea bass is a great delicacy.","I play bass in a jazz band."]
        
        # Valores de saída
        saida = self.modelo.getCodificacaoTexto(texto)
        
        # Testa o tamanho do dicionário
        self.assertEqual(len(saida), 4) 
        
        # Testa o nome das chaves
        self.assertTrue("texto_original" in saida)
        self.assertTrue("tokens_texto_mcl" in saida)        
        self.assertTrue("texto_embeddings_MEAN" in saida)
        self.assertTrue("texto_embeddings_MAX" in saida)
                
        # Testa a saida dos valores das chaves
        self.assertEqual(len(saida['texto_original']), 2)
        self.assertEqual(len(saida['tokens_texto_mcl']), 2)
        # Testa a quantidade de embeddings
        self.assertEqual(len(saida['texto_embeddings_MEAN']), 2)
        self.assertEqual(len(saida['texto_embeddings_MAX']), 2)
        self.assertEqual(saida['texto_original'][0], texto[0])
        self.assertEqual(saida['texto_original'][1], texto[1])
        
        # Testa o tipo das saida dos valores das chaves        
        self.assertIsInstance(saida['texto_embeddings_MEAN'], list)
        self.assertIsInstance(saida['texto_embeddings_MEAN'][0], torch.Tensor)
        self.assertIsInstance(saida['texto_embeddings_MEAN'][1], torch.Tensor)
        
        self.assertIsInstance(saida['texto_embeddings_MAX'], list)
        self.assertIsInstance(saida['texto_embeddings_MAX'][0], torch.Tensor)
        self.assertIsInstance(saida['texto_embeddings_MAX'][1], torch.Tensor)        

    # Testes getCodificacaoSentenca string
    def test_getCodificacaoSentenca_string(self):
        logger.info("Testando o getCodificacaoSentenca com string")             
        
        # Valores de entrada
        texto = "Fresh sea bass is a great delicacy. I play bass in a jazz band."
        
        # Valores de saída
        saida = self.modelo.getCodificacaoSentenca(texto)
        
        # Testa o tamanho do dicionário
        self.assertEqual(len(saida), 5) 
        
        # Testa o nome das chaves
        self.assertTrue("texto_original" in saida)
        self.assertTrue("tokens_texto_mcl" in saida)
        self.assertTrue("sentencas_texto" in saida)
        self.assertTrue("sentenca_embeddings_MEAN" in saida)
        self.assertTrue("sentenca_embeddings_MAX" in saida)
                
        # Testa a saida dos valores das chaves        
        self.assertEqual(len(saida['tokens_texto_mcl']), 20)
        self.assertEqual(len(saida['sentencas_texto']), 2)
        # Testa a quantidade de embeddings
        self.assertEqual(len(saida['sentenca_embeddings_MEAN']), 2)
        self.assertEqual(len(saida['sentenca_embeddings_MAX']), 2)
        self.assertEqual(saida['texto_original'], texto)
        
        # Testa o tipo das saida dos valores das chaves        
        self.assertIsInstance(saida['sentenca_embeddings_MEAN'], list)
        self.assertIsInstance(saida['sentenca_embeddings_MEAN'][0], torch.Tensor)
        
        self.assertIsInstance(saida['sentenca_embeddings_MAX'], list)
        self.assertIsInstance(saida['sentenca_embeddings_MAX'][0], torch.Tensor)

    # Testes getCodificacaoSentenca lista string
    def test_getCodificacaoSentenca_lista_string(self):
        logger.info("Testando o getCodificacaoSentenca com lista de string")             
        
        # Valores de entrada                
        texto = ["Fresh sea bass is a great delicacy. I play bass in a jazz band.", "Good morning."]
        
        # Valores de saída
        saida = self.modelo.getCodificacaoSentenca(texto)
        
        # Testa o tamanho do dicionário
        self.assertEqual(len(saida), 5) 
        
        # Testa o nome das chaves
        self.assertTrue("texto_original" in saida)
        self.assertTrue("tokens_texto_mcl" in saida)
        self.assertTrue("sentencas_texto" in saida)
        self.assertTrue("sentenca_embeddings_MEAN" in saida)
        self.assertTrue("sentenca_embeddings_MAX" in saida)
                
        # Testa a saida dos valores das chaves        
        self.assertEqual(len(saida['tokens_texto_mcl']), 2)
        self.assertEqual(len(saida['tokens_texto_mcl'][0]), 20)
        self.assertEqual(len(saida['tokens_texto_mcl'][1]), 3)
        self.assertEqual(len(saida['sentencas_texto']), 2)
        self.assertEqual(len(saida['sentencas_texto'][0]), 2)
        self.assertEqual(len(saida['sentencas_texto'][1]), 1)
        
        # Testa a quantidade de embeddings
        self.assertEqual(len(saida['sentenca_embeddings_MEAN']), 2)
        self.assertEqual(len(saida['sentenca_embeddings_MEAN'][0]), 2)
        self.assertEqual(len(saida['sentenca_embeddings_MEAN'][1]), 1)
        self.assertEqual(len(saida['sentenca_embeddings_MAX']), 2)
        self.assertEqual(len(saida['sentenca_embeddings_MAX'][0]), 2)
        self.assertEqual(len(saida['sentenca_embeddings_MAX'][1]), 1)
        self.assertEqual(saida['texto_original'], texto)
        
        # Testa o tipo das saida dos valores das chaves        
        self.assertIsInstance(saida['sentenca_embeddings_MEAN'], list)
        self.assertIsInstance(saida['sentenca_embeddings_MEAN'][0], list)
        self.assertIsInstance(saida['sentenca_embeddings_MEAN'][0][0], torch.Tensor)
        self.assertIsInstance(saida['sentenca_embeddings_MEAN'][0][1], torch.Tensor)
        self.assertIsInstance(saida['sentenca_embeddings_MEAN'][1], list)
        self.assertIsInstance(saida['sentenca_embeddings_MEAN'][1][0], torch.Tensor)
                
        self.assertIsInstance(saida['sentenca_embeddings_MAX'], list)
        self.assertIsInstance(saida['sentenca_embeddings_MAX'][0], list)
        self.assertIsInstance(saida['sentenca_embeddings_MAX'][0][0], torch.Tensor)
        self.assertIsInstance(saida['sentenca_embeddings_MAX'][0][1], torch.Tensor)
        self.assertIsInstance(saida['sentenca_embeddings_MAX'][1], list)
        self.assertIsInstance(saida['sentenca_embeddings_MAX'][1][0], torch.Tensor)

    # Testes getCodificacaoPalavraExcecao string
    def test_getCodificacaoPalavraExcecao_string(self):
        logger.info("Testando o getCodificacaoPalavraExcecao com string")             
        
        # Valores de entrada
        texto = "I am 1° place in the 100 meter dash."
        # A ferramenta de PLN tokeniza 1o em 2 tokens.
        
        # Valores de saída
        saida = self.modelo.getCodificacaoPalavra(texto)
        
        # Testa o tamanho do dicionário
        self.assertEqual(len(saida), 8) 
        
        # Testa o nome das chaves
        self.assertTrue("texto_original" in saida)
        self.assertTrue("tokens_texto" in saida)
        self.assertTrue("tokens_texto_mcl" in saida)
        self.assertTrue("tokens_oov_texto_mcl" in saida)
        self.assertTrue("tokens_texto_pln" in saida)
        self.assertTrue("pos_texto_pln" in saida)
        self.assertTrue("palavra_embeddings_MEAN" in saida)
        self.assertTrue("palavra_embeddings_MAX" in saida)
                
        # Testa a saida dos valores das chaves
        self.assertEqual(len(saida['tokens_texto']), 11)
        self.assertListEqual(saida['tokens_texto'], ['I', 'am', '1', '°', 'place', 'in', 'the', '100', 'meter', 'dash', '.'])
        self.assertEqual(len(saida['tokens_texto_mcl']), 13) # O MCL gera mais tokens que a ferramenta de PLN
        self.assertListEqual(saida['tokens_texto_mcl'], ['▁I', '▁am' , '▁1', '°', '▁place', '▁in', '▁the', '▁100', '▁', 'meter', '▁das', 'h', '.'])
        self.assertEqual(len(saida['tokens_oov_texto_mcl']), 11)
        self.assertListEqual(saida['tokens_oov_texto_mcl'], [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0])
        self.assertEqual(len(saida['tokens_texto_pln']), 11)
        self.assertListEqual(saida['tokens_texto_pln'], ['I', 'am', '1', '°', 'place', 'in', 'the', '100', 'meter', 'dash', '.'])
        self.assertEqual(len(saida['pos_texto_pln']), 11)
        self.assertListEqual(saida['pos_texto_pln'], ['PRON', 'AUX', 'NUM', 'NUM', 'NOUN', 'ADP', 'DET', 'NUM', 'NOUN', 'NOUN', 'PUNCT'])
        # Testa a quantidade de embeddings
        self.assertEqual(len(saida['palavra_embeddings_MEAN']), 11)
        self.assertEqual(len(saida['palavra_embeddings_MAX']), 11)
        # Testa o valor do texto
        self.assertEqual(saida['texto_original'], texto)
        
        # Testa o tipo das saida dos valores das chaves        
        self.assertIsInstance(saida['palavra_embeddings_MEAN'], list)
        self.assertIsInstance(saida['palavra_embeddings_MEAN'][0], torch.Tensor)
        
        self.assertIsInstance(saida['palavra_embeddings_MAX'], list)
        self.assertIsInstance(saida['palavra_embeddings_MAX'][0], torch.Tensor)

    # Testes getCodificacaoPalavraExcecaoMaior string
    def test_getCodificacaoPalavraExcecaoMaior_string(self):
        logger.info("Testando o getCodificacaoPalavraExcecaoMaior com string")             
        
        # Valores de entrada
        texto = "I have lived on Main St. for a long time."
        # A ferramenta de PLN tokeniza St. em 1 token.
        # A ferramenta de MCL tokeniza St. em 2 tokens.
        
        # Valores de saída
        saida = self.modelo.getCodificacaoPalavra(texto, dic_excecao = {"St.":2,})
        
        # Testa o tamanho do dicionário
        self.assertEqual(len(saida), 8) 
        
        # Testa o nome das chaves
        self.assertTrue("texto_original" in saida)
        self.assertTrue("tokens_texto" in saida)
        self.assertTrue("tokens_texto_mcl" in saida)
        self.assertTrue("tokens_oov_texto_mcl" in saida)
        self.assertTrue("tokens_texto_pln" in saida)
        self.assertTrue("pos_texto_pln" in saida)
        self.assertTrue("palavra_embeddings_MEAN" in saida)
        self.assertTrue("palavra_embeddings_MAX" in saida)
                
        # Testa a saida dos valores das chaves
        self.assertEqual(len(saida['tokens_texto']), 11)
        self.assertListEqual(saida['tokens_texto'], ['I', 'have', 'lived', 'on', 'Main', 'St.', 'for', 'a', 'long', 'time', '.'])
        self.assertEqual(len(saida['tokens_texto_mcl']), 13) # O MCL gera mais tokens que a ferramenta de PLN
        self.assertListEqual(saida['tokens_texto_mcl'], ['▁I', '▁have', '▁lived', '▁on', '▁Main', '▁St', '.', '▁for','▁', 'a', '▁long', '▁time', '.'])
        self.assertEqual(len(saida['tokens_oov_texto_mcl']), 11)
        self.assertListEqual(saida['tokens_oov_texto_mcl'], [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0])
        self.assertEqual(len(saida['tokens_texto_pln']), 11)
        self.assertListEqual(saida['tokens_texto_pln'], ['I', 'have', 'lived', 'on', 'Main', 'St.', 'for', 'a', 'long', 'time', '.'])
        self.assertEqual(len(saida['pos_texto_pln']), 11)
        self.assertListEqual(saida['pos_texto_pln'], ['PRON', 'AUX', 'VERB', 'ADP', 'PROPN', 'PROPN', 'ADP', 'DET', 'ADJ', 'NOUN', 'PUNCT'])
        # Testa a quantidade de embeddings
        self.assertEqual(len(saida['palavra_embeddings_MEAN']), 11)
        self.assertEqual(len(saida['palavra_embeddings_MAX']), 11)
        # Testa o valor do texto
        self.assertEqual(saida['texto_original'], texto)
        
        # Testa o tipo das saida dos valores das chaves        
        self.assertIsInstance(saida['palavra_embeddings_MEAN'], list)
        self.assertIsInstance(saida['palavra_embeddings_MEAN'][0], torch.Tensor)
        
        self.assertIsInstance(saida['palavra_embeddings_MAX'], list)
        self.assertIsInstance(saida['palavra_embeddings_MAX'][0], torch.Tensor)

    # Testes getCodificacaoPalavra string
    def test_getCodificacaoPalavra_string(self):
        logger.info("Testando o getCodificacaoPalavra com strings")              
        
        # Valores de entrada
        texto = "I play bass in a jazz band."
        
        # Valores de saída
        saida = self.modelo.getCodificacaoPalavra(texto)
        
        # Testa o tamanho do dicionário
        self.assertEqual(len(saida), 8) 
        
        # Testa o nome das chaves
        self.assertTrue("texto_original" in saida)
        self.assertTrue("tokens_texto" in saida)
        self.assertTrue("tokens_texto_mcl" in saida)
        self.assertTrue("tokens_oov_texto_mcl" in saida)
        self.assertTrue("tokens_texto_pln" in saida)
        self.assertTrue("pos_texto_pln" in saida)
        self.assertTrue("palavra_embeddings_MEAN" in saida)
        self.assertTrue("palavra_embeddings_MAX" in saida)
                
        # Testa a saida dos valores das chaves
        self.assertEqual(len(saida['tokens_texto']), 8)
        self.assertEqual(len(saida['tokens_texto_mcl']), 9)
        self.assertEqual(len(saida['tokens_oov_texto_mcl']), 8)
        self.assertEqual(len(saida['tokens_texto_pln']), 8)
        self.assertEqual(len(saida['pos_texto_pln']), 8)
        # Testa a quantidade de embeddings
        self.assertEqual(len(saida['palavra_embeddings_MEAN']), 8)
        self.assertEqual(len(saida['palavra_embeddings_MAX']), 8)
        # Testa o valor do texto
        self.assertEqual(saida['texto_original'], texto)
        # Testa as palavras fora do vocabulário
        self.assertListEqual(saida['tokens_oov_texto_mcl'], [0, 0, 0, 0, 1, 0, 0, 0])
        
        # Testa o tipo das saida dos valores das chaves        
        self.assertIsInstance(saida['palavra_embeddings_MEAN'], list)
        self.assertIsInstance(saida['palavra_embeddings_MEAN'][0], torch.Tensor)
        
        self.assertIsInstance(saida['palavra_embeddings_MAX'], list)
        self.assertIsInstance(saida['palavra_embeddings_MAX'][0], torch.Tensor)
        
    # Testes getCodificacaoPalavra lista de string
    def test_getCodificacaoPalavra_lista_string(self):
        logger.info("Testando o getCodificacaoPalavra lista com string")
        
        # Valores de entrada
        texto = ["Fresh sea bass is a great delicacy.","I play bass in a jazz band."]
                
        # Valores de saída
        saida = self.modelo.getCodificacaoPalavra(texto)
        
        # Testa o tamanho do dicionário
        self.assertEqual(len(saida), 8)
                
        # Testa o nome das chaves
        self.assertTrue("texto_original" in saida)
        self.assertTrue("tokens_texto" in saida)
        self.assertTrue("tokens_texto_mcl" in saida)
        self.assertTrue("tokens_oov_texto_mcl" in saida)
        self.assertTrue("tokens_texto_pln" in saida)
        self.assertTrue("pos_texto_pln" in saida)
        self.assertTrue("palavra_embeddings_MEAN" in saida)
        self.assertTrue("palavra_embeddings_MAX" in saida)
        
        # Testa a saida dos valores das chaves
        # Testa a quantidade de palavras
        self.assertEqual(len(saida['tokens_texto']), 2)
        self.assertEqual(len(saida['tokens_texto'][0]), 8)
        self.assertEqual(len(saida['tokens_texto'][1]), 8)
        # Testa a quantidade de textos
        self.assertEqual(len(saida['tokens_texto_mcl']), 2)
        # Testa a quantidade de tokens das textos
        self.assertEqual(len(saida['tokens_texto_mcl'][0]), 11)
        self.assertEqual(len(saida['tokens_texto_mcl'][1]), 9)
        # Testa a quantidade de embeddings
        self.assertEqual(len(saida['palavra_embeddings_MEAN']), 2)
        # Testa a quantidade de de embeddings
        self.assertEqual(len(saida['palavra_embeddings_MEAN'][0]), 8)
        self.assertEqual(len(saida['palavra_embeddings_MEAN'][1]), 8)        
        # Testa a quantidade de embeddings
        self.assertEqual(len(saida['palavra_embeddings_MAX']), 2)
        # Testa a quantidade de de embeddings
        self.assertEqual(len(saida['palavra_embeddings_MAX'][0]), 8)
        self.assertEqual(len(saida['palavra_embeddings_MAX'][1]), 8)
        
        # Testa a quantidade de textos
        self.assertEqual(len(saida['texto_original']), 2)
        # Testa o valor dos textos
        self.assertEqual(saida['texto_original'][0], texto[0])
        self.assertEqual(saida['texto_original'][1], texto[1])
        # Testa as palavras fora do vocabulário
        self.assertListEqual(saida['tokens_oov_texto_mcl'][0], [0, 0, 0, 0, 1, 0, 1, 0])
        self.assertListEqual(saida['tokens_oov_texto_mcl'][1], [0, 0, 0, 0, 1, 0, 0, 0])
        
        # Testa o tipo das saida dos valores das chaves      
        # MEAN  
        self.assertIsInstance(saida['palavra_embeddings_MEAN'], list)
        # Tipo do primeiro texto
        self.assertIsInstance(saida['palavra_embeddings_MEAN'][0], list)
        # Tipo do segundo texto
        self.assertIsInstance(saida['palavra_embeddings_MEAN'][1], list)
        # Tipo dos elementos da lista do primeiro texto
        self.assertIsInstance(saida['palavra_embeddings_MEAN'][0][0], torch.Tensor)
        # Tipo dos elementos da lista do segundo texto
        self.assertIsInstance(saida['palavra_embeddings_MEAN'][1][0], torch.Tensor) 
        # MAX
        self.assertIsInstance(saida['palavra_embeddings_MAX'], list)
        # Tipo do primeiro texto
        self.assertIsInstance(saida['palavra_embeddings_MAX'][0], list)
        # Tipo do segundo texto
        self.assertIsInstance(saida['palavra_embeddings_MAX'][1], list)
        # Tipo dos elementos da lista do primeiro texto
        self.assertIsInstance(saida['palavra_embeddings_MAX'][0][0], torch.Tensor)
        # Tipo dos elementos da lista do segundo texto
        self.assertIsInstance(saida['palavra_embeddings_MAX'][1][0], torch.Tensor)          
             
    # Testes getCodificacaoToken string
    def test_getCodificacaoToken_string(self):
        logger.info("Testando o getCodificacaoToken com string")
        
        # Valores de entrada
        texto = "I play bass in a jazz band."
        
        # Valores de saída
        saida = self.modelo.getCodificacaoToken(texto)
        
        # Testa o tamanho do dicionário
        self.assertEqual(len(saida), 4) 
        
        # Testa o nome das chaves
        self.assertTrue("tokens_texto_mcl" in saida)
        self.assertTrue("token_embeddings" in saida)
        self.assertTrue("input_ids" in saida)
        self.assertTrue("texto_original" in saida)
        
        # Testa a saida dos valores das chaves
        self.assertEqual(len(saida['tokens_texto_mcl']), 9)
        self.assertEqual(len(saida['token_embeddings']), 9)
        self.assertEqual(len(saida['input_ids']), 9)
        self.assertEqual(saida['texto_original'], texto)
        
        # Testa o tipo das saida dos valores das chaves        
        self.assertIsInstance(saida['token_embeddings'], list)
        self.assertIsInstance(saida['token_embeddings'][0], torch.Tensor)        
        
    # Testes getCodificacaoToken lista de string
    def test_getCodificacaoToken_lista_string(self):
        logger.info("Testando o getCodificacaoToken lista com strings")
        
        # Valores de entrada
        texto = ["Fresh sea bass is a great delicacy.","I play bass in a jazz band."]
        
        # Valores de saída
        saida = self.modelo.getCodificacaoToken(texto)
        
        # Testa o tamanho do dicionário
        self.assertEqual(len(saida), 4)
                
         # Testa o nome das chaves
        self.assertTrue("tokens_texto_mcl" in saida)
        self.assertTrue("token_embeddings" in saida)
        self.assertTrue("input_ids" in saida)
        self.assertTrue("texto_original" in saida)
        
        # Testa a saida dos valores das chaves
        # Testa a quantidade de textos
        self.assertEqual(len(saida['tokens_texto_mcl']), 2)
        # Testa a quantidade de tokens das textos
        self.assertEqual(len(saida['tokens_texto_mcl'][0]), 11)
        self.assertEqual(len(saida['tokens_texto_mcl'][1]), 9)
        # Testa a quantidade de ids
        self.assertEqual(len(saida['input_ids']), 2)
        # Testa a quantidade de tokens das textos
        self.assertEqual(len(saida['input_ids'][0]), 11)
        self.assertEqual(len(saida['input_ids'][1]), 9)
        # Testa a quantidade de textos
        self.assertEqual(len(saida['token_embeddings']), 2)
        # Testa a quantidade de tokens das textos
        self.assertEqual(len(saida['token_embeddings'][0]), 11)
        self.assertEqual(len(saida['token_embeddings'][1]), 9)
        # Testa a quantidade de textos
        self.assertEqual(len(saida['texto_original']), 2)
        # Testa o valor dos textos
        self.assertEqual(saida['texto_original'][0], texto[0])
        self.assertEqual(saida['texto_original'][1], texto[1])
        
        # Testa o tipo das saida dos valores das chaves        
        self.assertIsInstance(saida['token_embeddings'], list)
        # Tipo do primeiro texto
        self.assertIsInstance(saida['token_embeddings'][0], list)
        # Tipo do segundo texto
        self.assertIsInstance(saida['token_embeddings'][1], list)
        # Tipo dos elementos da lista do primeiro texto
        self.assertIsInstance(saida['token_embeddings'][0][0], torch.Tensor)
        # Tipo dos elementos da lista do segundo texto
        self.assertIsInstance(saida['token_embeddings'][1][0], torch.Tensor)
    
    # Testes getMedidasTexto
    def test_getMedidasTexto(self):
        logger.info("Testando o getMedidasTexto(texto)")
        
        # Valores de entrada
        texto = ["Fresh sea bass is a great delicacy.","I play bass in a jazz band."]

        # Valores de saída
        saida = self.modelo.getMedidasTexto(texto)
        
        # Valores esperados
        CcosEsperado = 0.3873968720436096
        CproEsperado = 1.234673261642456
        CeucEsperado = 1.980639934539795
        CmanEsperado = 34.53952407836914
                       
        # Testa o nome das chaves
        self.assertTrue("cos" in saida)
        self.assertTrue("pro" in saida)
        self.assertTrue("euc" in saida)
        self.assertTrue("man" in saida)
                       
        # Compara somente n casas decimais
        casas_decimais = 3
        self.assertAlmostEqual(saida['cos'], CcosEsperado, places=casas_decimais)
        self.assertAlmostEqual(saida['pro'], CproEsperado, places=casas_decimais)
        self.assertAlmostEqual(saida['euc'], CeucEsperado, places=casas_decimais)
        self.assertAlmostEqual(saida['man'], CmanEsperado, places=casas_decimais) 
        
    # Testes getMedidasTextoPalavraRelevante_0
    def test_getMedidasTexto_PalavraRelevante_0(self):
        logger.info("Testando o getMedidasTexto(texto, palavra_relevante=0)")
        
        # Valores de entrada
        texto = ["Fresh sea bass is a great delicacy.","I play bass in a jazz band."]

        # Valores de saída
        saida = self.modelo.getMedidasTexto(texto, palavra_relevante=0)
        
        # Valores esperados
        CcosEsperado = 0.3873968720436096
        CproEsperado = 1.234673261642456
        CeucEsperado = 1.980639934539795
        CmanEsperado = 34.53952407836914
                       
        # Testa o nome das chaves
        self.assertTrue("cos" in saida)
        self.assertTrue("pro" in saida)
        self.assertTrue("euc" in saida)
        self.assertTrue("man" in saida)
                       
        # Compara somente n casas decimais
        casas_decimais = 3
        self.assertAlmostEqual(saida['cos'], CcosEsperado, places=casas_decimais)
        self.assertAlmostEqual(saida['pro'], CproEsperado, places=casas_decimais)
        self.assertAlmostEqual(saida['euc'], CeucEsperado, places=casas_decimais)
        self.assertAlmostEqual(saida['man'], CmanEsperado, places=casas_decimais) 
        
    # Testes getMedidasTextoPalavraRelevante_1
    def test_getMedidasTexto_PalavraRelevante_1(self):
        logger.info("Rodando getMedidasTexto(texto, palavra_relevante=1)")
        
        # Valores de entrada
        texto = ["Fresh sea bass is a great delicacy.","I play bass in a jazz band."]

        # Valores de saída
        saida = self.modelo.getMedidasTexto(texto, palavra_relevante=1)
        
        # Valores esperados
        CcosEsperado = 0.3386894166469574
        CproEsperado = 1.5117847919464111
        CeucEsperado = 2.458951950073242
        CmanEsperado = 44.317378997802734
                                              
        # Testa o nome das chaves
        self.assertTrue("cos" in saida)
        self.assertTrue("pro" in saida)
        self.assertTrue("euc" in saida)
        self.assertTrue("man" in saida)
                       
        # Compara somente n casas decimais
        casas_decimais = 3        
        self.assertAlmostEqual(saida['cos'], CcosEsperado, places=casas_decimais)
        self.assertAlmostEqual(saida['pro'], CproEsperado, places=casas_decimais)
        self.assertAlmostEqual(saida['euc'], CeucEsperado, places=casas_decimais)
        self.assertAlmostEqual(saida['man'], CmanEsperado, places=casas_decimais) 

    # Testes getMedidasTextoPalavraRelevante_2
    def test_getMedidasTexto_PalavraRelevante_2(self):
        logger.info("Rodando .getMedidasTexto(texto, palavra_relevante=2)")
        
        # Valores de entrada
        texto = ["Fresh sea bass is a great delicacy.","I play bass in a jazz band."]

        # Valores de saída
        saida = self.modelo.getMedidasTexto(texto, palavra_relevante=2)
        
        # Valores esperados
        CcosEsperado = 0.0                
        CeucEsperado = 0.0
        CmanEsperado = 0.0
                       
        # Testa o nome das chaves
        self.assertTrue("cos" in saida)
        self.assertTrue("euc" in saida)
        self.assertTrue("man" in saida)
                       
        # Compara somente n casas decimais
        casas_decimais = 3
        self.assertAlmostEqual(saida['cos'], CcosEsperado, places=casas_decimais)
        self.assertAlmostEqual(saida['euc'], CeucEsperado, places=casas_decimais)
        self.assertAlmostEqual(saida['man'], CmanEsperado, places=casas_decimais) 
        
    # Testes getEmbeddingTexto e similaridadeCosseno
    def test_getEmbeddingTexto_similaridadeCosseno(self):
        logger.info("Rodando .getEmbeddingTexto(texto) e similaridadeCosseno(embedding1, embedding2))")
        
        # Valores de entrada        
        texto1 = "Fresh sea bass is a great delicacy." 
        texto2 = "I fished for a bass in the river yesterday." 
        texto3 = "I play bass in a jazz band."

        # Valores de saída
        # Recupera os embeddings dos textos
        embeddingTexto1 = self.modelo.getEmbeddingTexto(texto1)
        embeddingTexto2 = self.modelo.getEmbeddingTexto(texto2)
        embeddingTexto3 = self.modelo.getEmbeddingTexto(texto3)

        # Avalia a similaridade entre os embeddings dos textos
        sim12 = similaridadeCosseno(embeddingTexto1, embeddingTexto2)
        sim13 = similaridadeCosseno(embeddingTexto1, embeddingTexto3)
        sim23 = similaridadeCosseno(embeddingTexto2, embeddingTexto3)
        
        # Valores esperados
        sim12Esperado = 0.5752597451210022
        sim13Esperado = 0.5554090142250061
        sim23Esperado = 0.6850479245185852
        
        #Compara somente n casas decimais
        casas_decimais = 3
        self.assertAlmostEqual(sim12, sim12Esperado, places=casas_decimais)
        self.assertAlmostEqual(sim13, sim13Esperado, places=casas_decimais)
        self.assertAlmostEqual(sim23, sim23Esperado, places=casas_decimais) 
               
    # Testes getCodificacaoToken e similaridadeCosseno
    def test_getCodificacaoToken_similaridadeCosseno(self):
        logger.info("Rodando .getCodificacaoToken(texto) e similaridadeCosseno(embedding1, embedding2))")
        
        # Valores de entrada
        texto = "After stealing money from the bank vault, the bank robber was seen fishing on the Amazonas river bank."

        # Valores de saída
        saida = self.modelo.getCodificacaoToken(texto)
        
        # Recupera os indices do token "bank" no texto (7,13,18)
        idx_tokens = getIndexTokenTexto(saida['tokens_texto_mcl'], "▁bank")
                
        # Recupera os embeddings da saída do método de acordo com os índices
        embedToken1 = saida['token_embeddings'][idx_tokens[0]]
        embedToken2 = saida['token_embeddings'][idx_tokens[1]]
        embedToken3 = saida['token_embeddings'][idx_tokens[2]]
        
        # Mensura a similaridade do cosseno
        sim12 = similaridadeCosseno(embedToken1,embedToken2)
        sim13 = similaridadeCosseno(embedToken1,embedToken3)
        sim23 = similaridadeCosseno(embedToken2,embedToken3)
                        
        # Valores esperados
        sim12Esperado = 0.6884649395942688
        sim13Esperado = 0.4111558794975281
        sim23Esperado = 0.38392549753189087
        
        # Compara somente n casas decimais
        casas_decimais = 3
        self.assertAlmostEqual(sim12, sim12Esperado, places=casas_decimais)
        self.assertAlmostEqual(sim13, sim13Esperado, places=casas_decimais)
        self.assertAlmostEqual(sim23, sim23Esperado, places=casas_decimais) 

    # Testes getEmbeddingTexto e produtoEscalar
    def test_getEmbeddingTexto_produtoEscalar(self):
        logger.info("Rodando .getEmbeddingTexto(texto) e produtoEscalar(embedding1, embedding2))")
        
        # Valores de entrada        
        texto1 = "Fresh sea bass is a great delicacy." 
        texto2 = "I fished for a bass in the river yesterday." 
        texto3 = "I play bass in a jazz band."

        # Valores de saída
        # Recupera os embeddings dos textos
        embeddingTexto1 = self.modelo.getEmbeddingTexto(texto1)
        embeddingTexto2 = self.modelo.getEmbeddingTexto(texto2)
        embeddingTexto3 = self.modelo.getEmbeddingTexto(texto3)

        # Avalia a similaridade entre os embeddings dos textos
        pro12 = produtoEscalar(embeddingTexto1, embeddingTexto2)
        pro13 = produtoEscalar(embeddingTexto1, embeddingTexto3)
        pro23 = produtoEscalar(embeddingTexto2, embeddingTexto3)
        
        # Valores esperados
        pro12Esperado = 2.00468111038208
        pro13Esperado = 2.0749378204345703
        pro23Esperado = 2.6158621311187744
        
        #Compara somente n casas decimais
        casas_decimais = 3
        self.assertAlmostEqual(pro12, pro12Esperado, places=casas_decimais)
        self.assertAlmostEqual(pro13, pro13Esperado, places=casas_decimais)
        self.assertAlmostEqual(pro23, pro23Esperado, places=casas_decimais) 
       
    # Testes getCodificacaoToken e produto escalar
    def test_getCodificacaoToken_produtoEscalar(self):
        logger.info("Rodando .getCodificacaoToken(texto) e produtoEscalar(embedding1, embedding2))")
        
        # Valores de entrada
        texto = "After stealing money from the bank vault, the bank robber was seen fishing on the Amazonas river bank."

        # Valores de saída
        saida = self.modelo.getCodificacaoToken(texto)
        
        # Recupera os indices do token "▁bank" no texto (7,13,18)
        idx_tokens = getIndexTokenTexto(saida['tokens_texto_mcl'], "▁bank")
                
        # Recupera os embeddings da saída do método de acordo com os índices
        embedToken1 = saida['token_embeddings'][idx_tokens[0]]
        embedToken2 = saida['token_embeddings'][idx_tokens[1]]
        embedToken3 = saida['token_embeddings'][idx_tokens[2]]
        
        # Mensura a similaridade do cosseno
        pro12 = produtoEscalar(embedToken1,embedToken2)
        pro13 = produtoEscalar(embedToken1,embedToken3)
        pro23 = produtoEscalar(embedToken2,embedToken3)
                        
        # Valores esperados
        pro12Esperado = 8.25847053527832
        pro13Esperado = 5.2866010665893555
        pro23Esperado = 5.398103713989258
        
        # Compara somente n casas decimais
        casas_decimais = 3
        self.assertAlmostEqual(pro12, pro12Esperado, places=casas_decimais)
        self.assertAlmostEqual(pro13, pro13Esperado, places=casas_decimais)
        self.assertAlmostEqual(pro23, pro23Esperado, places=casas_decimais) 
        
    # Testes getCodificacaoToken e distanciaEuclidiana
    def test_getCodificacaoToken_distanciaEuclidiana(self):
        logger.info("Rodando .getCodificacaoToken(texto) e distanciaEuclidiana(embedding1, embedding2))")
        
        # Valores de entrada
        texto = "After stealing money from the bank vault, the bank robber was seen fishing on the Amazonas river bank."

        # Valores de saída
        saida = self.modelo.getCodificacaoToken(texto)
        
        # Recupera os indices do token "bank" no texto (7,13,18)
        idx_tokens = getIndexTokenTexto(saida['tokens_texto_mcl'], "▁bank")
                
        # Recupera os embeddings da saída do método de acordo com os índices
        embedToken1 = saida['token_embeddings'][idx_tokens[0]]
        embedToken2 = saida['token_embeddings'][idx_tokens[1]]
        embedToken3 = saida['token_embeddings'][idx_tokens[2]]
        
        # Mensura a distância Euclidiana
        dif12 = distanciaEuclidiana(embedToken1,embedToken2)
        dif13 = distanciaEuclidiana(embedToken1,embedToken3)
        dif23 = distanciaEuclidiana(embedToken2,embedToken3)
                        
        # Valores esperados
        dif12Esperado = 2.751354932785034
        dif13Esperado = 3.932889461517334
        dif23Esperado = 4.170392036437988
        
        # Compara somente n casas decimais
        casas_decimais = 3
        self.assertAlmostEqual(dif12, dif12Esperado, places=casas_decimais)
        self.assertAlmostEqual(dif13, dif13Esperado, places=casas_decimais)
        self.assertAlmostEqual(dif23, dif23Esperado, places=casas_decimais) 
       
    # Testes getCodificacaoToken e distanciaManhattan
    def test_getCodificacaoToken_distanciaManhattan(self):
        logger.info("Rodando .getCodificacaoToken(texto) e distanciaManhattan(embedding1, embedding2))")
        
        # Valores de entrada
        texto = "After stealing money from the bank vault, the bank robber was seen fishing on the Amazonas river bank."

        # Valores de saída
        saida = self.modelo.getCodificacaoToken(texto)
        
        # Recupera os indices do token "bank" no texto (7,13,18)
        idx_tokens = getIndexTokenTexto(saida['tokens_texto_mcl'], "▁bank")
                
        # Recupera os embeddings da saída do método de acordo com os índices
        embedToken1 = saida['token_embeddings'][idx_tokens[0]]
        embedToken2 = saida['token_embeddings'][idx_tokens[1]]
        embedToken3 = saida['token_embeddings'][idx_tokens[2]]
        
        # Mensura a distância Euclidiana
        dif12 = distanciaManhattan(embedToken1,embedToken2)
        dif13 = distanciaManhattan(embedToken1,embedToken3)
        dif23 = distanciaManhattan(embedToken2,embedToken3)
                        
        # Valores esperados
        dif12Esperado = 46.316822
        dif13Esperado = 67.33476
        dif23Esperado = 72.573906
        
        # Compara somente n casas decimais
        casas_decimais = 3
        self.assertAlmostEqual(dif12, dif12Esperado, places=casas_decimais)
        self.assertAlmostEqual(dif13, dif13Esperado, places=casas_decimais)
        self.assertAlmostEqual(dif23, dif23Esperado, places=casas_decimais) 
                       
if "__main__" == __name__:
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    logger.info("Teste TextoTransformer_t5_en")
    unittest.main()
    