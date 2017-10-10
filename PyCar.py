# -*- coding: utf-8 -*-
#Henry Liu
#2017-10-10 with Louis
#Long Gang Home

import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD) #GPIO 调用BOARD编号方式

print '正在设置GPIO 端口......'
gpio.setup(7,gpio.OUT)
gpio.setup(11,gpio.OUT)
gpio.setup(13,gpio.OUT)
gpio.setup(15,gpio.OUT)

print '小车开始启动了......'
gpio.output(7,True) #左侧轮子前进
gpio.output(11,False)

gpio.output(13,False) #右侧轮子前进
gpio.output(15,True)

time.sleep(200)
gpio.cleanup()
print '小车停止了......'
