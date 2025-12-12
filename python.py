import cv2
import matplotlib.pyplot as plt

# 1. Cargar imagen (cambia la ruta por la imagen que quieras usar)
img = cv2.imread("imagen.jpg")

# Verificamos si la imagen se cargó correctamente
if img is None:
    raise ValueError("No se pudo cargar la imagen. Verifica la ruta.")

# 2. Convertir a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 3. Aplicar suavizado para reducir ruido
blur = cv2.GaussianBlur(gray, (5, 5), 1)

# 4. Aplicar el detector de bordes Canny
edges = cv2.Canny(blur, threshold1=100, threshold2=200)

# 5. Mostrar resultados
plt.figure(figsize=(12,5))

plt.subplot(1,3,1)
plt.title("Imagen Original")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(1,3,2)
plt.title("Grises + Suavizado")
plt.imshow(blur, cmap="gray")
plt.axis("off")

plt.subplot(1,3,3)
plt.title("Bordes (Canny)")
plt.imshow(edges, cmap="gray")
plt.axis("off")

plt.show()
