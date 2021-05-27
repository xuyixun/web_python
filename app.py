import cv2
from flask import Flask,request
app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello_world():
    image_original = request.files['file']
     # 先將圖片轉為灰階
    img = cv2.cvtColor(image_original, cv2.COLOR_BGR2GRAY) 
    # 將圖片做模糊化，可以降噪
    image_blur = cv2.medianBlur(img,5) 
    # 一般圖二值化(有模糊降噪)
    image_binary = cv2.threshold(image_blur,100,255,cv2.THRESH_BINARY)
    cv2.imwrite('test.png', image_binary)
    return 'Hello, Docker!'