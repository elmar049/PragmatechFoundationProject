from flask import Flask, render_template

app=Flask(__name__)

title="salamlar olsun"
text="kimlere?"
@app.route('/')
def index():   #zdes etot index otnositsa v tempalte indexu?
    return render_template('index.html', x=title, y=text )         #"Bu <h1>index</h1> sehifesidr"   #dekorator


if __name__=='__main__':
    app.run(debug=True)