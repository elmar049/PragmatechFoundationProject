# student={'name':'Elmar', 'surname':'mammadov', 'age':'28', 'position':'student'}

# print(student['age']) 

# for x in "banana":
#   print(x) 
#   if x==banan



users=[
{   'name':'Elmar',
    'surname':'Mammadov',
    'id':'1'
},
{
    'name':'Fazil',
    'surname':'Quliev',
    'id':'2'
},
{
    'name':'Neymar',
    'surname':'Ronaldinyo',
    'id':'3'
},

]


def finduser():
    uzeritap=input("axtardigniz userin adin dsxil edin:")
    for user in users:
        if uzeritap==user['name']:
            print(user['name'])


finduser()