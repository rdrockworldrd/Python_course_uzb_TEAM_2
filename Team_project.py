import matplotlib.pyplot as plt # bu python dasturining kutubxonalaridan biri bo'lib grafik shakllarni tasvirlash uchun foydalaniladi

import pandas as pd # pandas - bu ma'lumotlarni tahlil qilish uchun Python dasturlash tili kutubxonasi,
# u raqamli jadvallar va vaqt seriyalarini ma'lumotlari tuzilmalari va operatsiyalaridan foydalanishda qo'llaniladi

from tkinter import * # Tkinter dasturi bu Python dastulash tilida kodlarni (GUI) foydalanuvchini grafik interfiys ko'rinishida foydalanishi uchun qo'llaniladi

data = pd.read_csv("Annual freshwater ms dos.csv") # dastur ishlashi uchun ma'lamulotlarni joylashgan manzili bazasi, joy-yo'li

def chiz(): # funksinalarni e'lon qilish va ular ustida amallar bajarish

    c1=variable1.get() # get metodi birilgan ayni bir funksiya uchun qiymatlarni qaytarib olkish olish uchun ishlatiladi
    c2=variable2.get() # bu yerda "c1", "c2", "c3","c4", lar shartli ravishda belgilangan ifodalar ya'ni o'zgaruvchilar
    c3=variable3.get()
    c4=variable4.get()
    gr1=data[data.country==c1] # data[data.country==c1] - bazadagi ma'lumotlarni tegishli ustundan olish uchun mo'ljallangan
    gr2=data[data.country==c2] # bu yerda "gr1","gr2","gr3","gr3" shartli ravishda belgilandi
    gr3=data[data.country==c3]
    gr4 = data[data.country == c4]
    plt.plot(gr1.year, gr1.freshwater/10**7) # bazadagi ma'lumotlarni ustunlarni olib grafikni chizishda plot metoddan foydalanildi
    plt.plot(gr2.year, gr2.freshwater/10**7)
    plt.plot(gr3.year, gr3.freshwater/10**7)
    plt.plot(gr4.year, gr4.freshwater/10**7)
    plt.legend([c1,c2,c3,c4]) # yaratilgan grafikda chiziqlarni nomlarini farqlash uchun legend metodidan foydalanildi
    plt.xlabel("year") # grafikda gorizantal o'q bo'ylab yillarni ifodalash uchun xlabel metodidan foydalildi
    plt.xlabel("freshwater") # grafikda vertikal o'q bo'ylab suv sarfini ifodalash uchun xlabel metodidan foydalildi
    plt.show() # grafikni ekrang ko'rsatish uchun show () metodi


master = Tk() # Tkinter dasturi ishga tushurilishi bu yerda "master" so'zi shartli yozib olindi
master.geometry("300x200") # bu dasturda interfiys ni o'chamlari geomtriyasi beligilandi

variable1 = StringVar(master) # StringVar tkinter classi metodi bo'lib o'zgaruvchilarni monitoring qilish uchun foydalaniladi
variable1.set("Osiyo") # dasturda yaritilgan tugmaning boshlang'ich qiymati
w1 = OptionMenu(master, variable1, "Uzbekistan", "China", "India", "Indonesia", "Pakistan", "Bangladesh", "Japan",
"Philippines", "Vietnam", "Turkey", "Iran", "Thailand", "Myanmar", "South Korea", "Iraq", "Afghanistan", "Saudi Arabia",
"Malaysia", "Yemen", "Nepal", "North Korea", "Sri Lanka", "Kazakhstan", "Syria", "Cambodia", "Jordan", "Azerbaijan",
"United Arab Emirates", "Tajikistan", "Israel", "Laos", "Lebanon", "Kyrgyzstan", "Turkmenistan", "Singapore", "Oman",
"Palestine", "Kuwait", "Georgia", "Mongolia", "Armenia", "Qatar", "Bahrain", "Cyprus","Bhutan", "Brunei", "Fiji",
"Timor", "Papua New Guinea", "New Zealand", "Maldives", "Australia") # dasturda dropdown tugmasini yaratish uchun OptionMenu metodidan foydalanildi,
# bu yerda "w1" shartli ravishda beilgilandi
w1.config(bg="#e845f7")# config metodi obyektlarni attribularini bilan ishlash imkonini beradi bu yer "bg" background yani
# orqa fon ranglarini o'zgartish uchun foydalanildi bu yerda "#e845f7" esa Color Hex code RGB ranglarni kordinatalarini ifodalashda ishlatiladi,
w1.pack() # pack dasturda yaratilgan tugmalarga qo'yilgan ma'lumotlarni yig'ib interfiysda joylashtirish uchun foydalaniladi


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

btn=Button(master,text="Grafikni chizish", command=chiz, bg="#32a83a", fg="#fff") # yaratilgan dasturda grafini chizmalarini
# chizishda yordam beradigan maxsus tugma.
btn.pack() # pack dasturda yaratilgan tugmalarga qo'yilgan ma'lumotlarni yig'ib interfiysda joylashtirish uchun foydalaniladi
master.mainloop() # mainloop klassi Python dasturi orqali Tkinter ni ishga tushurish uchun ishalatiladi

