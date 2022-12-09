from flask import render_template, request, redirect
from app import app
from models.books import books
from models.books import *

@app.route('/library')
def index():
    return render_template('index.html', title='Home', books=books)

@app.route('/library/<index>')
def single_book(index):
    selected_book = books[int(index)]
    return render_template('book.html', book=selected_book)

@app.route('/library', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    new_book = Book(title, author, genre)
    add_new_book(new_book)
    return redirect('/library')
