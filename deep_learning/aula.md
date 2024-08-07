# Deep Learning
Qual a diferença com o Machine Learning?  
1. Quando é muito complexo
2. Quando tem muitos dados
3. Quando não tem um modelo ou exemplo a ser seguido
Nesses casos usamos o Deep Learning

## Rede Neural Artificial
É uma rede que recebe entradas, aplica pesos nelas e soma um certo valor.  
No exemplo das flores, seriam 4 entradas. E para usar ele não podemos ignorar entradas que nem no caso do Machine Learning.  
<br>
Para identificar entre um cão e gato, é um único neurônio com entradas e uma saída.  
Mas quando começa a ficar complexo e envolve várias decisões, precisamos de mais de um.  
  
### Função de ativação do Neurônio
Como saber quando usamos um ou outro?  
Temos várias funções para decidir, tem aquelas que é 0 ou 1, outras lineares, outras mais complexas.  
Tudo depende do caso, se queremos um valor ou outro, se vai ser uma faixa de valores etc.  

### Ou seja
1. Entrada
2. Peso
3. Bias (valor a ser somado)
4. Função de entrada

#### Entradas
* 1
* 2
* 3

#### Pesos
* 0.1
* 0.2
* 0.3

#### Bias
0

#### Função de ativação em Degrau
(u < 1 é 0, u >= 1 é 1)

#### Portanto
(1 * 0.1 + 2 * 0.2 + 3 * 0.3) + 0 = 1.4  
Como é maior que 1, temos o resultado 1

#### Concluindo
Para cada função e valores temos um resultado diferente.  
  
## Treinando uma rede para a porta AND
Se:
* 0 e 0 = 0
* 0 e 1 = 0
* 1 e 0 = 0
* 1 e 1 = 1
Para que os pesos consigam alcançar o valor 1 quando as entradas forem 1, e dar em 0 caso qualquer um não seja 1, podemos usar os pesos 0.5.  
* 0 + 0 = 0
* 0 + 0.5 = 0.5
* 0.5 + 0 = 0.5
* 0.5 + 0.5 = 1
Dessa forma temos uma rede neural capaz de simular a porta AND.  

### Ajuste de pesos
#### pesos(n + 1) = peso(n) + (taxaAprendizagem * entrada * erro)
Considerando uma taxa de aprendizagem = 0.1. Temos os seguintes cenários para o caso de teste 1 e 1 = 1. E começando com 0.  
* Entrada A: 0 + (0.1 * 1 * 1) = 0.1. Entrada B: 0 + (0.1 * 1 * 1) = 0.1
* Entrada A: 0.1 + (0.1 * 1 * 1) = 0.2 ...
* Entrada A: 0.5 + (0.1 * 1 * 0) = 0.5
Ou seja, 0.5 é um peso ideal para a rede neural.  
<br>
Perceba que ao treinar a mais do que o necessário, se a taxa de aprendizagem for muito alta, podemos acabar ultrapassando e não chegando a um bom neurônio.  




