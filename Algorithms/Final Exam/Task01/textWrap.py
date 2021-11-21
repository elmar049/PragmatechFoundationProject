import textwrap
def wrap(string, max_width):
    return "\n".join(textwrap.wrap(string, max_width))







    #Men elemek istediyim kimi, amma hackerranger yuxardakini qebul eleyir 



metn="Mennen yaxshi programci cixacey"
for i in range(0, len(metn), 4):
    print(metn[i:i+4])