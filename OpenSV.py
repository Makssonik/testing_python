# https://www.youtube.com/watch?v=1Yi3irfC8BA
# Импорт OpenSV и назначение имени cv
import cv2 as cv

# вывод версии OpenSV
print(cv.__version__)

# Захват изображения с веб камеры, по умолчанию веб камера с id 0
capture = cv.VideoCapture(0)

# Подгружаем каскад с лицами
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

# Цикл выводит изображение с WEB-камеры пока не нажмешь ESC
while True:
    # Получаем изображение
    ret, img = capture.read()

    # Основной поиск лица. img - где искать.
    # scaleFactor - размер.
    # minNeighbors - сколько соседей может быть, точнее поиск будет.
    # minSize - минимальный размер поискового квадрата
    faces = face_cascade.detectMultiScale(img, scaleFactor=1.5, minNeighbors=5, minSize=(20, 20))

    # Рисуем квадрат на изображении
    for (x, y, w, h) in faces:
        # img - где рисуем
        # (x, y) - начало квадрата
        # (x+w, y+h) - конец квадрата
        # (0, 0, 255) - цвет
        # 2 - толщина
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv.imshow('From camera', img)  # Показывает изображение с заголовком
    k = cv.waitKey(30) & 0xFF  # Ждет нажатия кнопки ESC 30 мил.сек., и все это в integer
    if k == 27:
        break

# Прекращает использовать веб камеру
capture.release()

# Закрывает все окна
cv.destroyAllWindows()
