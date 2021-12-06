
from flask import Flask, render_template,  request, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os

app=Flask(__name__)

UPLOAD_FOLDER = 'static/assest'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newsdb.db'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)


class Xeberler(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(100))
    content=db.Column(db.String(1000))
    img=db.Column(db.String(100))



@app.route('/')
def index():
    news=Xeberler.query.all()
    return render_template('index.html', news=news)




@app.route("/adding/", methods=["GET","POST"])
def adding():
    news = Xeberler.query.all()
    if request.method=='POST':
        file = request.files['img']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        basliq=request.form["title"]
        metn=request.form["content"]
        newss= Xeberler(    #data beseye gonderen budu
            title = basliq,
            content = metn,
            img = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        )
        db.session.add(newss)
        db.session.commit()
        return redirect("/")
    return render_template("inputs.html", news=news)    # niye inputsu, index deyil?





@app.route('/contentnews/<int:id>')
def contentnews(id):
    news = Xeberler.query.filter_by(id=id).first()
    if news == id:
         return render_template("contentnews.html",news=news)
    return render_template("contentnews.html",news=news)




@app.route("/delete/<int:id>")
def delete(id):
    news=Xeberler.query.filter_by(id=id).first()
    db.session.delete(news)
    db.session.commit()
    return redirect("/adding")



if __name__=='__main__':
    app.run(debug=True)    