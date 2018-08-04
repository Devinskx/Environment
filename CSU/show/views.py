from django.shortcuts import render
from show import models
from django.http import HttpResponse
import datetime
import json

# Create your views here.
# test
def test(request):
    # led = models.Led.objects.get(led_id=1)
    # door = models.Door.objects.get(door_id=1)
    # blower = models.Blower.objects.get(blow_id=1)
    # environment = models.Environment.objects.get(e_id=1)
    # # print(led)
    # dict = {'led': led, 'door': door, 'blower': blower, 'environment': environment}
    # return render(request,'show/ledinfo.html',{'dict':dict})
    print(datetime.datetime.now().time().hour)
    print(datetime.datetime.now().minute)
    return HttpResponse(status=200,content='ok')



# 首页的数据信息
def indexshow(request):
    led = models.Led.objects.get(led_id=1)
    door = models.Door.objects.get(door_id=1)
    blower = models.Blower.objects.get(blow_id=1)
    environment = models.Environment.objects.get(e_id=1)
    #判断是否超过阈值
    threshold = models.Threshold.objects.get(t_id=1)
    if environment.e_co2 >= threshold.t_co2:
        co2status = 1
    else:
        co2status =0
    if environment.e_pm >=threshold.t_pm:
        pmstatus = 1
    else:
        pmstatus =0
    if environment.e_temperature >= threshold.t_temperature:
        temstatus = 1
    else:
        temstatus =0
    if environment.e_humidity >= threshold.t_humidity:
        humiditystatus = 1
    else:
        humiditystatus =0
    # print(led)
    dict = {'led':led, 'door':door, 'blower':blower, 'environment':environment}

    # 今日的图表数据
    time = datetime.datetime.now().strftime('%Y,%m,%d')
    time = time.split(',')
    year = int(time[0])
    month = int(time[1])
    day = int(time[2])
    enhistorys = models.Enhistory.objects.filter(currenttime__contains=datetime.date(year, month, day))
    return render(request,'show/test.html',{'dict':dict, 'table':enhistorys})

# LED数据展示
def ledinfo(request):
    leds = models.Led.objects.all()
    return render(request,'show/test.html',{'leds':leds})

#所需图表的环境段时间数据
def table(request):
    date = []
    for i in range(1,4):
        time = (datetime.datetime.now() - datetime.timedelta(days=i)).strftime('%Y,%m,%d')
        time = time.split(',')
        year = int(time[0])
        month = int(time[1])
        day = int(time[2])
        enhistorys = models.Enhistory.objects.filter(currenttime__contains=datetime.date(year, month, day))
        temperature = []
        humidity = []
        co2 = []
        pm = []
        for i in enhistorys:
            temperature.append(i.h_temperature)
            humidity.append(i.h_humidity)
            co2.append(i.h_co2)
            pm.append(i.h_pm)
        dirt={'temperature':temperature,'humidity':humidity,'co2':co2,'pm':pm}
        date.append(dirt)
    date.reverse()
    return render(request,'show/test.html',{'date':date})



