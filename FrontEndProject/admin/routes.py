#ADMIN-ROUTES:

from flask import Flask, request,render_template, redirect,url_for
from werkzeug.utils import import_string, secure_filename
import os
from run import app
from models import *
from flask_mail import Message
from flask_login import LoginManager, UserMixin, login_manager, login_user, login_required, logout_user, current_user
from run import login_manager


# Login
@login_manager.user_loader
def load_user(user_id):
    from models import Login
    return Login.query.get(int(user_id))

@app.route("/login",methods=["GET","POST"])
def admin_login():
    from models import Login
    from run import db
    login = Login(
        admin_username = "elmar",
        admin_password = "elmar",
        log_bool = False
    )
    db.session.add(login)
    db.session.commit()
    
    if request.method == "POST":
        if login.admin_username == request.form["admin_username"] and login.admin_password == request.form["admin_password"]:
            login_user(login, remember=login.log_bool)
            return redirect (url_for("index"))

        else:
            return redirect(url_for("admin_login"))

    return render_template("admin/login.html", login = login)

# Logout
@app.route("/logout")
@login_required
def admin_logout():
    logout_user()
    return redirect (url_for("index"))






@app.route("/aboutUs")
def aboutus_html():
    return render_template("app/aboutus.html")


@app.route("/contact")
def contact_html():
    return render_template("app/contact.html")



@app.route("/admin", methods=['POST','GET'])
@login_required
def index():
    from models import Services
    from run import db
    srvs=Services.query.all()
    if request.method=='POST':
        name=request.form['srvname']
        content=request.form['srvcontent']
        file = request.files['srvimg']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        serviceobject=Services(
        service_img=os.path.join(app.config['UPLOAD_FOLDER'], filename),
        service_title=name,
        service_content=content
        )
        db.session.add(serviceobject)
        db.session.commit()
        return redirect("/admin")
    return render_template("admin/blog.html", srvs=srvs)


@app.route("/admin/delete/<int:id>")
def delete(id):
    from models import Services
    from run import db
    srvs=Services.query.filter_by(id=id).first()
    db.session.delete(srvs)
    db.session.commit()
    return redirect("/admin")




@app.route('/admin/update/<int:id>',methods=['GET','POST'])
@login_required
def admin_update(id):   
    from models import Services
    from run import db

    srvs = Services.query.filter_by(id=id).first()
    if request.method=='POST':
        srvs = Services.query.filter_by(id=id).first()
        srvs.service_title=request.form['srvname']
        srvs.service_content=request.form['srvcontent']
        db.session.commit()
        return redirect('/admin')
    
    return render_template('admin/update_blog.html',srvs=srvs)











@app.route("/admin/products", methods=['POST','GET'])
@login_required
def products():
    from models import Products
    from run import db
    prds=Products.query.all()
    if request.method=='POST':
        name=request.form['product_name']
        file = request.files['product_img']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        productobject=Products(
        product_img=os.path.join(app.config['UPLOAD_FOLDER'], filename),
        product_name=name,
        )
        db.session.add(productobject)
        db.session.commit()
        return redirect("/admin/products")
    return render_template("admin/product.html", prds=prds)




@app.route("/products/delete/<int:id>")
def delete_product(id):
    from models import Products
    from run import db
    prds=Products.query.filter_by(id=id).first()
    db.session.delete(prds)
    db.session.commit()
    return redirect("/admin/products")



@app.route('/products/update/<int:id>',methods=['GET','POST'])
@login_required
def product_update(id):   
    from models import Products
    from run import db

    prds = Products.query.filter_by(id=id).first()
    if request.method=='POST':
        prds = Products.query.filter_by(id=id).first()
        prds.product_name=request.form['product_name']
        
        db.session.commit()
        return redirect('/admin/products')
    
    return render_template('admin/update_product.html',prds=prds)









@app.route('/admin/emails', methods=["GET","POST"])
@login_required
def admin_emails():
    from models import Emails
    from run import db
    import smtplib    
    from flask_mail import Mail,Message
    from run import mail

    mails=Emails.query.all()
    if request.method=='POST':
        mailname=request.form['name']
        mailsurname=request.form['surname']
        mailnumber=request.form['number']
        mailemail=request.form['mail']
        mailtext=request.form['text']
        mails=Emails(
            mailname=mailname,
            mailsurname = mailsurname,
            mailemail = mailemail,
            mailnumber= mailnumber,
            mailtext= mailtext,
        )
        myGmail = "dlyamusic999@gmail.com"
        msg = Message(mailtext,sender = mailemail, recipients = [myGmail])
        mail.send(msg)
        db.session.add(mails)
        db.session.commit()
        return redirect ("/")
    return render_template("admin/emails.html", mails=mails)




@app.route("/emails/delete/<int:id>")
def delete_email(id):
    from models import Emails
    from run import db
    mls=Emails.query.filter_by(id=id).first()
    db.session.delete(mls)
    db.session.commit()
    return redirect("/admin/emails")

        





