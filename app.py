import numpy
import cv2
from flask import Flask, request, make_response
app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello_world():
    image_flask = request.files['file'].read()
    # convert string data to numpy array
    image_np = numpy.fromstring(image_flask, numpy.uint8)
    # convert numpy array to image
    image_cv2 = cv2.imdecode(image_np, cv2.IMREAD_UNCHANGED)
    # 先將圖片轉為灰階
    image_gray = cv2.cvtColor(image_cv2, cv2.COLOR_BGR2GRAY)
    # 將圖片做模糊化，可以降噪
    image_blur = cv2.medianBlur(image_gray, 5)
    # 一般圖二值化(有模糊降噪)
    ret, image_binary = cv2.threshold(image_blur, 100, 255, cv2.THRESH_BINARY)
    cv2.imwrite('test.png', image_binary)
    imageSub(image_binary, 'name.png', 0.1, 0.25, 0.18, 0.5)
    imageSub(image_binary, 'number.png', 0.8, 0.9, 0.35, 0.9)
    return 'Hello, Docker!'


@app.route('/show/<string:filename>', methods=['GET'])
def imageShow(filename):
    image_data = open(filename, "rb").read()
    response = make_response(image_data)
    response.headers['Content-Type'] = 'image/png'
    return response


def imageSub(image, name, hbr, her, wbr, wer):
    hight, width = image.shape
    imageSub = image[int(hight*hbr):int(hight*her), int(width *
                     wbr):int(width*wer)]  # 裁剪坐标为[y0:y1, x0:x1]
    cv2.imwrite(name, imageSub)
