# coding=utf-8
import cv2
import time

cap = cv2.VideoCapture(0)

while(True):
    # 每次从视频数据流框架中抓取一帧图片
    ret, frame = cap.read()

    # 将图片显示在特定窗口上
    cv2.imshow('OpenCV Capture',frame)

    # 当按下 q 键时退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # 当按下 s 键时保存图像
    key = cv2.waitKey(1)
    if key == ord('s'):
        filename = time.strftime('%Y%m%d-%H%M%S') + ".jpg"
        cv2.imwrite(filename, frame)