import time
from tkinter import *
import requests
from PIL import ImageTk, Image
from datetime import datetime, timedelta
from configparser import ConfigParser
from ping3 import ping


root = Tk()
root.attributes('-fullscreen', True)
root.geometry("1024x780")
root.config(background="black")
root.update()
time.sleep(1)
Logo = ImageTk.PhotoImage(file="IMG/Logo.png")
canvas1 = Canvas(width=1024, height=768, )
canvas1.pack()
canvas1.update()

FechaHoy = datetime.today()
FechaAyer = FechaHoy - timedelta(days=1)
FechaHoy = FechaHoy.strftime("%d-%m-%Y")
FechaAyer = FechaAyer.strftime("%d-%m-%Y")

Y = [148,
     302,
     458,
     611]

Filas = [[36, 282, 528, 774],
         [36, 282, 528, 774],
         [36, 282, 528, 774],
         [36, 282, 528, 774]]

Lots = [["la primera 12pm", "la suerte 12.30pm", "q real", "nac t" ],
        ["la primera 8pm", "la suerte 6pm", "q pale", "nac n"],
        ["lotedom", "loteka", "king lot dia", "king lot noche"],
        ["ny dia", "ny noche", "fl tarde", 'fl noche'],
        ["anguilla 10am", "anguilla 1pm", "anguilla 6pm","anguilla 9pm"]] #Esta fila es para que funcione Premion_en_grande() con la anguilla
        
ImagenFilas2 = [["PrimeraD.png", "SuerteD.png", "Real.png", "NT.png"],
                ["PrimeraN.png", "SuerteN.png", "QP.png", "NN.png"],
                ["LTD.png", "LTK.png", "KLD.png", "KLN.png"],
                ["NYD.png", "NYN.png", "FLD.png", "FLN.png"],
                ["ANG.png"]]  #Esta fila es para que funcione Premion_en_grande() con la anguilla
                

# Para la Anguilla
X_ang = [36, 794]
Y_ang = 14
Lots_ang = ["anguilla 10am", "anguilla 1pm", "anguilla 6pm", "anguilla 9pm" ]



TardeNoche = ["TARDE", "NOCHE"]
HoraAng = ["10:00 am", "1:00 pm", "6:00 pm", "9:00 pm"]
Colores = ["gray12", "gray13", "gray14"]

Images_G = {}
Images_P = {}
buf0 = Image.open("IMG/BolaAzul.png").resize((250, 250), Image.ANTIALIAS)
Images_G["BolaAzul"] = ImageTk.PhotoImage(buf0)
buf0 = Image.open("IMG/BolaAzul.png").resize((65, 65), Image.ANTIALIAS)
Images_P["BolaAzul"] = ImageTk.PhotoImage(buf0)

buf0 = Image.open("IMG/BolaBlanca.png").resize((250, 250), Image.ANTIALIAS)
Images_G["BolaBlanca"] = ImageTk.PhotoImage(buf0)
buf0 = Image.open("IMG/BolaBlanca.png").resize((65, 65), Image.ANTIALIAS)
Images_P["BolaBlanca"] = ImageTk.PhotoImage(buf0)

#Para la Anguilla
buf0 = Image.open("IMG/BolaAzul.png").resize((45, 45), Image.ANTIALIAS)
Images_P["BolaAzul_ang"] = ImageTk.PhotoImage(buf0)
buf0 = Image.open("IMG/BolaBlanca.png").resize((45, 45), Image.ANTIALIAS)
Images_P["BolaBlanca_ang"] = ImageTk.PhotoImage(buf0)

for i in ImagenFilas2:
    for j in i:
        buf = Image.open("IMG/" + j)
        buf1 = buf.resize((1024, 226), Image.ANTIALIAS)
        buf2 = buf.resize((210, 50), Image.ANTIALIAS)
        Images_G[Lots[ImagenFilas2.index(i)][i.index(j)]] = ImageTk.PhotoImage(buf1)
        Images_P[Lots[ImagenFilas2.index(i)][i.index(j)]] = ImageTk.PhotoImage(buf2)
        
#Para la Anguilla
buf = Image.open("IMG/ANG.png")
buf1 = buf.resize((1024, 226), Image.ANTIALIAS)
buf2 = buf.resize((210, 35), Image.ANTIALIAS)
Images_G["anguilla"] = ImageTk.PhotoImage(buf1)
Images_P["anguilla"] = ImageTk.PhotoImage(buf2)


def comprobar_conexion():
    while True:
        try:     
            if ping('8.8.8.8'):
                break
        except:
            print("error.") 
        time.sleep(5)
    

def _Pausa_():
    canvas1.update()
    time.sleep(0.07)
    #time.sleep(0.01)

def descargar_premios():
    url = "https://drive.google.com/u/0/uc?id=1xoK8xsJ014ijRmCHnP4ZNjyv_NTI7thh"
    response = ""
    try:
        response = requests.get(url).text
    except:
        print("error")

    if "nac n" in response:
        with open("Premios.ini", 'w') as file:
            file.write(response)

def Premion_en_grande():
    Lista_G = []
    ini2 = ConfigParser()
    ini2.read("Premios.ini")
    try:
        for key, value in ini2.items(str(FechaHoy)):
            if not value == "":
                if not value == ini.get(str(FechaHoy), key):
                    P = value.replace("100", "00")
                    P = P.split(",")
                    Dix = {"Loteria": key, "Fecha": FechaHoy, "Pr": P[0], "Se": P[1], "Te": P[2],
                           "Circulo": Images_G["BolaAzul"],
                           "Color": "navy"}
                    Lista_G.append(Dix)
        if Lista_G:
            for i in Lots:
                for j in i:
                    for k in Lista_G:
                        if k["Loteria"] == j:
                            if "anguilla " in j:
                                j = "anguilla 10am"
                            # if "ny " in j:
                                # j = "ny dia"
                            # if "fl " in j:
                                # j = "fl tarde"
                            canvas1.create_rectangle(0, 0, 1024, 768, fill="white", outline="")
                            _Pausa_()
                            canvas1.create_image(512, 113, image=Images_G[j])
                            _Pausa_()
                            canvas1.create_image(185, 409, image=Images_G["BolaAzul"])
                            _Pausa_()
                            canvas1.create_image(513, 409, image=Images_G["BolaAzul"])
                            _Pausa_()
                            canvas1.create_image(840, 409, image=Images_G["BolaAzul"])
                            _Pausa_()
                            canvas1.create_text(512, 620, text=k["Fecha"], fill=k["Color"], font='Ebrima 60 bold')
                            _Pausa_()
                            canvas1.create_text(185, 409, text=k["Pr"], font='Ebrima 120 bold')
                            _Pausa_()
                            canvas1.create_text(513, 409, text=k["Se"], font='Ebrima 120 bold')
                            _Pausa_()
                            canvas1.create_text(840, 409, text=k["Te"], font='Ebrima 120 bold')
                            _Pausa_()
                            time.sleep(30)
                            canvas1.create_rectangle(0, 0, 1024, 768, fill="black", outline="")
                            _Pausa_()
    except:
        print("error Premion_en_grande")

    ini.read("Premios.ini")


def pizarra():
    try:   
        ini.read("Premios.ini")
        descargar_premios()
        Premion_en_grande()
    
        # canvas1.config(background="black", highlightthickness=10, highlightbackground="cyan2")
        canvas1.config(background="black", highlightthickness=0)
        canvas1.pack()
        _Pausa_()
        canvas1.create_rectangle(256, 14, 780, 144, fill="black", outline="")
        _Pausa_()
        time.sleep(0.5)
        canvas1.create_image(525, 79, image=Logo)
        _Pausa_()
    
        Lista = []
        ini.read("Premios.ini")
        try:
            
            if ini.has_section(str(FechaHoy)):
                for key, value in ini.items(str(FechaHoy)):
                    if value == "":
                        if ini.get(str(FechaAyer), key) == "":
                            Dix = {"Loteria": key, "Fecha": "--/--/----", "Pr": "--", "Se": "--", "Te": "--",
                                   "Circulo": Images_P["BolaBlanca"],
                                   "Color": "tan4"}
                            Lista.append(Dix)
                            continue
            
                        P = ini.get(str(FechaAyer), key)
                        P = P.replace("100", "00")
                        P = P.split(",")
                        Dix = {"Loteria": key, "Fecha": FechaAyer, "Pr": P[0], "Se": P[1], "Te": P[2],
                               "Circulo": Images_P["BolaBlanca"], "Color": "tan4"}
                        Lista.append(Dix)
                    else:
                        P = value.replace("100", "00")
                        P = P.split(",")
                        Dix = {"Loteria": key, "Fecha": FechaHoy, "Pr": P[0], "Se": P[1], "Te": P[2],
                               "Circulo": Images_P["BolaAzul"], "Color": "navy"}
                        Lista.append(Dix)
            else:
                for key, value in ini.items(str(FechaAyer)):
                    if value == "":
                        Dix = {"Loteria": key, "Fecha": "--/--/----", "Pr": "--", "Se": "--", "Te": "--",
                               "Circulo": Images_P["BolaBlanca"],
                               "Color": "tan4"}
                        Lista.append(Dix)
                        continue
        
                    P = value
                    P = P.replace("100", "00")
                    P = P.split(",")
                    Dix = {"Loteria": key, "Fecha": FechaAyer, "Pr": P[0], "Se": P[1], "Te": P[2],
                           "Circulo": Images_P["BolaBlanca"], "Color": "tan4"}
                    Lista.append(Dix)
        except:
            print("error pizarra")
    
        for h in Y:
            for x in Filas[Y.index(h)]:
                
                canvas1.create_rectangle(x, h, x + 240, h + 128, fill="black", outline="")
                _Pausa_()
                time.sleep(0.3)
                canvas1.create_rectangle(x, h, x + 240, h + 128, fill="white", outline="")
                _Pausa_()
                canvas1.create_image(x + 120, h + 24, image=Images_P[Lots[Y.index(h)][Filas[Y.index(h)].index(x)]])
                _Pausa_()
                Data = next((item for item in Lista if item["Loteria"] == Lots[Y.index(h)][Filas[Y.index(h)].index(x)]), None)
                canvas1.create_image(x + 45, h + 75, image=Data["Circulo"])
                _Pausa_()
                canvas1.create_image(x + 120, h + 75, image=Data["Circulo"])
                _Pausa_()
                canvas1.create_image(x + 195, h + 75, image=Data["Circulo"])
                _Pausa_()
                canvas1.create_text(x + 120, h + 120, text=Data["Fecha"], fill=Data["Color"], font=('Ebrima 12 bold'))
                _Pausa_()
    
                canvas1.create_text(x + 45, h + 75, text=Data["Pr"], font=('Ebrima 28 bold'))
                _Pausa_()
                canvas1.create_text(x + 120, h + 75, text=Data["Se"], font=('Ebrima 28 bold'))
                _Pausa_()
                canvas1.create_text(x + 195, h + 75, text=Data["Te"], font=('Ebrima 28 bold'))
                _Pausa_()
                continue
        
        for x in X_ang:
            canvas1.create_rectangle(x, Y_ang, x + 220, Y_ang + 128, fill="black", outline="")
            _Pausa_()
            time.sleep(0.3)
            canvas1.create_rectangle(x, Y_ang, x + 220, Y_ang + 128, fill="white", outline="")
            _Pausa_()
            canvas1.create_image(x + 110, Y_ang + 18, image=Images_P["anguilla"])
            _Pausa_() 
            
            if X_ang.index(x) == 0:
                for lot in Lots_ang:
                    if lot == "anguilla 10am":
                        Data = next((item for item in Lista if item["Loteria"] == "anguilla 10am"), None)
                        h = Y_ang + 56
                        canvas1.create_text(x + 30, h, text="10am", fill="Black", font=('Arial 19 bold'))
                        _Pausa_()
                    elif lot == "anguilla 1pm":
                        Data = next((item for item in Lista if item["Loteria"] == "anguilla 1pm"), None)
                        h = Y_ang + 103
                        canvas1.create_text(x + 30, h, text="1pm", fill="Black", font=('Arial 20 bold'))
                        _Pausa_()
                    else:
                        continue
                    if Data["Circulo"] == Images_P["BolaAzul"]:
                        Bolo = Images_P["BolaAzul_ang"]
                    else:
                        Bolo = Images_P["BolaBlanca_ang"]
                    canvas1.create_image(x + 90, h, image=Bolo)
                    _Pausa_()
                    canvas1.create_image(x + 140, h, image=Bolo)
                    _Pausa_()
                    canvas1.create_image(x + 190, h, image=Bolo)
                    _Pausa_()
                    canvas1.create_text(x + 90, h, text=Data["Pr"], font=('Ebrima 20 bold'))
                    _Pausa_()
                    canvas1.create_text(x + 140, h, text=Data["Se"], font=('Ebrima 20 bold'))
                    _Pausa_()
                    canvas1.create_text(x + 190, h, text=Data["Te"], font=('Ebrima 20 bold'))
                    _Pausa_()
            else:
                for lot in Lots_ang:
                    if lot == "anguilla 6pm":
                        Data = next((item for item in Lista if item["Loteria"] == "anguilla 6pm"), None)
                        h = Y_ang + 56
                        canvas1.create_text(x + 30, h, text="6pm", fill="Black", font=('Arial 20 bold'))
                        _Pausa_()
                    elif lot == "anguilla 9pm":
                        Data = next((item for item in Lista if item["Loteria"] == "anguilla 9pm"), None)
                        h = Y_ang + 103
                        canvas1.create_text(x + 30, h, text="9pm", fill="Black", font=('Arial 20 bold'))
                        _Pausa_()
                    else:
                        continue
                    if Data["Circulo"] == Images_P["BolaAzul"]:
                        Bolo = Images_P["BolaAzul_ang"]
                    else:
                        Bolo = Images_P["BolaBlanca_ang"]
                    canvas1.create_image(x + 90, h, image=Bolo)
                    _Pausa_()
                    canvas1.create_image(x + 140, h, image=Bolo)
                    _Pausa_()
                    canvas1.create_image(x + 190, h, image=Bolo)
                    _Pausa_()
                    canvas1.create_text(x + 90, h, text=Data["Pr"], font=('Ebrima 20 bold'))
                    _Pausa_()
                    canvas1.create_text(x + 140, h, text=Data["Se"], font=('Ebrima 20 bold'))
                    _Pausa_()
                    canvas1.create_text(x + 190, h, text=Data["Te"], font=('Ebrima 20 bold'))
                    _Pausa_()
                   
    
        canvas1.update()
        root.after(180000, pizarra)
    except:
        print("error pizarra")
        canvas1.update()
        root.after(10000, pizarra)

#comprobar_conexion()
descargar_premios()
ini = ConfigParser()

root.after(5000, pizarra)

root.mainloop()
