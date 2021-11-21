# HakerRang ucun:
def mutate_string(string, position, character):
    string=string[:position]+ character+ string[position+1:]
    return string









x="abracadabra"
y=list(x)
y[5]='k'

print("".join(y))





# abracAdabra iydi, oldu abracKdabra 

