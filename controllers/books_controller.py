from flask import Flask, redirect, render_template, Blueprint, request
from models.book import Book
import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

books_bp = Blueprint('books',__name__)

@books_bp.route('/')
def home():
    books = book_repository.select_all()
    return render_template('index.html',all_books=books, page_title="Home")

@books_bp.route('/<id>/delete', methods=['POST'])
def delete(id):
    book_repository.delete(id)
    return redirect('/')

@books_bp.route('/new')
def new_book():
    authors = author_repository.select_all()
    return render_template('new_book.html', all_authors = authors, page_title="Add New Book")

@books_bp.route('/addbook', methods = ['POST'])
def add_book():
    title = request.form['title']
    author_id = request.form['author_id']
    author_object = author_repository.select(author_id)
    book_object = Book(title, author_object)
    book_repository.save(book_object)
    return redirect('/')

@books_bp.route('/<id>', methods=['GET'])
def show_book(id):
    book = book_repository.select(id)
    return render_template('show.html', display_book = book, page_title=book.title)

@books_bp.route('/<id>', methods = ['POST'])
def edit_book_function(id):
    title = request.form['title']
    author_id = request.form['author_id']
    author_object = author_repository.select(author_id)
    book_to_update = Book(title, author_object, id)
    book_repository.update(book_to_update)
    return redirect('/')

@books_bp.route('/<id>/edit', methods=['GET'])
def edit_book(id):
    book  = book_repository.select(id)
    author_list = author_repository.select_all()
    return render_template('/edit.html', book = book, all_authors = author_list, page_title = "Edit")