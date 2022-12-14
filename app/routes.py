#file will define endpoints

from flask import Blueprint, jsonify

class Book:
    def __init__(self, id=None, title=None, description=None):
        self.id = id
        self.title = title
        self.description = description

books = [
    Book(1, "Harry Potter", "A fantasy novel set in an imaginary world."),
    Book(2, "The Little Prince", "A fantasy novel set in an imaginary world."),
    Book(3, "Fictional Book Title", "A fantasy novel set in an imaginary world.")
] 

books_bp = Blueprint("books", __name__, url_prefix="/books")

@books_bp.route("", methods=["GET"])
def handle_books():
    books_response = []
    for book in books:
        books_response.append({
            "id": book.id,
            "title": book.title,
            "description": book.description
        })
    return jsonify(books_response), 200

@books_bp.route("/<book_id>", methods=["GET"])
def handle_book(book_id):
    try:
        book_id = int(book_id)
    except ValueError:
        return {"message": f"book id {book_id} invalid"}, 400
    for book in books:
        if book.id == book_id:
            return {
                "id": book.id,
                "title": book.title,
                "description": book.description
            }, 200
        return {"message": f"book {book_id} not found"}, 404
