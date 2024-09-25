from flask import Flask, request, render_template, redirect, url_for
import pytesseract
import os
from utils.usingOCR import OCR
from utils.support import allowed_file

app = Flask(__name__)

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\NhanPham\AppData\Local\Programs\Tesseract-OCR'

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def main_page():
    return render_template('home.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return render_template('home.html', warning='No file part !')
    file = request.files['image']
    if file.filename == '':
        return render_template('home.html', warning='No selected file !')
    if file and allowed_file(file.filename):
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return render_template('home.html', warning='File uploaded successfully !')
    return render_template('home.html', warning='File type not allowed !')

if __name__ == "__main__":
    if not os.path.exists("uploads"):
        os.makedirs("uploads")
    app.run(debug=True)