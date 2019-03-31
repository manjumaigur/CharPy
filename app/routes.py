from flask import Flask
from flask import render_template, flash, redirect, url_for, session, request, Response
from flask import jsonify
from app import app
import cv2
import io
from PIL import Image
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

import RPi.GPIO as GPIO

client = vision.ImageAnnotatorClient()

vc = cv2.VideoCapture(0)

@app.route('/')
@app.route('/index')
def index(): 
   """Video streaming .""" 
   return render_template('index.html')

def gen(): 
   """Video streaming generator function.""" 
   while True: 
       rval, frame = vc.read() 
       cv2.imwrite('pic.jpg', frame)
       yield (b'--frame\r\n' 
              b'Content-Type: image/jpeg\r\n\r\n' + open('pic.jpg', 'rb').read() + b'\r\n') 

@app.route('/text_feed', methods=['GET', 'POST'])
def detect_text():
    """Detects text in the file."""
    with io.open('pic.jpg', 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    string = ''

    for text in texts:
        string+=' ' + text.description
        break
    return jsonify(
        success=True,
        text_detected=string,
    )

@app.route('/video_feed') 
def video_feed(): 
   """Video streaming route. Put this in the src attribute of an img tag."""
   return Response(gen(), 
                   mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/send_signal', methods=['GET', 'POST'])
def send_signal():
  try:
    GPIO_PIN = 23
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_PIN, GPIO.OUT)
    GPIO.output(GPIO_PIN, GPIO.HIGH)
    # time.sleep(1)
    # GPIO.output(GPIO_PIN, GPIO.HIGH)
    # time.sleep(1)
    # GPIO.output(GPIO_PIN, GPIO.HIGH)
    # time.sleep(1)
    # GPIO.output(GPIO_PIN, GPIO.LOW)
  except:
    print ("Error inside function send_signal")
    pass
  GPIO.cleanup()
  return jsonify(
      success=True,
  )

if __name__ == '__main__': 
	app.run(host='0.0.0.0', debug=True, threaded=True)