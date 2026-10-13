import cv2
from pyzbar.pyzbar import decode
import json
from datetime import datetime

attendance = {}

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    for barcode in decode(frame):
        qr_data = barcode.data.decode("utf-8")
        points = barcode.polygon

        if qr_data not in attendance:
            attendance[qr_data] = {
                "date": datetime.now().strftime("%Y-%m-%d"),
                "time": datetime.now().strftime("%H:%M:%S")
            }

        pts = np.array([(p.x, p.y) for p in points], np.int32)
        cv2.polylines(frame, [pts], True, (0, 255, 0), 2)
        cv2.putText(frame, qr_data, (points[0].x, points[0].y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.imshow("QR Attendance", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()