# -*- coding:utf-8 –*-
import cv2
# 调用模型库文件
face_cascade = cv2.CascadeClassifier('C:01_face/venv/lib/python3.6/site-packages/cv2/data/haarcascade_frontalface_default.xml')# 这个路径需要按需修改
# 摄像头参数设置
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
faceNum = 0

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=3)

    faceNum = len(faces)
    print("人脸数量: %s" % faceNum)

    if len(faces) > 0:
        for faceRect in faces:
            x, y, w, h = faceRect
            # -------- 在人脸周围绘制矩形
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)

    cv2.imshow('img', frame)

    # -------- Q键推出
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
# 释放资源
cv2.destroyAllWindows()
cap.release()