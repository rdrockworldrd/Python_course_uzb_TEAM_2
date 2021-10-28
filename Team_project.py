import matplotlib.pyplot as plt
import pandas as pd
from tkinter import *
import numpy as np
data = pd.read_csv("Annual freshwater ms dos.csv")

def chiz():

    c1=variable1.get()
    c2=variable2.get()
    c3=variable3.get()
    c4=variable4.get()
    gr1=data[data.country==c1]
    gr2=data[data.country==c2]
    gr3=data[data.country==c3]
    gr4 = data[data.country == c4]
    plt.plot(gr1.year, gr1.freshwater/10**8)
    plt.plot(gr2.year, gr2.freshwater/10**8)
    plt.plot(gr3.year, gr3.freshwater/10**8)
    plt.plot(gr4.year, gr4.freshwater/10**8)
    plt.legend([c1,c2,c3,c4])
    plt.xlabel("year")
    plt.xlabel("freshwater")
    plt.show()


master = Tk()
master.geometry("300x200")

variable1 = StringVar(master)
variable1.set("Osiyo") # default value
w1 = OptionMenu(master, variable1, "Uzbekistan", "China", "India", "Indonesia", "Pakistan", "Bangladesh", "Japan",
"Philippines", "Vietnam", "Turkey", "Iran", "Thailand", "Myanmar", "South Korea", "Iraq", "Afghanistan", "Saudi Arabia",
"Malaysia", "Yemen", "Nepal", "North Korea", "Sri Lanka", "Kazakhstan", "Syria", "Cambodia", "Jordan", "Azerbaijan",
"United Arab Emirates", "Tajikistan", "Israel", "Laos", "Lebanon", "Kyrgyzstan", "Turkmenistan", "Singapore", "Oman",
"Palestine", "Kuwait", "Georgia", "Mongolia", "Armenia", "Qatar", "Bahrain", "Cyprus","Bhutan", "Brunei", "Fiji",
"Timor", "Papua New Guinea", "New Zealand", "Maldives", "Australia")
w1.config(bg="#e845f7")
w1.pack()

variable2 = StringVar(master)
variable2.set("Yevropa") # default value
w2 = OptionMenu(master, variable2, "Russia", "Germany", "United Kingdom", "France", "Italy", "Spain", "Ukraine", "Poland",
"Romania", "Netherlands", "Belgium", "Czechia", "Greece", "Portugal", "Sweden", "Hungary", "Belarus",
"Austria", "Serbia", "Switzerland", "Bulgaria", "Denmark", "Finland", "Slovakia", "Norway", "Ireland", "Croatia",
"Moldova", "Bosnia and Herzegovina", "Albania", "Lithuania", "North Macedonia", "Slovenia", "Latvia",
"Estonia", "Montenegro", "Luxembourg", "Malta", "Iceland", "Monaco")
w2.config(bg="#45f7ee")
w2.pack()

variable3 = StringVar(master)
variable3.set("Afrika") # default value
w3 = OptionMenu(master, variable3, "Nigeria", "Ethiopia", "Egypt", "Congo", "Tanzania", "South Africa", "Kenya", "Uganda",
"Algeria", "Sudan", "Morocco", "Angola", "Mozambique", "Ghana", "Madagascar", "Cameroon", "Niger",
"Burkina Faso", "Mali", "Malawi", "Zambia", "Senegal", "Chad", "Somalia", "Zimbabwe", "Guinea", "Rwanda", "Benin", "Burundi",
"Tunisia", "South Sudan", "Togo", "Sierra Leone", "Libya", "Liberia", "Central African Republic",
"Mauritania", "Eritrea", "Namibia", "Gambia", "Botswana", "Gabon", "Lesotho", "Guinea-Bissau", "Equatorial Guinea",
"Mauritius", "Eswatini", "Djibouti", "Comoros", "Cape Verde", "Sao Tome and Principe", "Seychelles", "Guinea",
"Democratic Republic of Congo", "Cote d'Ivoire","Africa Eastern and Southern", "Africa Western and Central")
w3.config(bg="#f7eb79")
w3.pack()

variable4 = StringVar(master)
variable4.set("Shimoliy va Janubiy Amerika") # default value
w4 = OptionMenu(master, variable4, "United States", "Brazil", "Mexico", "Colombia", "Argentina", "Canada", "Peru",
"Venezuela", "Chile", "Guatemala", "Ecuador", "Bolivia", "Haiti", "Cuba", "Dominican Republic", "Honduras", "Paraguay",
"Nicaragua", "El Salvador", "Costa Rica", "Panama", "Uruguay", "Jamaica", "Trinidad and Tobago", "Guyana", "Suriname",
"Belize", "Barbados", "Saint Lucia", "Grenada", "Saint Vincent and the Grenadines", "Antigua and Barbuda",
"Dominica", "Saint Kitts and Nevis", "Puerto Rico")
w4.config(bg = "#2172db")
w4.pack()

btn=Button(master,text="Grafikni chizish", command=chiz, bg="#32a83a", fg="#fff")
btn.pack()
master.mainloop()

