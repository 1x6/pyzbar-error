import os
import pyzbar
from pyzbar.pyzbar import decode
from PIL import Image
from flask import request, jsonify, Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    img = Image.open('barcode.png')
    decoded_list = decode(img)
    print(len(decoded_list))
    print(decoded_list)
    return str(decoded_list)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000)) 