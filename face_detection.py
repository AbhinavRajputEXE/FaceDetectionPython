import cv2

def detect_face(image_path):
    face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    detected_faces = face_detector.detectMultiScale(gray_image, 1.3, 5)

    for (x, y, w, h) in detected_faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('Detected Faces', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#Example
detect_face('data/images/face2.jpg')
detect_face('data/images/face.jpg')