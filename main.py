# Iride Main
#
# Copyright Emanuele Parini
#
# Iride Script
import match, date, number
import os
from flask import Flask, request

UPLOAD_FOLDER = '/upload'
ALLOWED_EXTENSIONS = {'jpg', 'png'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def start():
    return "<p>Welcome to Iride Engine 2.1</p>"


@app.route('/detect', methods=['GET', 'POST'])
def detect():
    if request.method == 'POST':
        if 'file1' not in request.files:
            return 'there is no file1 in form!'
        file1 = request.files['file1']
        path = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
        file1.save(path)
        ow_detect = match.IrideMatch('id_utente')
        return ow_detect

@app.route('/docinfo')
def docInfo():
    path = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
    ow_date = date.IrideDate('([0-9]{2}\-[0-9]{2}\-[0-9]{2})')
    ow_number = number.IrideNumber()
    return ow_date+'|'+ow_number

if __name__ == '__main__':
    app.run()

# Detect Document Owner
#ow_detect = match.IrideMatch('id_utente')
#print(ow_detect)

# Detect Document Date
#ow_date = date.IrideDate('([0-9]{2}\-[0-9]{2}\-[0-9]{2})')
#print(ow_date)

# Detect Document Number
#ow_number = number.IrideNumber()
#print(ow_number)
