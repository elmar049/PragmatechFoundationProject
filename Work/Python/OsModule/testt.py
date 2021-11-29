import os

# folderOne='C:/Users/elmar/Desktop/project/photos'
# folderTwo='C:/Users/elmar/Desktop/project/HTML'
# folderThree='C:/Users/elmar/Desktop/project/JavaScript'
# folderFour='C:/Users/elmar/Desktop/project/CSS'

# os.mkdir(folderOne)
# os.mkdir(folderTwo)
# os.mkdir(folderThree)
# os.mkdir(folderFour)


src="C:/Users/elmar/Desktop/project/1"
dest="C:/Users/elmar/Desktop/project/photos/1"

try:
    if os.path.exists(dest):
        print("There is already a file there")
    else:
        os.replace(src,dest)
        print(src+" was moved")
except FileNotFoundError:
    print(src+" was not found")