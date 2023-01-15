"""
                Project Titanium 1.0
"""
import os
import sys
import importlib
import urllib.request


REPO = "titaniumRepo"

if "download" in sys.argv[1]:
    appmetada = str(sys.argv[2]).replace(".py", "")
    try:
        app = importlib.import_module(f"{REPO}.{appmetada}")
        print(f"Downloading {app.APPNAME} \n")
        savepath = os.path.join("appcache", f"{app.APPNAME}.apk")
        urllib.request.urlretrieve(app.DOWNLOAD_LINK, savepath)
        print("Downloaded! Now installing on your android device! \n")
    except ModuleNotFoundError:
        print(f"titanium: Cant find a package with name {sys.argv[2]}! ")
if "overview" in sys.argv[1]:
    appmetada = str(sys.argv[2]).replace(".py", "")
    try:
        app = importlib.import_module(f"{REPO}.{appmetada}")
        print(f"Name: {app.APPNAME}")
        print(f"Description: {app.DESCRIPTION}")
        print(f"VERSION: {app.VERSION}")
    except ModuleNotFoundError:
        print(f"titanium: Cant find a package with name {sys.argv[2]}! ")
if "update" in sys.argv[1]:
    appmetada = str(sys.argv[2]).replace(".py", "")
    try:
        app = importlib.import_module(f"{REPO}.{appmetada}")
        print(f"Downloading {app.APPNAME} \n")
        savepath = os.path.join("appcache", f"{app.APPNAME}.apk")
        os.remove(savepath)
        urllib.request.urlretrieve(app.DOWNLOAD_LINK, savepath)
        print("Downloaded! Now installing update on your android device! \n")
    except ModuleNotFoundError:
        print(f"titanium: Cant find a package with name {sys.argv[2]}! ")
