from flask import render_template
from app import app
from models.books import books
from models.books import *

@app.route('/library')
def index():
    return render_template('index.html', title='Home', books=books)