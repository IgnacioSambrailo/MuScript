from ReadWriteMemory import ReadWriteMemory
import pyautogui
from time import sleep

while 1:
    rwm = ReadWriteMemory()

    process = rwm.get_process_by_name("win9x.exe")
    process.open()

    baseaddress = 0xEB02000

    zen = process.get_pointer(baseaddress)

    value = process.read(zen)
    if value <1292413704 or value>1292413704:
        print(value)
