import cv2
from flask import Flask,request
app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello_world():
    image_original = request.files['file']
    image_binary = cv2.threshold(image_original,100,255,cv2.THRESH_BINARY)
    cv2.imwrite('test.png', image_binary)
    return 'Hello, Docker!'