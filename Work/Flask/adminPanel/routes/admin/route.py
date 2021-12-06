from app import app
from flask import redirect, request, render_template
from models import *

@app.route('/admin/')
def admin():
    return render_template('admin/index.html')



@app.route('/admin/users',methods=['GET','POST'])
def admin_user():
    if request.form=='POST':
        name=request.form['ad']
        surname=request.form['soyad']
        userr=User(name, surname)
        return render_template('admin/user.html',  userr=userr)
    return render_template('admin/user.html', userr=None)