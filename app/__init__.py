from flask import Flask
from app.init_db import db_connect
import psycopg2

app = Flask(__name__)


#Data base connection
def get_db_connection():
    conn = psycopg2.connect(
            host="localhost",
            database="python_project",
            user="postgres",
            password="admin")
    conn = get_db_connect()
    return conn


get_db_connection()

@app.route('/books', methods=['GET'])
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM books;')
    books = cur.fetchall()
    cur.close()
    conn.close()
    return books


@app.route ('/', methods=['POST'])
def hello_world():
       return "<p>Hello, World!</p>"

