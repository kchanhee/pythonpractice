import Tkinter as tk
import tkFileDialog as filedialog
import xml.etree.ElementTree as ET

def convertToCOD(filename):
    infile = open(filename)
    blank_count = 0
    while blank_count < 2:
        line = infile.readline()
        if len(line) == 0:
            blank_count += 1
            continue
        card_count = line[0]
        card_name = line[2:]
        print "card count: %s, card name: %s" % (card_count, card_name) 
    


root = tk.Tk()
root.withdraw()
files = filedialog.askopenfilenames(parent = root, title='Choose a file')
print root.tk.splitlist(files)

for f in files:
    convertToCOD(f)

