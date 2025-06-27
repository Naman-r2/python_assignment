
from flask import Flask, render_template, jsonify
import random
from batchmates import names

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/random')
def get_random_name():
    return jsonify({'name': random.choice(names)})
