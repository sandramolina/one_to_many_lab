from flask import Flask, redirect, render_template, Blueprint, request
from models.book import Book
import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

books_bp = Blueprint('books',__name__)

@books_bp.route('/')
def home():
    books = book_repository.select_all()
    return render_template('index.html',all_books=books)

@books_bp.route('/<id>/delete', methods=['POST'])
def delete(id):
    book_repository.delete(id)
    return redirect('/')

@books_bp.route('/new')
def new_book():
    authors = author_repository.select_all()
    return render_template('new_book.html', all_authors = authors)

@books_bp.route('/addbook', methods = ['POST'])
def add_book():
    title = request.form['title']
    author_id = request.form['author_id']
    author_object = author_repository.select(author_id)
    book_object = Book(title, author_object)
    book_repository.save(book_object)
    return redirect('/')