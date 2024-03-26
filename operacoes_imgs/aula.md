# Relacionamentos e Operações entre Imagens
Como as imagens são nada mais nada menos do que matrizes, podemos realizar operações com elas para obter novas imagens.
1. Soma -> Podemos deixar mais clara uma imagem (somamos uma matriz de mesmo tamanho)
2. Subtração -> Podemos deixar mais escura (subtraimos uma matriz de mesmo tamanho)
3. Sobreposição -> Sobrepor imagens uma na outra, juntar as duas (imagem 1, peso, imagem 2, peso e gamma (valor para somar ao resultado em cada pixel, ou seja, quanto maior mais claro))
4. Operações Lógicas
    * Not -> Negado
    * And -> True quando os dois são true
    * Or -> True quando pelo menos um deles é true
    * Xor -> Quando os dois são true, temos false. Só é true quando só um deles é true