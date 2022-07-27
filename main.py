from flask import Flask
from books import Book
app = Flask(__name__)

@app.route("/")
def hello_world():
    book = Book()
    data = book.get_books_infos_limit()
    return data

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=1943,debug=True)


