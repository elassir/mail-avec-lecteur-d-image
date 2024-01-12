import cv2
import mediapipe as mp
from email.message import EmailMessage
import smtplib
import time 

last_email_time = 0
email_delay = 30  # Délai en secondes
# Initialisation de MediaPipe Hands
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

# Fonction pour envoyer un email
# zone a remplir
def send_email(subject, body):
    email_sender = ''
    email_password =''
    email_receiver = ''

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
        print("Email envoyé avec succès !")

# Capture vidéo
cap = cv2.VideoCapture(0)

last_sent = None

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    lmList = []
    if results.multi_hand_landmarks:
        for handlandmark in results.multi_hand_landmarks:
            for id, lm in enumerate(handlandmark.landmark):
                h, w, _ = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
            mpDraw.draw_landmarks(img, handlandmark, mpHands.HAND_CONNECTIONS)
    current_time = time.time()
    if lmList:
        # Détecter la position du pouce
        thumb_tip = lmList[4][2]
        thumb_base = lmList[2][2]

        if current_time - last_email_time > email_delay:
            if thumb_tip < thumb_base and last_sent != "happy":
                send_email("mail automatique", "J'ai fait un pouce vers le haut c'est oui")
                last_sent = "happy"
                last_email_time = current_time
        elif thumb_tip > thumb_base and last_sent != "sad":
                send_email("mail automatique", "J'ai fait un pouce vers le bas c'est non")
                last_sent = "sad"
                last_email_time = current_time

    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
