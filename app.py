from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'ashu'
app.config['MYSQL_PASSWORD'] = '12345'
app.config['MYSQL_DB'] = 'mydb'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    user_query = request.form['user']
    product_query = request.form['product']

    try:
        cur = mysql.connection.cursor()

        # Search for users based on the input queries
        cur.execute("SELECT * FROM users WHERE name LIKE %s OR product LIKE %s",
                    (f"%{user_query}%", f"%{product_query}%"))
        cur.execute("INSERT INTO users (name, product) VALUES (%s, %s)", ('John Doe', 'Product A'))
        cur.execute("INSERT INTO users (name, product) VALUES (%s, %s)", ('Jane Smith', 'Product B'))
        cur.execute("INSERT INTO users (name, product) VALUES (%s, %s)", ('Alice Johnson', 'Product A'))
        cur.execute("INSERT INTO users (name, product) VALUES (%s, %s)", ('Bob Anderson', 'Product C'))


        results = cur.fetchall()
        cur.close()

        return render_template('search.html', results=results)

    except Exception as e:
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)


# Insert Sample Data (Optional)

