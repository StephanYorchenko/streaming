from flask import Flask, render_template, request, Markup, send_file
import os
import random

import pyautogui

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template('hello.html')

@app.route('/get', methods=['GET', 'POST'])
def refresh_image():
    pyautogui.screenshot('static/screenshot.png')
    return send_file('static/screenshot.png', as_attachment=True)

@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == '__main__':
    app.run('0.0.0.0', 8002)
