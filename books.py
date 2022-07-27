from pymysql import connect


class Book(object):
    def __init__(self):  #create object
        self.conn = connect(
            host=localhost,
            port='3306',
            user='root',
            password='root',
            database='books',
            charset='utf8'
        )
        self.cursor=self.conn.cursor()

    def __del__(self):  #release object
        self.cursor.close()
        self.conn.close()

    def get_books_infos_limit(self):
        sql='select * from book_infos limit 1'
        return self.cursor.execute(sql)

