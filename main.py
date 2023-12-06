from tkinter import *
from tkinter import scrolledtext
import xml.etree.ElementTree as ET
from PIL import ImageTk, Image

pencere = Tk()
pencere.title("XML PROJECT")
pencere.geometry("1800x800")

navigasyon = 0
tree = ET.parse('veriseti.xml')
root = tree.getroot()
max_index = len(root) - 1

def ileriGit():
    global navigasyon
    navigasyon += 1
    if navigasyon > max_index:
        navigasyon = 0
    goster(navigasyon)

def geriGit():
    global navigasyon
    navigasyon -= 1
    if navigasyon < 0:
        navigasyon = max_index
    goster(navigasyon)

def goster(navigasyon):
    resim = root[navigasyon][7].text
    bilgiler = [
        root[navigasyon][0].text,
        root[navigasyon][1].text,
        root[navigasyon][2].text,
        root[navigasyon][3].text,
        root[navigasyon][4].text,
        root[navigasyon][5].text,
        root[navigasyon][6].text,
        root[navigasyon][7].text
    ]

    gorsel = ImageTk.PhotoImage(Image.open(resim))
    cerceve = Label(image=gorsel, bg="white")
    cerceve.image = gorsel
    cerceve.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky=N+S+E+W)

    scrolled_text = scrolledtext.ScrolledText(pencere, wrap=WORD, width=60, height=25)
    scrolled_text.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky=N+S+E+W)

    for index, bilgi in enumerate(bilgiler):
        text = f"{index + 1}. {bilgi}\n"
        if index % 2 == 0:
            scrolled_text.insert(END, text, 'odd')
            scrolled_text.tag_configure('odd', foreground='blue')
        else:
            scrolled_text.insert(END, text, 'even')
            scrolled_text.tag_configure('even', foreground='green')

    scrolled_text.configure(state='disabled')

def listele():
    liste = ""
    for index, item in enumerate(root, start=1):
        liste += f"Kayıt {index}:\n"
        for i, info in enumerate(item, start=1):
            liste += f"{i}. Bilgi: {info.text}\n"
        liste += "\n"

    liste_pencere = Toplevel(pencere)
    liste_pencere.title("Tüm İçerik")

    scrolled_text = scrolledtext.ScrolledText(liste_pencere, wrap=WORD, width=200, height=50)
    scrolled_text.grid(row=0, column=0, padx=10, pady=10, sticky=N+S+E+W)

    for line in liste.splitlines():
        if line.startswith("Kayıt "):
            numara = line.split()[1].rsplit(":", 1)[0]
            tag = "odd" if int(numara) % 2 != 0 else "even"
            scrolled_text.insert(END, line + "\n", tag)
        else:
            scrolled_text.insert(END, line + "\n")

        scrolled_text.tag_configure("odd", background="lightblue")
        scrolled_text.tag_configure("even", background="lightgreen")

    scrolled_text.configure(state="disabled")


ileriButon = Button(pencere, text="İleri", command=ileriGit, width=10, height=2)
geriButon = Button(pencere, text="Geri", command=geriGit, width=10, height=2)
listeleButon = Button(pencere, text="Tüm İçeriği Listele", command=listele, width=15, height=2)

geriButon.grid(row=0, column=0, sticky="nsew", padx=5, pady=10)
ileriButon.grid(row=0, column=1, sticky="nsew", padx=5, pady=10)
listeleButon.grid(row=0, column=2, sticky="nsew", padx=5, pady=10)

pencere.columnconfigure(0, weight=1)
pencere.columnconfigure(1, weight=1)
pencere.columnconfigure(2, weight=1)

goster(navigasyon)

pencere.mainloop()

