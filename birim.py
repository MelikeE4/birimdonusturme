import tkinter as tk

def hesapla():
    derece=float(ekran1.get())
    f=((derece/100)*180)+32

    ekran2.insert(0,f)

def cevir():
    derece=float(ekran1.get())
    c=((derece-32)*5/9)

    ekran2.insert(0,c)

def donustur():
    derece=float(ekran1.get())
    k=(derece+273)

    ekran2.insert(0,k)

pencere=tk.Tk()
pencere.title("Birim Dönüştürücü")
pencere.config(bg="light pink")
pencere.geometry("600x600")

label1=tk.Label(pencere,text="Dönüştürülecek Değer")
label1.pack()

ekran1=tk.Entry(pencere)
ekran1.pack()

ekran2=tk.Entry(pencere)
ekran2.pack()

buton1=tk.Button(pencere,text="Dereceyi Fahrenheita Dönüştür",command=lambda:hesapla())
buton1.pack()

buton2=tk.Button(pencere,text="Fahrenheitı Dereceye Dönüştür",command=lambda:cevir())
buton2.pack()

buton3=tk.Button(pencere,text="Dereceyi Kelvine Dönüştür",command=lambda:donustur())
buton3.pack()

pencere.mainloop()