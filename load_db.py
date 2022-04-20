from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

author1 = Author("Jane", "Austen")
author_repository.save(author1)
#test = author_repository.select_all()
#print(test[0].__dict__)

#print(author_repository.select(1))

#author_repository.delete_all()

#author_repository.delete(5)

# author2 = Author("Stephen", "King")
# author_repository.save(author2)
#author2.last_name = "Bachman"

#author_repository.update(author2)

# book1 = Book("Jane Eyre", author1)
# book_repository.save(book1)

# book2 = Book("The Shinning", author2)
# book_repository.save(book2)

#print(book_repository.select_all())

#print(book_repository.select(1))
#book_repository.delete_all()
#book_repository.delete(2)
#book1.title = "Jane Eyre 2"
#book_repository.update(book1)
