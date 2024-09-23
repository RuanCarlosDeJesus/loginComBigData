from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
import pandas as pd
import dask.dataframe as dd

app = Flask(__name__)


app.config["MONGO_URI"] = "mongodb://localhost:27017/users_db" 
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    new_user = {
        'name': name,
        'email': email,
        'password': password
    }
    mongo.db.users.insert_one(new_user)  

    
    process_data()
    
    return redirect(url_for('index'))

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    user = mongo.db.users.find_one({'email': email, 'password': password})  
    if user:
        return f"Welcome, {user['name']}!"
    return "Invalid credentials!"

@app.route('/count_users', methods=['GET'])
def count_users():
    user_count = mongo.db.users.count_documents({})  
    return f"Total de usuários cadastrados: {user_count}"

def process_data():
    print("Iniciando o processamento de Big Data...")

    
    data = {
        'name': ['Alice', 'Bob', 'Charlie'] * 1000,
        'value': [1, 2, 3] * 1000
        'name': [' Marcos', 'Janna', 'Carol'] * 1000,
        'value': [1, 2, 3] * 1000
    }
    
   
    df = pd.DataFrame(data)
    print("DataFrame criado com sucesso.")
    
    
    df.to_csv('data.csv', index=False)
    print("Arquivo CSV gerado.")

   
    dask_df = dd.read_csv('data.csv')
    print("Arquivo CSV lido com Dask.")

    result = dask_df.groupby('name').sum().compute()  
    print("Processamento com Dask completo. Resultado:")
    print(result) 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

