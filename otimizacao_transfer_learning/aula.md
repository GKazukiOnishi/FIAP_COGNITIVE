# Técnicas de Otimização

## Validation
Uma parte do conjunto de dados é removido e usado para verificar a performance do modelo durante o treinamento, aí ele vai ajustando ao longo do treinamento os hiperparâmetros, também evitando **overfitting** com a base de dados de treinamento.  
  
**Overfitting**: Quando o modelo se ajusta demais apenas aos dados de treinamento e não funciona com a precisão desejada

## Dropout
Aleatoriamente ignoramos uma parte parte dos neurônios (Ex: 20%) em cada camada, afim de evitar **Overfitting**.

## Batch Normalization
Tenta ajustar as ativações e torna elas mais inteligentes usando normalização, média 0 etc.  
No final ela cria uma camada de BN após as camadas de convolução ou densas da rede.  

## Data Augmentation
Aumentamos o dataset de imagens ao gerar várias variações de cada um delas, facilitando a identificação de características semelhantes de uma imagem.  

## Callbacks
O código passa a verificar quando o treinamento de epochs para de valer a pena, porque deixa de mudar os valores.  

# Arquiteturas de Redes CNN
Arquiteturas já prontas para treinamento com as camadas preparadas, podendo ser usadas e treinadas com nossas datasets, mas já tendo passado por testes anteriores e já tendo passado por diversos treinamentos com milhares de imagens, permitindo uma classificação muito boa já.  
Tem N arquiteturas já prontas

## MobileNET etc. etc.
## Inception
IF/ELSE nas camadas, em que mais de uma camada pode ser ativada a partir de um única original.

# Transfer Learning
Nos aproveitamos de arquiteturas de redes neurais existentes e treiná-las para classificar novas categorias ou objetos personalizados.  
Nós pegamos as nossas entradas, jogamos na arquitetura pronta, e depois podemos inclusive trocar as saídas, permitindo usar uma para classificar (neurônio que diz se é gato ou cachorro) e outro para regressão talvez (linear ou logística), permitindo predizer a idade do animal.  
  
Com essa ideia não precisamos criar modelos do zero, podemos aproveitar modelos genéricos já prontos.  
  
## Como funciona
1. Escolhemos uma rede pré-treinada
2. Removemos a camada de classificação (include_top = False)
3. Adicionamos camadas personalizadas no modelo (mais camadas de saídas, por exemplo)
4. Congelamos os pesos (para não treinar tudo de novo que o modelo pré-treinado já treinou)
5. Pré-processamento dos dados para preparar para a rede pré-treinada
6. Treine o modelo
7. Avalie e otimize