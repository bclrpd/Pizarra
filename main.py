import time
from tkinter import *
import requests
import PIL
from PIL import ImageTk, Image
PIL.Image.ANTIALIAS = PIL.Image.LANCZOS
from datetime import datetime, timedelta
from configparser import ConfigParser
from ping3 import ping

# Función para verificar la conexión a Internet
def check_internet_connection():
    while True:
        try:
            if ping('8.8.8.8'):
                break
        except:
            print("Error al verificar la conexión a Internet.")
        time.sleep(5)

# Función para descargar los premios desde la URL
def download_premios():
    url = "https://drive.google.com/u/0/uc?id=1xoK8xsJ014ijRmCHnP4ZNjyv_NTI7thh"
    try:
        response = requests.get(url).text
        if "nac n" in response:
            with open("Premios.ini", 'w') as file:
                file.write(response)
    except Exception as e:
        print(f"Error al descargar premios: {e}")

# Función para mostrar los premios en grande
def display_premios_grandes():
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
    except Exception as e:
        print(f"Error en display_premios_grandes: {e}")

    ini.read("Premios.ini")

# Función para mostrar los premios en la pizarra


def pizarra():
    try:
        ini.read("Premios.ini")
        download_premios()
        display_premios_grandes()

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
        except Exception as e:
            print(f"Error reading prize data: {e}")


        for h, fila in zip(Y, Filas):
            for x in fila:
                canvas1.create_rectangle(x, h, x + 240, h + 128, fill="black", outline="")
                _Pausa_()
                time.sleep(0.3)
                canvas1.create_rectangle(x, h, x + 240, h + 128, fill="white", outline="")
                _Pausa_()
                loteria = Lots[Y.index(h)][Filas[Y.index(h)].index(x)]
                canvas1.create_image(x + 120, h + 24, image=Images_P[loteria])
                _Pausa_()
                Data = next((item for item in Lista if item["Loteria"] == loteria), None)
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

        canvas1.update()
        root.after(180000, pizarra)
    except Exception as e:
        print(f"Error al mostrar los premios en la pizarra: {e}")
        canvas1.update()
        root.after(10000, pizarra)

def _Pausa_():
    canvas1.update()
    time.sleep(0.07)

# Configuración de la ventana principal
root = Tk()
root.attributes('-fullscreen', True)
root.geometry("1024x780")
root.config(background="black")
root.update()
time.sleep(1)

# Cargar imágenes y crear elementos de la interfaz
#Logo = ImageTk.PhotoImage(file="IMG/Logo.png")
buf0 = Image.open("IMG/Logo.png").resize((480, 130), Image.ANTIALIAS)
Logo = ImageTk.PhotoImage(buf0)
canvas1 = Canvas(width=1024, height=768, )
canvas1.pack()
canvas1.update()

FechaHoy = datetime.today()
FechaAyer = FechaHoy - timedelta(days=1)
FechaHoy = FechaHoy.strftime("%d-%m-%Y")
FechaAyer = FechaAyer.strftime("%d-%m-%Y")

#Y = [14, 148, 302, 458, 611]
Y = [14, 163, 312, 463, 611]

Filas = [[36, 774],
		 [36, 282, 528, 774],
         [36, 282, 528, 774],
         [36, 282, 528, 774],
         [36, 282, 528, 774]]

Lots = [[ "fl tarde", 'fl noche'],
		["la primera 12pm", "la suerte 12.30pm", "q real", "nac t"],
        ["la primera 8pm", "la suerte 6pm", "q pale", "nac n"],
        ["lotedom", "loteka", "ny dia", "ny noche"],
        ["anguilla 10am", "anguilla 1pm", "anguilla 6pm", "anguilla 9pm"]]

ImagenFilas2 = [["FLD.png", "FLN.png"],
				["PrimeraD.png", "SuerteD.png", "Real.png", "NT.png"],
                ["PrimeraN.png", "SuerteN.png", "QP.png", "NN.png"],
                ["LTD.png", "LTK.png", "NYD.png", "NYN.png"],
                ["ANG10am.png", "ANG1pm.png", "ANG6pm.png", "ANG9pm.png"]]

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

for i in ImagenFilas2:
    for j in i:
        buf = Image.open("IMG/" + j)
        buf1 = buf.resize((1024, 226), Image.ANTIALIAS)
        buf2 = buf.resize((210, 50), Image.ANTIALIAS)
        Images_G[Lots[ImagenFilas2.index(i)][i.index(j)]] = ImageTk.PhotoImage(buf1)
        Images_P[Lots[ImagenFilas2.index(i)][i.index(j)]] = ImageTk.PhotoImage(buf2)


# Verificar la conexión a Internet y descargar los premios inicialmente
check_internet_connection()
download_premios()
ini = ConfigParser()

# Iniciar la visualización de los premios en la pizarra
root.after(5000, pizarra)

root.mainloop()
