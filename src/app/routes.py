from flask import render_template
from app import app

@app.route('/')
def game():
    return render_template('index.html')