from tkinter import *
from tkinter import messagebox as mb
import webview
import config
import localization.ru_ru.about as lra
import localization.en_us.about as lea
import localization.ru_ru.main as lrm
import localization.en_us.main as lem
from tkinter.ttk import *
import os



plugins = []






nametext = None
desctext = None
welcometext = None
gotext = None
aboutxt = None
webengine = None


if config.LOCALIZATION == "ru_ru":
    nametext = lra.NAME
    desctext = lra.DESC
    welcometext = lrm.WELCOME
    gotext = lrm.GOBTN
    aboutxt = lrm.ABOUTWINDOW
if config.LOCALIZATION == "en_us":
    nametext = lea.NAME
    desctext = lea.DESC
    welcometext = lem.WELCOME
    gotext = lem.GOBTN
    aboutxt = lem.ABOUTWINDOW





window = Tk()
window.title("RetroBrowsing 1.0")
window.geometry("1024x768")
def goon():
    if config.WEB_ENGINE == "DEFAULT":
        if webname.get() == "RetroBrowsing/about" or webname.get() == "RetroBrowsing/About":
            aboutttt()
        if webname.get() == "RetroBrowsing/guidebook" or webname.get() == "RetroBrowsing/Guidebook":
            guidebookk()
        if webname.get() == "RetroBrowsing/config" or webname.get() == "RetroBrowsing/Config":
            webview.create_window('RetroBrowsing/Config', 'config.py')
            webview.start(http_server=True)
        if 'file:' in webname.get():
            filepathlox = webname.get()
            filepath = filepathlox.split(":")
            webview.create_window(f'File: {filepath[1]}', filepath[1])
            webview.start(http_server=True)
        else: 
            if '.' in webname.get():
                window = webview.create_window(f'{webname.get()}', f'http://{webname.get()}')
                webview.start()
            else:
                mb.showerror(title="Invalid Parameter!", message="Invalid website addres or command!")
    else:
        if webname.get() == "RetroBrowsing/about" or webname.get() == "RetroBrowsing/About":
            aboutttt()
        if webname.get() == "RetroBrowsing/guidebook" or webname.get() == "RetroBrowsing/Guidebook":
            guidebookk()
        if webname.get() == "RetroBrowsing/config" or webname.get() == "RetroBrowsing/Config":
            webview.create_window('RetroBrowsing/Config', 'config.py')
            webview.start(http_server=True)
        if 'file:' in webname.get():
            filepathlox = webname.get()
            filepath = filepathlox.split(":")
            webview.create_window(f'File: {filepath[1]}', filepath[1])
            webview.start(http_server=True, gui=config.WEB_ENGINE)
        else: 
            if '.' in webname.get():
                window = webview.create_window(f'{webname.get()}', f'http://{webname.get()}')
                webview.start(gui=config.WEB_ENGINE)
            else:
                mb.showerror(title="Invalid Parameter!", message="Invalid website addres or command!")
def aboutttt():
    newWindow = Toplevel(window)
    newWindow.title("RetroBrowsing 1.0")
    name = Label(newWindow, text=f"RetroBrowsing {config.VERSION}")
    desc = Label(newWindow, text=desctext)
    githubb = Button(newWindow, text="Github", command=github)
    supportprj = Button(newWindow, text="Support on hoc22", command=supportprojecthoc22)
    guidebook = Button(newWindow, text="GuideBook", command=guidebookk)
    name.pack()
    desc.pack()
    guidebook.pack()
    githubb.pack()
    supportprj.pack()
    newWindow.mainloop()
def guidebookk():
    if config.WEB_ENGINE == "DEFAULT":
        webview.create_window('RetroBrowsing/GuideBook', 'htmls/guidebook.html')
        webview.start(http_server=True)
    else:
        webview.create_window('RetroBrowsing/GuideBook', 'htmls/guidebook.html')
        webview.start(http_server=True, gui=config.WEB_ENGINE)

def github():
    if config.WEB_ENGINE == "DEFAULT":
        window = webview.create_window('RetroBrowsing/GitHub', f'http://github.com/z3ven/RetroBrowsing')
        webview.start()
    else:
        window = webview.create_window('RetroBrowsing/GitHub', f'http://github.com/z3ven/RetroBrowsing')
        webview.start(gui=config.WEB_ENGINE)  
def supportprojecthoc22():
    if config.WEB_ENGINE == "DEFAULT":
        window = webview.create_window('RetroBrowsing/hoc2022', f'http://learn.algoritmika.az/')
        webview.start() 
    else:
        window = webview.create_window('RetroBrowsing/hoc2022', f'http://learn.algoritmika.az/')
        webview.start(gui=config.WEB_ENGINE) 

def youtubee():
    if config.WEB_ENGINE == "DEFAULT":
        window = webview.create_window('YouTube', f'http://youtube.com/')
        webview.start()
    else:
        window = webview.create_window('YouTube', f'http://youtube.com/')
        webview.start(gui=config.WEB_ENGINE)
def instagram():
    if config.WEB_ENGINE == "DEFAULT":
        window = webview.create_window('Instagram', f'http://intagram.com/')
        webview.start() 
    else:  
        window = webview.create_window('Instagram', f'http://intagram.com/')
        webview.start(gui=config.WEB_ENGINE)   
def facebook():
    if config.WEB_ENGINE == "DEFAULT":
        window = webview.create_window('FaceBook', f'http://facebook.com/')
        webview.start(gui=config.WEB_ENGINE) 
    else:  
        window = webview.create_window('FaceBook', f'http://facebook.com/')
        webview.start(gui=config.WEB_ENGINE)   
def twitter():
    if config.WEB_ENGINE == "DEFAULT":
        window = webview.create_window('Twitter', f'http://twitter.com/')
        webview.start(gui=config.WEB_ENGINE) 
    else:  
        window = webview.create_window('Twitter', f'http://twitter.com/')
        webview.start(gui=config.WEB_ENGINE)  

welcomeL = Label(width=180, text=welcometext)
webname = Entry(width=100)
go = Button(width=50, text=gotext, command=goon)
aboutt = Button(width=15, text=aboutxt, command=aboutttt)
fastrecources = Label(text="Recources: ")
youtube = Button(text="YouTube", command=youtubee)
insta = Button(text="Instagram", command=instagram)
faceb = Button(text="FaceBook", command=facebook)
twiiter = Button(text="Twitter", command=twitter)



welcomeL.pack()
webname.pack()
go.pack()
fastrecources.pack()
youtube.pack()
insta.pack()
faceb.pack()
twiiter.pack()
aboutt.pack()


'''
def pluginsystem():
        for path in os.listdir(config.PLUGINS):
            if os.path.isfile(os.path.join(config.PLUGINS, path)):
                plugins.append(path)
        for plugin in plugins:
            os.system(f'python plugins/{plugin}')
'''
if __name__ == "__main__":
    #pluginsystem()
    window.mainloop()

