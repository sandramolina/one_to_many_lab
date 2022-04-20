from flask import Flask, redirect, render_template, Blueprint, request
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