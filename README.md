# RetroBrowsing
The Browser for old computers with own web engine, themes and plugins.
# A new update!
Meet RetroBrowsing 2.0!
New version, new functions!
New update 2.0 containts this changes:
* Design based on html
* RetroEngine 2.0
* Easy config changing
* Themes
* Fast-Redirect
* Allows build
* Downloads support(works only on macOS and Linux) via RetroEngine 2.0

# Installation
If you don't have python, install it from [here](https://python.org)
Install git

After clone the project files via:
```
git clone https://github.com/z3ven/RetroBrowsing
```

## Build 
Run build.sh on macOS or Linux or build.bat if you are on windows.
```
cd RetroBrowsing
./build.sh
```
On Windows
```
cd RetroBrowsing
build
```


SET ALL THE SETTINGS IN CONFIG. AFTER YOU WILL NOT ABLE TO CHANGE THEM. Wait until it will build. In ```dist``` folder you will find the files that you will need.
## Requierements
To install requirements you can just write this:
```
pip3 install -r requirements.txt
```

## Issue
If you use windows or linux go to the 'config.py' and set 
```python
WEB_ENGINE = set_here_you_needed_web_engine_from_the_following_table"
```
| Platform | Web engine parameter|
| --- | --- |
| GTK | gtk |
| macOS | DEFAULT |
| QT | qt |
| Windows | edgechromium |
| Windows  | edgehtml |
| Windows | mshtml |
| Windows | cef |

More about the web engine you can know [here](https://pywebview.flowrl.com/guide/renderer.html)
# Usage
### Web sites
To open website write its name and click 'Submit'
### File opening support
To open files use:
```
file://filepath
```
and click submit.

# Advanced
## Language
To change language go to configuration.py and edit this varible
```python
LOCALIZATION = language_name
```
The languzge that you set must be at format ru_ru and you need to have downloaded HTML files.
## Themes
* Download any ```.css``` file
* Drop it to ```/static/``` folder in main RetroBrowsing folder
* Open ```config.py```
* Set this
```python
THEME = "../static/your_theme_name.css"
```
## Plugins
Plugins are removed. We didnt sure that the Plugins work fine.

# Licence
Anyone can copy this project, but if you clone my project with my code, you need to mention me. 
