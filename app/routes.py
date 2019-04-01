from flask import Flask
from flask import render_template, flash, redirect, url_for, session, request, Response
from flask import jsonify
from app import app
import cv2
import io
import time
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
  GPIO.setmode (GPIO.BOARD)       # programming the GPIO by BOARD pin numbers, GPIO21 is called as PIN40
  GPIO.setup(40,GPIO.OUT)             # initialize digital pin40 as an output.
  GPIO.output(40,1)                      # turn the LED on (making the voltage level HIGH)
  time.sleep(1)                         # sleep for a second
  GPIO.cleanup()                         # turn the LED off (making all the output pins LOW)
  time.sleep(1)                        #sleep for a second    

  GPIO.setmode (GPIO.BOARD)       # programming the GPIO by BOARD pin numbers, GPIO21 is called as PIN40
  GPIO.setup(40,GPIO.OUT)             # initialize digital pin40 as an output.
  GPIO.output(40,1)                      # turn the LED on (making the voltage level HIGH)
  time.sleep(1)                         # sleep for a second
  GPIO.cleanup()                         # turn the LED off (making all the output pins LOW)
  time.sleep(1)                        #sleep for a second 

  GPIO.setmode (GPIO.BOARD)       # programming the GPIO by BOARD pin numbers, GPIO21 is called as PIN40
  GPIO.setup(40,GPIO.OUT)             # initialize digital pin40 as an output.
  GPIO.output(40,1)                      # turn the LED on (making the voltage level HIGH)
  time.sleep(1)                         # sleep for a second
  GPIO.cleanup()                         # turn the LED off (making all the output pins LOW)
  time.sleep(1)                        #sleep for a second 
  return jsonify(
      success=True,
  )

if __name__ == '__main__': 
	app.run(host='0.0.0.0', debug=True, threaded=True)