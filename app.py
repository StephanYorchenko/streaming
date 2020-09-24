from flask import Flask, render_template, request, send_file, Response

import os
import random
import threading
import pyautogui
from camera import Camera

app = Flask(__name__)

mutex = threading.Lock()

def get_screen_():
    with mutex:
        pyautogui.screenshot('static/screenshot.png')

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template('hello.html')

@app.route('/get', methods=['GET', 'POST'])
def refresh_image():
    get_screen()
    return send_file('static/screenshot.png', as_attachment=True)

@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/get_screen')
def get_screen():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run('0.0.0.0', 8002)
