from flask import Flask, request

app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])  #route zdes otvecaet za to cto vzyat return iz def index-a i zakinut v URL(browser)
def index():
    if request.method=='POST':
        name=request.form['ad']
        return f'<h1>senin gozel adin var ay {name}</h1>'
    return "salam"    
      
    # name=request.args.get("ad")    #eto metod ctob mojno bilo poluchit daniie is URL... zdes variable kotoriuy  idet v return, a soyad eto bduet v URL
    # surname=request.args.get("soyad")    #ad i soyad zdes parametri url-a
    # return f'<h1>soxum adiv {name} ve soyadiva {surname}</h1>'
  

@app.route('/about') 
def about():
    return f""""
        <form action="/" method='POST'>
        <input type="text" placeholder="namee" name='ad'>
        
        <input type="submit">
    </form>
    
    """   

if __name__=='__main__':    
    app.run(debug=True)  #otvecaet za klick, kotoriy mejdu userom i serverom