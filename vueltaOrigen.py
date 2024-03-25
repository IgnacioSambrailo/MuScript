from ReadWriteMemory import ReadWriteMemory
import pyautogui
from time import sleep


def volver_a_origen(x,y):
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

    while x != value and y != value2:
        if y> value2:
            pyautogui.moveTo(x=550, y=328)
            while y>value2:
                print("estoy aumentando coordenadas y")
                value2 = process.read(ycordenate)
                pyautogui.mouseDown(button='left')
                pyautogui.mouseUp(button='left')
                if y == value2:
                    break
        elif y<value2:
            pyautogui.moveTo(x=478, y=376)
            while y<value2:
                print("estoy disminuyendo coordenadas y")
                value2 = process.read(ycordenate)
                pyautogui.mouseDown(button='left')
                pyautogui.mouseUp(button='left')
                if y == value2:
                    break
        if x> value:
            pyautogui.moveTo(x=549, y=380)
            while x > value:
                print("estoy aumentando coordenadas x")
                value = process.read(xcordenate)
                pyautogui.mouseDown(button='left')
                pyautogui.mouseUp(button='left')
                if x == value:
                    break
        elif x<value:
            pyautogui.moveTo(x=479, y=342)
            while x < value:
                print("estoy disminuyendo coordenadas x")
                value = process.read(xcordenate)
                pyautogui.mouseDown(button='left')
                pyautogui.mouseUp(button='left')
                if x == value:
                    break




