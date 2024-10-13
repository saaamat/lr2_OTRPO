import cv2

# Загружаем классификатор для распознавания лиц
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Загружаем изображение
image_path = 'src/faces.jpg'  # Измените на имя вашего файла с фото
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Находим лица
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Печатаем количество найденных лиц
print(f'Найдено {len(faces)} лиц(а).')

# Для отладки можно нарисовать рамки вокруг найденных лиц
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)


