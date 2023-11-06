import cv2

# Abrindo a imagem
path = r'Questões/1/image.jpg'
image = cv2.imread(path)

# Plotando a imagem
cv2.imshow('Image', image)
cv2.waitKey(0)

# Salvando a imagem
cv2.imwrite('Questões/1/Imagem_salva.jpg', image)

print('FIM')

