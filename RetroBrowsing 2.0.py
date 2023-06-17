import os
import sys
import webview
import config
from flask import Flask, render_template, request, redirect
import urllib.request




guifile = "../static/default.css"
if config.THEME != "DEFAULT":
    guifile = f"../static/{config.THEME}"

if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    server = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
else:
     server = Flask(__name__)



@server.route("/gui/")
def gui(lang):
    if config.LOCALIZATION == "en_us":
        return render_template("gui.html", themefile=guifile)
    elif config.LOCALIZATION == "ru_ru":
        return render_template("gui_ru.html", themefile=guifile)
@server.route('/gui/', methods=['POST'])
def guiurl(lang):
    requestuserurl = request.form['text']
    userurl = str(requestuserurl)
    if 'file://' in userurl:
        path = userurl.split("file://")[1]
        return render_template("openfile.html", file=path)
    else:
        return redirect(f"http://{userurl}")
@server.route("/update/")
def update(lang):
    if config.LOCALIZATION == "en_us":
        return render_template("update-en.html")
    elif config.LOCALIZATION == "ru_ru":
        return render_template("update-ru.html")
@server.route("/about/")
def about(lang):
    if config.LOCALIZATION == "en_us":
        return render_template("about-en.html", language=config.LOCALIZATION, build=config.VERSION, theme=config.THEME, retroengine="RetroEngine 2.0, GUI=HTML, CURRENTSTATE=RENDERING", themefile=guifile)
    elif config.LOCALIZATION == "ru_ru":
        return render_template("about-ru.html", language=config.LOCALIZATION, build=config.VERSION, theme=config.THEME, retroengine="RetroEngine 2.0, GUI=HTML, CURRENTSTATE=RENDERING", themefile=guifile)


@server.route("/downloadsupport/")
def downloadsupport():
    return render_template("downloader.html", themefile=guifile)
@server.route("/downloadfile/", methods=["POST"])
def download():
    requestuserurl = request.form['text']
    userurl = str(requestuserurl)
    urllib.request.urlretrieve(userurl)
    return render_template("ok.html")




def serverrun():
    server.run(host="0.0.0.0", port=2386)
retrobrowsing = webview.create_window(title="RetroBrowsing 2.0", url=f"http://127.0.0.1:2386/gui/", min_size=(800, 600))
webview.start(serverrun)

