# staffLocationWEB
Project allows to show location of each user on your remote server.

## Docker startup

### Requirements

- [Docker](https://docs.docker.com/install/)
- [docker-compose](https://docs.docker.com/compose/install/)

### How to start
1. Get project:
```console
$ git clone --recursive https://github.com/mperov/staffLocationWEB.git
$ cd staffLocationWEB/
```
2. 1) change full path to your .ssh folder in docker-compose.yml (/home/coder/.ssh is example path);
   2) Input IP address of your remote machine also change username and modify ssh port if it isn't 22 in call `getLocation.show()` that is at staffLocation.py source file;  
   3) Follow [4-7 README points of submodule project](https://github.com/mperov/getLinuxUserLocation/blob/main/README.md).  
3. Build and run container:
```console
$ docker-compose build
$ docker-compose up -d
```
**If it's all right site http://localhost:8080 will be available.**

## Typical startup

### How to start
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

4. Install submodule Python requirements - `pip3 install -r getLinuxUserLocation/requirements` or `python3 -m pip install -r getLinuxUserLocation/requirements`
5. Follow [4-7 README points of submodule project](https://github.com/mperov/getLinuxUserLocation/blob/main/README.md)
6. Input IP address of your remote machine also change username and modify ssh port if it isn't 22 in call `getLocation.show()` that is at staffLocation.py source file.

### Usage
1. Run project
```console
$ source staffLocationWEB/bin/activate
$ ./staffLocation.py
```
2. Open your favorite browser and go to http://localhost:8080
