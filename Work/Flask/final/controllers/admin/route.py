#controllers/admin/routes


from os import name
from flask import redirect, request, render_template
from run import app

@app.route('/admin/')
def admin_index():
    return render_template('admin/index.html')


@app.route('/admin/users',methods=['GET','POST'])
def users():
    from run import db 
    from modules.module import User
    users=User.query.all()
    if request.method=='POST':
        _ad=request.form['ad']
        _soyad=request.form['soyad']
        user=User(name=_ad, surname=_soyad )
        db.session.add(user) 
        db.session.commit() 
        return redirect ('/admin/users')  # bu iwi gor, sonra ele saxla hemebn  seyfede
    return render_template ('admin/users.html', users=users)    


@app.route('/admin/delete/<int:id>')
def admin_delete(id):
    from run import db 
    from modules.module import User
    user=User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/admin/users')




@app.route('/admin/update/<int:id>',methods=['GET','POST'])
def admin_update(id):
    from modules.module import User
    from run import db
    user=User.query.get(id)
    if request.method=='POST':
        _ad=request.form['ad']
        _soyad=request.form['soyad']
        user.name=_ad
        user.surname=_soyad
        db.session.commit()
        return redirect('/admin/users')
    
    
    return render_template('admin/updateuser.html',user=user)