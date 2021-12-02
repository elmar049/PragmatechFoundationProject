from flask import Flask, request, render_template
from werkzeug.wrappers import request


app=Flask(__name__)




@app.route('/')
def index():
    return f"""
        <form action="/news" methods="POST">
        <input type="text" placeholder="Type News Title" name='title'>
        <input type="text" placeholder="Type News Content" name='content'>
        <input type="submit" value="Gonder">
    </form>
    """




@app.route('/news', methods=['GET', 'POST'])
def news():
    if request.method=='POST':
        bawdix=request.form['title']
        metin=request.form['content']
        return f'{bawdix} {metin} cox bomba xeberdir'










if (__name__)=='__main__':
    app.run(debug=True)
