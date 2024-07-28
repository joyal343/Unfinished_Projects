# Importing necessary modules from Flask
from flask import Flask, render_template, request
from peewee import SqliteDatabase
import datetime
# Creating the Flask application instance
app = Flask(__name__)

# Creating the Database Object
db = SqliteDatabase('product.db')

# Define a route for the home page
@app.route('/')
def home():
    # Render the HTML template named 'index.html'
    
    return render_template('index.html')

@app.route('/product/add', methods=['POST'])
def post_data():
    title=request.form['title'] 
    price=request.form['price']
    date=request.form['dateInp'].split('-')
    dateTimeObjDate = datetime.datetime( int(date[0]) , int(date[1]) , int(date[2]),0,0,0)
    return render_template('index.html')
    
# Run the application
if __name__ == '__main__':
    app.run(debug=True)
