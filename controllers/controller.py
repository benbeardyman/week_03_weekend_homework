from flask import render_template, request, redirect
from app import app
from models.books import *

@app.route('/books')
def index():
    return render_template('index.html', title='Home', books=books)

@app.route('/books/<index>')
def single_book(index):
    selected_book = books[int(index)]
    return render_template('book.html', book=selected_book)

@app.route('/books', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    checked_out = request.form.get('checked_out')
    new_book = Book(title, author, genre, checked_out)
    add_new_book(new_book)
    return redirect('/books')

@app.route('/books/delete/<index>', methods=['POST'])
def delete(index):
    delete_book_at_index(int(index))
    return redirect('/books')
