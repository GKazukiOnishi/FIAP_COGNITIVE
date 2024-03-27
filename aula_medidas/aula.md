# Aula de Medidas
Olhar código no Google Colab  
1. Reutilizamos o que aprendemos sobre contornos
2. Obtemos os pontos "caixa" de cada contorno
3. Ordenamos os pontos do contorno para descobrir qual ponto é qual (top left, top right, bottom left, bottom right)
4. Obtemos os pontos do meio de cada reta da caixa do contorno
5. Encontramos o centro
6. Definimos os pixels por medida, ou usamos um valor de referência
7. Calculamos a distância euclidiana entre cada ponto médio
8. Fazemos regra de três para obter a medida a partir da distância em pixels dos pontos médios
9. Escrevemos as medidas na imagem