from os import add_dll_directory
from flask import Flask, request

app=Flask(__name__)



@app.route('/')
def index():
    return f"""
        <form action="about" method='POST'>
        <input type="text" placeholder="Insert log" name='ad'>
        <input type="password" placeholder="Insert password" name='pass'>
        <input type="submit">
    </form>
    """

@app.route('/about', methods=['GET','POST'])
def about():
    if request.method=='POST':
        name=request.form['ad']
        passs=request.form['pass']
    if name =="elmar" and passs=="12345":
        return '<h1 style="color: red;">Bu Sehifeye xosh gelmisiniz</h1>'
    else:
        return '<h1 style="color: red;">Bu Sehifeye xosh gelmemisiniz</h1>'




if __name__=='__main__':

    app.run(debug=True)        