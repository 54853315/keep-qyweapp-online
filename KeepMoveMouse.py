#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @author : konakona<konakona@crazyphper.com>
 
import time
import datetime
import pyautogui

limit = 10
whileMin = input("主子，您计划摸鱼多久？（可以输入 1 代表1个小时，0.5 代表半个小时)；直接回车就有半小时哦～") or '0.5'
whileMin = float(whileMin)
offset = datetime.timedelta(hours=whileMin)
beginTime = datetime.datetime.now()
leaveTime = (beginTime + offset)
print('当前系统的时间是 :', beginTime)
print('你计划摸鱼到     :',leaveTime.strftime('%Y-%m-%d %H:%M:%S'))
while 1:
    currentTime = datetime.datetime.now()
    if leaveTime < currentTime:
        print("脚本已经完成了它的使命！期待您下一次的摸鱼！WLB")
        exit()
    pyautogui.moveTo(360, 450, 1) 
    pyautogui.moveTo(1100, 450, 1)
