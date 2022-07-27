from flask import Flask, jsonify, Response
from books import Book
import json

app = Flask(__name__)


# app.config['JSON_AS_ASCII'] = False # This line not working to display chinese characters


@app.route("/")
def hello_world():
    book = Book()
    arrdata = book.get_books_infos_limit()
    print("arrData2 = ", arrdata)
    # return jsonify(arrData)
    j_string = json.dumps(arrdata, indent=4, default=str, ensure_ascii=False) # to display chinese characters properly
    response = Response(j_string,content_type='application/json; charset=utf-8') # to display the returns properly with above codes
    return response

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=1943,debug=True)


