# Argo
Multi camera gathering and exploiting tool


[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) ![python](https://img.shields.io/badge/python-3.7-green.svg)
![Alt_text](https://github.com/M0tHs3C/Argo/blob/master/fotoArgo/Annotazione%202019-09-25%20185154.png?raw=true "Title")
## Installation
```bash
$ git clone https://github.com/M0tHs3C/Argo.git
$ cd Argo
$ pip3 install -r requirements.txt
$ python3 argo.py
```
## Introduction
Argo is a multi camera gathering and exploiting tool.
Argo will automatically search on the internet using censys or shodan key.
There are loaded some specific queries for vulnerable device usable on shodan or censys.
In order to make it work you will need to provide the key for shodan and censys, you can either enter them when you will be asked or you can modify manually the API files.
You will find them in the API folder; the api.txt file is for shodan, just paste the key in the first line and stop.
The censys_api.txt will be in the same folder, just paste the two key in two separate lines, one on top of the other one
## Usage
Argo is pretty basic, i've reduced the user interactions to the minimum necessary
It's pretty straightforward
The tool have 4 phases (non-mandatory)
* 1 ) Host gathering<br/>
    you will have to gather some host either from shodan or censys
* 2 ) Up testing<br/>
    test if all the host are really up
* 3 ) vuln testing<br/>
    some device will have to be tested for vulnerability, the query is right but there might be false positive
* 4 ) exploit<br/>
   in the fifth section you will find the exploit menu, a list of different exploit for different camera model
   logically the exploit for the "A" camera will not work if you gather host of "B" camera
   if is aveilable in the exploit section u will find a bruteforce tool for that camera too
## Cameras
Today the tool supports only
```bash
Hikvision camera
Viola dvr camera
AVTECH camera
Bticino server
RSP device
Geovision camera
goAhead camera
atlantis camera
ANPR camera
```
## Compability
The tool is tested to work on windows and linux



_legal disclaimer: Usage of Argo for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

