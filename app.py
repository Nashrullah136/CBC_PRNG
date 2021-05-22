from flask import Flask
from flask import render_template, url_for, request
import cbc_prng 
import ast

app = Flask(__name__)

@app.route("/")
def root():
    url_for('static', filename='app.css')
    return render_template('index.html')

@app.route("/encrypt", methods=['POST'])
def encrypt():
    plain = request.form['plain']
    key = int(request.form['key'])
    block_size = int(request.form['blocksize'])
    ciphertext = repr(cbc_prng.encrypt(plain, key, "0"*block_size, block_size))
    return ciphertext[1:-1]

@app.route("/decrypt", methods=['POST'])
def decrypt():
    plain = ast.literal_eval("'"+request.form['cipher']+"'")
    key = int(request.form['key'])
    block_size = int(request.form['blocksize'])
    plaintext = cbc_prng.decrypt(plain, key, "0"*block_size, block_size)
    return plaintext