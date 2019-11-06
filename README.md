# Wheel volume

```
work in progress
```

Python script which allows to control volume by holding mouse right button and scrolling mouse wheel.

## Installation

**Linux Mint 19.1**

Basic

* clone repository
* create python virtual env
* install requirements

System startup

* open `Startup Applications`
* click `+` and add new `Custom command`
  * name: `wheel-volume`
  * command: `nohup /home/hansek/.envs/wheel-volume/bin/python /home/hansek/projects/wheel-volume/wheel-volume.py &`

