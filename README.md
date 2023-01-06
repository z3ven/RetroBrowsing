# RetroBrowsing
The Browser for old computers with own web engine, themes and plugins. The GUI based on tkinter.
# A new update! 
# Installation
Download Python from https://python.org, after install a pywebview library

```
pip install pywebview
```

or

```
pip3 install pywebview
```
Install git

After clone the project files via:
```
git clone https://github.com/z3ven/RetroBrowsing
```
### Issue
If you use windows or another platform go to the 'config.py' and set 
```python
WEB_ENGINE = set_here_you_needed_web_engine_from_the_following_table"
```
| Platform | Web engine parameter|
| --- | --- |
| GTK | gtk |
| macOS | - |
| QT | qt |
| Windows | edgechromium |
| Windows  | edgehtml |
| Windows | mshtml |
| Windows | cef |

More about the web engine you can know at https://pywebview.flowrl.com/guide/renderer.html
# Usage
### Web sites
To open website write its name and click 'Go'
### File opening support
To open files use:
```
file:filepath
```
and click go.
### Commands
You can use the commands in entry. Every command starts with 'RetroBrowser/command_name'. There are list of them:
- ```about``` - shows the about window. You can see about window when you click 'About' in main window.
* ```guidebook``` - shows guidebook of the browser where you can find the tips of using the browser.
+ ```config``` - shows configuration file.


# Advanced
## Language
To change language go to configuration.py and edit this varible
```python
LOCALIZATION = language_name_from_folder_localization
```
The languzge that you set must be at format ru_ru and you need to have downloaded files of localization.
## Themes
Themes are not supported at version 1.0 but after will.
## Plugins
Plugins are beta-features. To power on, you need to uncoment the function from 178-184. And uncomment calling it at row 186. Later you can download the plugins in .py format and after paste them to the ```/plugins/``` folder.
### Writing your own plugins
To write your own plugins you can use any library or code. Of course they needed to be insalled. Here is an example of the plugin that opens the window and calling from the main window
```python
from tkinter import *
from .. import browser
def myextraplugin():
    newWindow = Toplevel(browserwindow)
    newWindow.title("RetroBrowsing 1.0")
    name = Label(newWindow, text="Example of the plugin.")
    name.pack()
    newWindow.mainloop()

my_mega_button = Button(text='Plugin button', command=myextraplugin)
```
# Licence
Anyone can copy this project, but if you clone my project with my code, you need to mention me. 
