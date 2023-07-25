import torch
import cv2
import numpy as np

model = torch.hub.load("ultralytics/yolov5", model="custom", path="best.pt", force_reload = True) # custom model

cv2.namedWindow("ASL")
vc = cv2.VideoCapture(0)

while vc.isOpened():
    ret, frame = vc.read()
    if not ret:
        print("no frame")
        break

    results = model(frame)
    cv2.imshow("ASL", results.render()[0])

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

vc.release()
cv2.destroyAllWindows()
