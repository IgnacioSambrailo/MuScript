from time import time,sleep
import pyautogui
from windowcapture import WindowCapture
from vision import Vision
import keyboard
from tkinter import *
import sys
import os
from vueltaOrigen import volver_a_origen
import time

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
def quit():
    pyautogui.keyUp('alt')
    global exitProgram
    exitProgram = True


keyboard.add_hotkey('F2', lambda: quit())

def juntar_zen(nombre_ventana, coordenadas_origen):
    sleep(2)
    global coordenadas_finales
    global coordenadas_iniciales
    global exitProgram
    # initialize the WindowCapture class
    wincap = WindowCapture(f"{nombre_ventana}")

    def resolver_ruta(ruta_relativa):
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, ruta_relativa)

    # initialize the Vision class
    vision_limestone = Vision(resolver_ruta('zen.png'))
    exitProgram = False

    loop_time = time.time()
    
    

    def esperar_sin_bloquear(tiempo_espera):
        inicio = time.time()
        while time.time() - inicio < tiempo_espera:
            if len(vision_limestone.find(wincap.get_screenshot(), 0.95)) > 0:
                return True  # Se detectaron rectángulos, se puede salir de la espera
            time.sleep(0.1)  # Pequeño tiempo de espera para evitar uso excesivo de CPU
        return False  # Se agotó el tiempo de espera sin detectar rectángulos

    while not exitProgram:
        pyautogui.keyDown('alt')
        time.sleep(0.5)  # Tiempo para asegurarse de que la tecla 'Alt' esté presionada
        # Capturar una nueva imagen del juego
        screenshot = wincap.get_screenshot()

        # Realizar la detección de objetos
        rectangles = vision_limestone.find(screenshot, 0.95)

        # Dibujar los resultados de detección en la imagen original
        output_image = vision_limestone.draw_rectangles(screenshot, rectangles)

        flag = 0
        # Tomar acciones del bot
        if len(rectangles) > 0:
            pyautogui.mouseUp(button='right')            
            # Obtener el primer objeto detectado en la lista y encontrar el lugar para hacer clic
            flag += 1
            targets = vision_limestone.get_click_points(rectangles)
            target = wincap.get_screen_position(targets[0])
            pyautogui.moveTo(x=target[0]+15, y=target[1]+20)
            pyautogui.mouseDown(button='left')
            pyautogui.mouseUp(button='left')
            pyautogui.mouseDown(button='left')
            pyautogui.mouseUp(button='left')
        else:
            pyautogui.mouseDown(button='right')
            # Esperar sin bloquear durante 5 segundos o hasta que se detecten rectángulos
            if not esperar_sin_bloquear(5):
                volver_a_origen(coordenadas_origen[0],coordenadas_origen[1])

        loop_time = time.time()  # Actualizar el tiempo de referencia para el bucle

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



class VentanaMu:
    def __init__(self,ventana):
        self.ventana = ventana
        self.ventana.title("v.2.0")
        self.ventana.geometry("220x200")
        self.ventana.resizable(False, False)


        self.ventana_mu = StringVar(self.ventana)
        self.coordenadas = StringVar(self.ventana)

        def ejecutar():
            print("arranca")
            coordenadas = self.coordenadas.get().split(",")
            coordenadas[0] = int(coordenadas[0])
            coordenadas[1] = int(coordenadas[1])
            juntar_zen(self.ventana_mu.get(),coordenadas)




        # LBL - INGRESAR NOMBRE
        lblInputMu = Label(self.ventana,text='Ingresa el nombre de la ventana \ndel mu', justify=LEFT)
        lblInputMu.place(x=18,y=7)

          # LBL - INGRESAR COORDENADAS
        lblInputMu = Label(self.ventana,text='Ingresa coordenadas origen', justify=LEFT)
        lblInputMu.place(x=18,y=67)

        # ENTRY - NOMBRE VENTANA
        entryVenta = Entry(self.ventana, textvariable=self.ventana_mu)
        entryVenta.place(x=85,y=25)

        # ENTRY - NOMBRE COORDENADAS
        entryVenta = Entry(self.ventana, textvariable=self.coordenadas)
        entryVenta.place(x=85,y=87)

         # LBL - ACLARACION
        lblFinalizar = Label(self.ventana, text='Para finalizar presione F2', justify=LEFT)
        lblFinalizar.place(x=19, y=125)

        # BTN - COMENZAR
        btnComenzar = Button(self.ventana,text="Comenzar", command=ejecutar)
        btnComenzar.place(x=80, y=156)






if __name__ == "__main__":
    ventana = Tk()
    aplicacion = VentanaMu(ventana)
    ventana.mainloop()


