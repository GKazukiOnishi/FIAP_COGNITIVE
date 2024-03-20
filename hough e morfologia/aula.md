# Transformada de Hough e morfologia

## Transformada de Hough
* Método para reconhecimento de padrões simples como retas e círculos  
* Permite detectar mesmo em imagens com pouca visibilidade ou muito ruído  

```
cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp = 160, minDist = 100, param1 = 200, param2 = 100, minRadius = 50, maxRadius = 150)
```

* imagem
* method
* dp -> quanto maior, mais fácil de encontrar círculos na imagem
* minDist -> Distância mínima entre centros dos círculos
* param1 -> Valor do gradiente
* param2 -> Limiar do Acumulador, quanto mais baixo mais círculos (inclusive falsos positivos)
* minRadius -> Raio mínimo (pixels)
* maxRadius -> Raio máximo (pixels)

`cv.HoughLinesP(image, rho, theta, threshold, lines, minLineLength, maxLineGap)`

* rho - distância
* theta - ângulo
* threshold - Limiar do acumulador - Permissividade para encontrar os formatos
* minLineLength - Comprimento mínimo da linha
* maxLineGap - Distância máxima entre pontos considerados na mesma linha

## Morfologia matemática
* Forma de alterar os pixeis de uma imagem a partir dela mesma
* Podemos por exemplo dilatar uma imagem
* Remover buracos, remover pontos soltos
* Erodir uma imagem