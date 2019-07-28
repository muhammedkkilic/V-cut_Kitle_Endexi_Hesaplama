import tkinter as tk
from tkinter import *
from tkinter import messagebox
from math import sqrt
def hesapla():
    if(boyunuz_text.get()==''):
        messagebox.showinfo('Uyarı','Lütfen Boyunuzu Giriniz')
        return
    if(kilonuz_text.get()==''):
        messagebox.showinfo('Uyarı', 'Lütfen Kilonuzu Giriniz')
        return
    b = int(boyunuz_text.get())
    k = int(kilonuz_text.get())
    sonuc = k / ((b/100)*(b/100))
    if (cinsiyet.get() == 1):
        ideal_kilo = 45.5 + (2.3 / 2.54) * (b - 152.4)
    if (cinsiyet.get() == 2):
        ideal_kilo = 50 + (2.3 / 2.54) * (b - 152.4)
    var3.set(int(ideal_kilo))
    if (sonuc <= 18.4) :
        sonuc_text.config(fg="Red")
        var2.set('İdeal kilonuzun altındasınız')
    elif (sonuc >= 18.5 and sonuc <= 24.9):
        sonuc_text.config(fg="Green")
        var2.set('Kilonuz tamamen normal')
    elif(sonuc >= 25.0 and sonuc <= 29.9):
        sonuc_text.config(fg="Red")
        var2.set('İdeal kilonuzun üstündesiniz')
    elif(sonuc >= 30.0 and sonuc <=34.9):
        sonuc_text.config(fg="Red")
        var2.set('Şişman (Obez) - I. Sınıf')
    elif(sonuc >= 35.0 and sonuc<= 44.):
        sonuc_text.config(fg="Red")
        var2.set('Şişman (Obez) - II. Sınıf')
    elif(sonuc >= 45.0):
        sonuc_text.config(fg="Red")
        var2.set('Aşırı Şişman (Aşırı Obez) - III. Sınıf')
    var.set(round(sonuc,1))

def temizle():
    boyunuz_text.delete(0,tk.END)
    kilonuz_text.delete(0,tk.END)
    var.set('')
    var2.set('')
    var3.set('')

pencere = tk.Tk();
pencere.geometry("700x400")
pencere.title('Vücut Kitle Endexi')

var= StringVar()
var2 =StringVar()
var3 = StringVar()

cinsiyetiniz_basligi = tk.Label(text='Cinsiyetiniz')
cinsiyetiniz_basligi.place(x=60,y=70)

cinsiyet = IntVar()
bayan = tk.Radiobutton(text='Bayan',variable=cinsiyet,value=1)
bayan.place(x=180,y=70)

bay = tk.Radiobutton(text='Bay',variable=cinsiyet,value=2)
bay.place(x=180,y=100)

bayan.select()

baslik_labeli = tk.Label(text='Vücut Kitle Endexi Hesaplama Aracı')
baslik_labeli.place(x=150,y=20)

boyunuz_labeli = tk.Label(text='Boyunuz')
boyunuz_labeli.place(x=60,y=140)

boyunuz_text = tk.Entry();
boyunuz_text.place(x=150,y=140)

kilonuz_labeli = tk.Label(text='Kilonuz')
kilonuz_labeli.place(x=60,y=190)

kilonuz_text = tk.Entry();
kilonuz_text.place(x=150,y=190)

hesapla_butonu = tk.Button(text='HESAPLA',command=hesapla)
hesapla_butonu.place(x=120,y=240)

kitle_endexi_labeli = tk.Label(text='Vücut Kitle Endeksiniz (BMI):')
kitle_endexi_labeli.place(x=350,y=70)

kitle_endexi_text = tk.Label(textvariable=var)
kitle_endexi_text.place(x=520,y=70)

sonuc_baslik_labeli = tk.Label(text='Sonuç :')
sonuc_baslik_labeli.place(x=350,y=140)

sonuc_text = tk.Label(textvariable=var2)
sonuc_text.config(fg="Red")
sonuc_text.place(x=400,y=140)

ideal_kilo_label = tk.Label(text='İdeal Kilonuz :')
ideal_kilo_label.place(x=350,y=190)

ideal_kilo_text = tk.Label(textvariable=var3)
ideal_kilo_text.place(x=440,y=190)

temizle_butonu = tk.Button(text="TEMİZLE" ,command=temizle)
temizle_butonu.place(x=260,y=240)

pencere.mainloop();