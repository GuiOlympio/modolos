import urllib.request
from tkinter.messagebox import showinfo
from webbrowser import open

try:
    p = urllib.request.Request("https://www.pudim.com.br/")
except:
    print(f'\033[0:31mERRO\033[m')
else:
    print("Encontrei o site do pudim!! :)")