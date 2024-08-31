"""
This module handles file uploads and color configuration for the Flask application.
"""

import os
import random
import socket
from flask import Flask, render_template, request, redirect, send_from_directory

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = os.getenv('UPLOAD_FOLDER', '/rahees-uploaded-files')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB limit

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

color_codes = {
    "red": "#e74c3c",
    "green": "#16a085",
    "blue": "#2980b9",
    "blue2": "#30336b",
    "pink": "#be2edd",
    "darkblue": "#130f40"
}

color = os.environ.get('APP_COLOR') or random.choice(
    ["red", "green", "blue", "blue2", "darkblue", "pink"]
)

@app.route("/")
def main():
    """
    Render the main page with a color configuration.
    """
    return render_template('hello.html', name=socket.gethostname(), color=color_codes[color])

@app.route('/color/<color_name>')
def new_color(color_name):
    """
    Change the color configuration and render the main page.
    """
    return render_template('hello.html', name=socket.gethostname(), color=color_codes[color_name])

@app.route('/read_file')
def read_file():
    """
    Read contents of a file and render the main page with the file contents.
    """
    with open("testfile.txt", "r", encoding="utf-8") as f:
        contents = f.read()
    return render_template('hello.html', name=socket.gethostname(), contents=contents, color=color_codes[color])

@app.route('/upload-title')
def index():
    """
    Render the upload form page.
    """
    return render_template('fill-form.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Handle file upload and save the file to the configured upload folder.
    """
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return render_template('sucessful-upload.html', uploaded_filename=file.filename)
    return redirect(request.url)

@app.route('/files/<filename>')
def uploaded_file(filename):
    """
    Serve a file from the upload folder.
    """
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)

