# Aprendizado Supervisionado - Classificação
Supervisionado - Quando a máquina conhece as classes e atributos, e consegue estudar em cima disso.  
Não supervisionado - Quando a própria máquina vai separando e classificando e aprendendo.  
Por reforço - Vai tentando algo até dar certo.  

## KNN - Vizinhos mais próximos
Algoritmo que tenta localizar o número de K vizinhos mais próximos de uma medida, buscando classificar o grupo em que um determinado ponto se encontra mais próximo.  
  
O número de K costuma ser ímpar porque facilita encontrar os grupos mais próximos e a encontrar o ponto diferencial.  
Ele é definido analisando um gráfico e vendo qual valor de K tem maior acurácia.  
  
### Treino
Geralmente fazem um teste com uma parte do conjunto de dados, e o treino com o restante. De forma que o algoritmo não conheça o dado de teste enquanto estiver treinando, não causando impactos quando for aplicar o resultado do treino em um teste.  
Exemplo: Teste sendo 20% da massa e Treino sendo 80%.  
  
Tendo o resultado do teste, tentamos verificar a acurácia com base nas classes reais e as classes predizidas.  
  
