
import os
import time
import cv2
import pyprind


class CharFrame:
    ascii_char = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

    # 像素映射到字符
    def pixelToChar(self, luminance):
        return self.ascii_char[int(luminance / 256 * len(self.ascii_char))]

    # 将普通帧转为 ASCII 字符帧
    def convert(self, img, limitSize):

        img = cv2.resize(img, limitSize, interpolation=cv2.INTER_AREA)

        ascii_frame = ''
        blank = ''
        for i in range(img.shape[0]):

            for j in range(img.shape[1]):
              ascii_frame += self.pixelToChar(img[i, j])
            ascii_frame += blank
        return ascii_frame


class V2Char(CharFrame):
    charVideo = []
    timeInterval = 0.033

    def __init__(self, path):
        self.genCharVideo(path)

    def genCharVideo(self, filepath):
        self.charVideo = []

        cap = cv2.VideoCapture(filepath)
        self.timeInterval = round(1 / cap.get(5), 3)#帧速率

        nf = int(cap.get(7))#得到文件的总帧数
        print('Generate char video, please wait...')
        for i in pyprind.prog_bar(range(nf)):
            # 转换颜色空间，第二个参数是转换类型，cv2.COLOR_BGR2GRAY表示从BGR&#8596;Gray
            rawFrame = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2GRAY)
 
            frame = self.convert(rawFrame, os.get_terminal_size())
            self.charVideo.append(frame)
        cap.release()

    def play(self):
        for frame in self.charVideo:
           print(frame)
           time.sleep(self.timeInterval)

if __name__ == '__main__':
    v2char = V2Char('vedio.mp4')
    v2char.play()
