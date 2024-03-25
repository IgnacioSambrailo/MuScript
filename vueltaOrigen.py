from ReadWriteMemory import ReadWriteMemory
import pyautogui
from time import sleep
import time

def volver_a_origen(x,y):
    pyautogui.mouseUp(button='right')  
    rwm = ReadWriteMemory()

    process = rwm.get_process_by_name("win9x.exe")
    process.open()

    baseaddress = 0x561014
    baseaddress2 = 0x561018

    xcordenate = process.get_pointer(baseaddress)
    ycordenate = process.get_pointer(baseaddress2)

    value = process.read(xcordenate)
    value2 = process.read(ycordenate)

    #print(value,value2)
    
    tiempo_inicial = time.time()
    tiempo_maximo = 3

    while x != value or y != value2:
        tiempo_actual = time.time()
        tiempo_transcurrido = tiempo_actual - tiempo_inicial
        
        if tiempo_transcurrido >= tiempo_maximo:
            print("Se ha superado el tiempo máximo. Saliendo del bucle.")
            break
        
        if y> value2:
            pyautogui.moveTo(x=550, y=328)
            while y>value2:
                print("estoy aumentando coordenadas y")
                value2 = process.read(ycordenate)
                pyautogui.mouseDown(button='left')
                pyautogui.mouseUp(button='left') 
                pyautogui.mouseDown(button='right')
                pyautogui.mouseUp(button='right') 
                if y == value2:                                       
                    break
        elif y<value2:
            pyautogui.moveTo(x=478, y=376)
            while y<value2:
                print("estoy disminuyendo coordenadas y")
                value2 = process.read(ycordenate)
                pyautogui.mouseDown(button='left')
                pyautogui.mouseUp(button='left') 
                pyautogui.mouseDown(button='right')
                pyautogui.mouseUp(button='right') 
                if y == value2:
                    break
        if x> value:
            pyautogui.moveTo(x=549, y=380)
            while x > value:
                print("estoy aumentando coordenadas x")
                value = process.read(xcordenate)
                pyautogui.mouseDown(button='left')
                pyautogui.mouseUp(button='left') 
                pyautogui.mouseDown(button='right')
                pyautogui.mouseUp(button='right') 
                if x == value:
                    break
        elif x<value:
            pyautogui.moveTo(x=479 - 10, y=342 - 20)
            while x < value:
                print("estoy disminuyendo coordenadas x")
                value = process.read(xcordenate)
                pyautogui.mouseDown(button='left')
                pyautogui.mouseUp(button='left') 
                pyautogui.mouseDown(button='right')
                pyautogui.mouseUp(button='right') 
                if x == value:
                    break




