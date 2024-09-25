from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import pytesseract
import os
from utils.usingOCR import OCR
from utils.support import allowed_file

app = Flask(__name__)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def main_page():
    return render_template('home.html')

@app.route('/upload', methods=['POST'])
def take_local_image():
    if 'image' not in request.files:
        return render_template('home.html', warning='No file part!')
    file = request.files['image']
    if file.filename == '':
        return render_template('home.html', warning='No selected file!')
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        model = OCR(file_path)
        os.remove(file_path)
        os.removedirs(UPLOAD_FOLDER)
        content = model.get_text(pytesseract)
        if not content:
            content = 'Unable to recognize text for this image!'
        return render_template('home.html', content=content)
    return render_template('home.html', warning='File type not allowed!')

if __name__ == "__main__":
    if not os.path.exists("uploads"):
        os.makedirs("uploads")
    app.run(debug=True)