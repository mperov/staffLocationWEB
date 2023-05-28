# staffLocationWEB
Project allows to show location of each user on your remote server.

## How to start
1. Get project:
```console
$ git clone --recursive https://github.com/mperov/staffLocationWEB.git
$ cd staffLocationWEB/
```
2. Create special Python virtual enviroment by
```console
$ sudo apt-get install python3-venv -y
$ python3 -m venv staffLocationWEB
$ source staffLocationWEB/bin/activate
```
3. Next install some Python modules - `pip3 install -r requirements` or `python3 -m pip install -r requirements`  
If you don't have pip3 then you may install it [how described here](https://pip.pypa.io/en/stable/installation/)

## Usage
1. Run project
```console
$ source staffLocationWEB/bin/activate
$ ./staffLocation.py
```
2. Open your favorite browser and go to http://localhost:8080
