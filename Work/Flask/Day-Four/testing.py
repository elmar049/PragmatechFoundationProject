from flask import Flask,request, render_template

app=Flask(__name__)#zdes vnutri mojno dobavit render_template='X' i toqda temlates papka budet X)

####### kaK perevesti infu iz python koda variable ctob svetilsa v HTML.. 

# @app.route('/')
# def index():
#     users=[
#     1,2,3,4,5,6,7,8,9

#     ]
#     return render_template('index.html', melumat=users)



########## Post method cherez x=request.form[]


@app.route('/ading')
def ading():
    news=[
        {   'TitleNews':'Əməkdar artist əməliyyat olundu',
            'ContentNews':'Bildiririk ki, Novruz Əliyev (Qartal) noyabrın 23-də Azərbaycan Respublikası Səhiyyə Nazirliyi Milli Onkologiya Mərkəzində əməliyyat olunub. Təbii ki, pandemiya ilə əlaqədar olaraq xəstə ziyarətinə qızından başqa heç kəs, hətta digər ailə üzvləri belə buraxılmayıb. Dünən isə xəstəxanadan çıxarılıb, qızı İlahə xanımın evindədir və ev şəraitində müalicəsi davam edir”.'
        },

        {   'TitleNews': 'Samuxda gənc qadın dəm qazından zəhərlənib',
            'ContentNews': '2000-ci il təvəllüdlü R.Novruzova zəhərlənmə diaqnozu ilə xəstəxanaya çatırılıb. Qadına tibbi yardım göstərilib, vəziyyətinin kafi olduğu bildirilir. İlkin məlumata görə 21 yaşlı qadın yaşadığı evdə dəm qazından zəhərlənib.'
        },    
        {
            'TitleNews': 'DSX-nin yaralı zabiti: “Helikopter 150-200 metr hündürlükdə uçurdu”',
            'ContentNews': ' Hava şəraiti də normal idi. Helikopter normal hündürlükdə – təxminən 150-200 metr hündürlükdə uçurdu. Ancaq qəzanın baş verdiyi eniş zamanı hündürlüyü dəqiq deyə bilmərəm.'
        }
        ]


    return render_template('new.html', x=news )



@app.route('/added', methods=['POST', 'GET'])

def added():
    if request.method=='POST':
        x=request.form['title']
        y=request.form['content']


    return f''






#### a=request.args.get() method:

# @app.route('/ading')
# def ading():
#     return 









if __name__=='__main__': 
    app.run(debug=True)   