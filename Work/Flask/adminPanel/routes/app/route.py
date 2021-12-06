from app import app
from flask import request, render_template, redirect


@app.route('/')
def index():
    return render_template('app/index.html')