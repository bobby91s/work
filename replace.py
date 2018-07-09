import os
import codecs

"""
Put this code in a .py file in the folder where your html-s are. This app will
crawl through all the files in it's current directory and will search for a '.html' file.
Insert in the variable called 'old' the string you want to replace and in the 'new' variable
the string you want it replaced with. After you run the program it will replace anything
from html tags to text in the html.
You will also get a small feedback after it's done.
"""

old = ''
new = ''


for filename in os.listdir(os.getcwd()):
    if '.html' in filename:
        with codecs.open(filename, "r", "utf-8") as f:
            newText=f.read().replace(old, new)

        with codecs.open(filename, "w", "utf-8") as f:
            f.write(newText)



print ('Done')
