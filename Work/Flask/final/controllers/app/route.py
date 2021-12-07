#controllers/app/routes


from flask import redirect, request, render_template
from run import app

@app.route('/')
def index():
    return render_template('app/index.html')


