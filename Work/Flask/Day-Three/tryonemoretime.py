from flask import Flask, request

app=Flask(__name__)

@app.route('/')
def index():
    return f"""<form action="/about" method='POST'>
        <input type="text" placeholder="Insert log" name='name'>
        <input type="text" placeholder="Insert password" name='pass'>
        <input type="submit">
    </form>
    """


@app.route('/about', methods=['GET','POST'])
def about ():
    if request.method=="POST":
        ad=request.form['name']
        parol=request.form['pass']
    if ad=='elmar' and parol=='12345':
        return '<h1 style="color: red;"> Gel cixda ala </h1>'
    else:
        return '<h1 style="color: red;"> One more attempts</h1>'     




if __name__=='__main__':
    app.run(debug=True)