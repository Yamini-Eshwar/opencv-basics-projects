import cv2

body_classifier = cv2.CascadeClassifier(r"C:\Users\vamsi\Downloads\haarcascade_fullbody.xml")

cap = cv2.VideoCapture(r"C:\Users\vamsi\Downloads\Ped_small.mp4")

while cap.isOpened():
    success, frame = cap.read()

    if not success:
        print("❌ Couldn't read frame. Video might be over or not found.")
        break

    frame = cv2.resize(frame, (640, 480))  # Optional: speed boost
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    bodies = body_classifier.detectMultiScale(gray, 1.2, 2)

    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)

    cv2.imshow('pedestrians', frame)

    if cv2.waitKey(25) & 0xFF == ord('a'):
        break

cap.release()
cv2.destroyAllWindows()
