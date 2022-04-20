from flask import Flask
from controllers.books_controller import books_bp
app = Flask(__name__)

app.register_blueprint(books_bp)