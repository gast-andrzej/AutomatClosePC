import time
import os

def func1():
    x = int(input("Za ile czasu chcesz zamknąć komputer (minut) "))
    time.sleep(x*60)
    os.system("shutdown /s /t 1")

func1()