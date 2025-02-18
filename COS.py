import tkinter as tk
from tkinter import Tk, Label, Button, Entry, StringVar, LEFT, RAISED, RIGHT, PhotoImage, END, BOTTOM

Hausa =  {"God": "Allah",
             "Jesus": "Yesu",
             "Holy Spirit": "Ruhu Mai Tsarki",
             "Man": "Namiji",
             "Woman": "Mace", 
             "Father": "Uba",
             "Mother": "Uwa",
             "Baby": "Jariri(male)",
             "Ram": "Rago",
             "Cry": "Kuka",
             "Sleep": "Barciu",
             "Bed": "Gado",
             "Lion": "Zaki",
             "Food": "Abinci",
             "Soup": "Miya",
             "Road": "Hanya",
             "Sand": "Miya",
             "Rice": "Shinkafa",
             "Song": "Waka", 
             "Car": "Mota",
             "See": "Gani",
             "Love": "Kauna",
             "Arrange": "Shiya",
             "Thank": "Godiya",
             "Hate": "Kyama",
             "Joy": "Farin",
             "Peace": "Zaman Lafia",
             "War": "Yaki",
             "Queen":"Sarauniya",
             "King": "Sarki",
             "Pray": "Addu'a", 
             "baby": "Jaririya(female)"}

Yoruba = {"God": "Olorun",
            "Jesus": "Jesu",
            "Holy Spirit": "Emi Mimo",
            "Man": "Okunrin",
            "Woman": "Obinrin",
            "Father": "Iya",
            "Baby": "Omo owo",
            "Ram": "Agbo",
            "Water": "Omi",
            "Cry": "Kigbe",
            "Sleep": "Sun", 
            "Bed": "Ibusun",
            "Lion": "Kinium",
            "Food": "Ounje",
            "Soup": "Bimo",
            "Rice": "Iresi",
            "Love": "Ife",
            "Arrange": "Seto",
            "Thank": "Ose",
            "Hate": "Ikorira",
            "Joy": "Ayo",
            "Peace": "Alafi",
            "War": "Ogun",
            "Queen": "Ayaba",
            "King": "Oba",
            "Pray": "Gbadura"}

Arabic = {"God": "Iilh",
            "Jesus": "Eisaa",
            "Holy Spirit": "Alruwh alquds",
            "Man": "Rajul",
            "Woman": "Aimra'a",
            "Father": "Ab",
            "Mother": "Al'umu",
            "Baby": "Tifl",
            "Ram": "Kabish",
            "Water": "Ma",
            "Cry": "Yabki",
            "Sleep": "Yanam",
            "Bed": "Sarir",
            "Lion": "Al'asad",
            "Food": "Taeam",
            "Soup": "Hisa'an",
            "Rice": "Arz",
            "Song": "Ughnia",
            "Car": "Sayaara",
            "See": "Yaraa",
            "Love":"Habul",
            "Arrange": "Yaratab",
            "ThANK": "Shakar",
            "Joy": "Marah",
            "Peace": "Salam",
            "War": "Haru",
            "Queen": "Malaka",
            "King": "MLIK",
            "Pray": "Yusaliy"}

Idoma = {"God": "Owoicho",
         "Jesus": "Jisos",
         "Holy Spirit": "Owu nifu",
         "Man": "Ochenyilo",
         "Woman:": "Ochenya",
         "Father": "Ada",
         "Mother": "Ene",
         "Baby": "Oyinonya",
         "Ram": "Adangba",
         "Water": "Enkpo",
         "Cry": "Ikwu",
         "Sleep": "Olaa",
         "Bed": "Agodo",
         "Lion": "Agaba",
         "Food": "Odule",
         "Soup": "Oho",
         "Rice": "Osikapa",
         "Song": "Ijeh",
         "Car": "Moto",
         "See": "Mor",
         "Love": "Ihotu",
         "Arrange": "Loyalohi",
         "Thank": "Ainya",
         "Hate": "Anya",
         "Joy": "Eiyee",
         "Peace": "Ebor",
         "War": "Efu",
         "Pray": "yaduwa",
         "King": "Oche",
         "Queen": "Ochanya"}

Swahili = {"God": "Mungu",
           "Jesus": "Yesu",
           "Holy Spirit": "Roho Mtakatifu",
           "Man": "Mwanamume",
           "Woman": "Mwanamke",
           "Father": "Baba",
           "Mother": "Mama",
           "Baby": "Mtoto",
           "Ram": "Kondoo dume",
           "Water": "Maji",
           "Cry": "Lia",
           "Sleep": "Lala",
           "Bed": "Kitanda",
           "Lion": "Simba",
           "Food": "Chakula",
           "Soup": "Supu",
           "Rice": "Mchele",
           "Song": "wimbo",
           "Car": "Gari",
           "See": "Ona",
           "Love": "Upendo",
           "Arrange": "Panga",
           "Thank": "Shukuru",
           "Hate": "Chukia",
           "Joy": "Furah",
           "Peace": "Amani",
           "War": "vita",
           "Queen": "Malkia",
           "King": "Mfalne",
           "Pray": "Omba"}



window = Tk()
window.geometry("600x250")
window.title("Naija Dictionary")
window.config(background="Black")
Icon = PhotoImage(file='Screenshot_2024-08-13-19-52-25.png')
window.iconphoto(True,Icon)

Image_label = tk.Label(window, image=Icon)

welcome_label = tk.Label(window, text="welcome to our dictionary", padx=200,pady=50,bg="black",fg="white",font=("Algerian", 40))
welcome_label.pack()

title_label = tk.Label(window, text="Kindly select a language", padx=200,pady=50,bg="black",fg="white", font=("Algerian", 20, 'bold, '))
title_label.pack()



entry_text = Entry(window, font=("Arial", 50), fg="black",bg="white")
entry_text.pack(side=LEFT)

result = StringVar()
result_label = Label(window, textvariable=result, font=("Algerian", 50))
result_label.pack(side=BOTTOM)

def translate(word, dictionary):
    if word in dictionary:
        result.set(dictionary[word])
    else:
        result.set("Word not found")

Hausa_button = Button(window, text="Hausa", command=lambda: translate(entry_text.get(), Hausa),
                       font=("Comic Sans MS", 20, 'bold'), relief=RAISED)
Hausa_button.pack(side=LEFT)

yoruba_button = Button(window, text="Yoruba", command=lambda: translate(entry_text.get(), Yoruba),
                       font=("Comic Sans MS", 20, 'bold'), relief=RAISED)
yoruba_button.pack(side=LEFT)

arabic_button = Button(window, text="Arabic", command=lambda: translate(entry_text.get(), Arabic),
                       font=("Comic Sans MS", 20, 'bold'), relief=RAISED)
arabic_button.pack(side=LEFT)

idoma_button = Button(window, text="Idoma", command=lambda: translate(entry_text.get(), Idoma),
                       font=("Comic Sans MS", 20, 'bold'), relief=RAISED)
idoma_button.pack(side=RIGHT)

Swahili_button = Button(window, text="Swahili", command=lambda: translate(entry_text.get(), Swahili),
                       font=("Comic Sans MS", 20, 'bold'), relief=RAISED)
Swahili_button.pack(side=RIGHT)





window.mainloop()