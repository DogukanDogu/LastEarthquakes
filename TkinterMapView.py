import tkinter as tk
from tkintermapview import TkinterMapView
from bs4 import BeautifulSoup
import requests
import re

root = tk.Tk()

label = tk.Label(root, text='Son Depremler', font='Arial 18')
label.pack()

map_widget = TkinterMapView(root,width=900,height=500)
map_widget.pack()

map_widget.set_position(36, 36)

def getCoordsData():
    url = "http://www.koeri.boun.edu.tr/scripts/lst5.asp"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    pre_tag = soup.find("pre")
    text = pre_tag.text
    lines = text.split("\n")
    words = []
    for index in range(7, len(lines)):
        word = re.split(r'\s+', lines[index])
        words.append(word)
    coords = []
    for w in words:
        coords = tuple(w[2:4] for w in words)
    return coords


coords = getCoordsData()

for coord in coords:
    split_strings = []
    for string in coord[0:]:
        split_strings.append(string.split(','))
    if coord != []:
       list1 = [float(i) for i in coord]
       map_widget.set_marker(list1[0], list1[1])

map_widget.set_zoom(5)

tk.mainloop()





