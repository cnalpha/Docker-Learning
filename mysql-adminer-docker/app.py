from flask import Flask, render_template
import pymysql

app = Flask(__name__)

# 資料庫連接配置
db = pymysql.connect(
    host='mysql',
    user='user',
    password='userpassword',
    database='student_db',
    cursorclass=pymysql.cursors.DictCursor
)

@app.route('/')
def index():
    with db.cursor() as cursor:
        cursor.execute("CREATE TABLE IF NOT EXISTS students (id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(255), last_name VARCHAR(255), age INT, class VARCHAR(50))")
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
    return render_template('index.html', students=students)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
