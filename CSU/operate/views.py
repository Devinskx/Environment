from django.http import HttpResponse
from operate import models
import json
import socket
import datetime
# Create your views here.

tcp_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_addr = ('127.0.0.1',10001)
tcp_client.connect(server_addr)
# 连接成功后，发送自己的标识信息，表明自己的数据方向是下行
tcp_client.send((json.dumps({'first_dir':'DOWN'})+" END").encode())


def test1(request):
    send={}
    send["boardid"]='01'
    send["devid"]='01'
    send["dataLen"]='01'
    send["data"]='2a'
    tcp_client.send((json.dumps(send)+"END").encode())
    return HttpResponse(200,'ok')


# # 网关通信（接收和发送）
# def recv_sockdata(the_socket):
#     total_data = ""
#     while True:
#         data = the_socket.recv(1024).decode()
#         if "END" in data:
#             total_data += data[:data.index("END")]
#             break
#         total_data += data
#     return total_data
# server_addr = ('0.0.0.0', 10002)
#
# # 线程类，处理和网关的交互
# class MyThread(threading.Thread,object):
#     def __init__(self,sock,addr):
#         threading.Thread.__init__(self)
#         self.sock = sock
#         self.addr = addr
#     def run(self):
#         print('Accept new connection from {}...'.format(self.addr))
#         self.recv_data()
#         print('Connection from {} closed.'.format(self.addr))
#     def recv_data(self):
#         while True:
#             res_data = recv_sockdata(self.sock)
#             try:
#                 data = json.loads(res_data,encoding="utf-8")
#
#             # 这里完成对数据的写入操作
#             # 解析网关的Json数据
#                 func_id = data['boardid']  # 功能板id
#                 sensor_id = data['devid']  # 传感器id
#                 value = data['data']  # 数据值（16进制的字符串形式）
#
#             # 取出数据表中的当前实时数据记录（每个实时记录表只有一条数据）
#             # 如果为空则创建新纪录
#                 try:
#                     led = models.Led.objects.get(led_id=1)
#                     led.currenttime=datetime.datetime.now()
#                     led.update_time = datetime.datetime.now()
#                 except models.Led.DoesNotExist:
#                     led = models.Led()
#                     led.led_id = 1
#                 try:
#                     blower = models.Blower.objects.get(blow_id=1)
#                     blower.currenttime = datetime.datetime.now()
#                     blower.update_time = datetime.datetime.now()
#                 except models.Blower.DoesNotExist:
#                     blower = models.Blower()
#                     blower.blow_id = 1
#                 try:
#                     door = models.Door.objects.get(door_id=1)
#                     door.currenttime = datetime.datetime.now()
#                     door.update_time = datetime.datetime.now()
#                 except models.Door.DoesNotExist:
#                     door = models.Door()
#                     door.door_id = 1
#                 try:
#                     environment = models.Environment.objects.get(e_id=1)
#                     environment.currenttime = datetime.datetime.now()
#                 except models.Environment.DoesNotExist:
#                     environment = models.Environment()
#                     environment.e_id = 1
#                 enhistory = models.Enhistory()
#                 # 分析数据
#                 if func_id == '01':
#                     if sensor_id == '01':  # led
#                         led_value = int(value,16)
#                         led.led_status = led_value
#                         led.save()
#                     elif sensor_id == '02':  # infrared
#                         infrared_value = int(value,16)
#                         environment.e_infrared = infrared_value
#                 elif func_id == '02':
#                     if sensor_id == '01':  # co2
#                         co2_value = int(value,16)
#                         environment.e_co2 = co2_value
#                         if datetime.datetime.now().hour%4==0 and datetime.datetime.now().minute==0:
#                             enhistory.h_co2 = co2_value
#                     elif sensor_id == '02':  # temperature
#                         tem_value = int(value,16)
#                         environment.e_temperature = tem_value
#                         if datetime.datetime.now().hour%4==0 and datetime.datetime.now().minute==0:
#                             enhistory.h_temperature = tem_value
#                 elif func_id == '03':
#                     if sensor_id == '01':  # ch4
#                         ch4_value = int(value,16)
#                         environment.e_ch4 = ch4_value
#                     elif sensor_id == '02':  # smoke
#                         smoke_value = int(value,16)
#                         environment.e_smoke = smoke_value
#                     elif sensor_id == '03':  # fire
#                         fire_value = int(value,16)
#                         environment.e_fire = fire_value
#                 elif func_id == '04':  # PM2.5
#                     if sensor_id == '01':
#                         pm_value = int(value,16)
#                         environment.e_pm = pm_value
#                         if datetime.datetime.now().hour%4==0 and datetime.datetime.now().minute==0:
#                             enhistory.h_pm = pm_value
#                     elif sensor_id == '02':
#                         humidity_value = int(value,16)
#                         environment.e_humidity = humidity_value
#                         if datetime.datetime.now().hour%4==0 and datetime.datetime.now().minute==0:
#                             enhistory.h_humidity = humidity_value
#                 elif func_id == '07':  # blower
#                     if sensor_id == '01':
#                         blower_value = int(value,16)
#                         blower.blow_status = blower_value
#                         blower.save()
#                 elif func_id == '08':  # door
#                     if sensor_id == '01':
#                         door_value = int(value,16)
#                         door.door_status = door_value
#                         door.save()
#                         print(door.currenttime)
#                 # （环境表）数据存表
#                 environment.save()
#                 enhistory.save()
#             except json.decoder.JSONDecodeError as e:
#                 print("error data:" + res_data)
#                 continue
#
#             print(data)  # 收到的数据
#
#
# # 创建socket
# tcpSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#
# # 绑定地址
# tcpSocket.bind(server_addr)
#
# # 监听端口
# tcpSocket.listen(15)
#
# threads = []
# print("Waiting for connection")
#
# # 服务器程序通过一个永久循环来接收来自客户端的连接
# def do_service():
#     while True:
#         # 接收一个新的连接
#         sock,addr = tcpSocket.accept()
#
#         # 创建线程来处理TCP连接，每个连接都必须创建新线程来处理
#         # 否j
#         # 则，单线程处理连接过程中无法接收其他客户端的连接
#         mthread = MyThread(sock,addr)
#         mthread.start()
#         threads.append(mthread)
#
# # 将会发生阻塞的接收新连接的逻辑放在线程中
# threading.Thread(target=do_service).start()

#操作LED
def ledoperate(request):
    # ledid = request.POST('led_id')
    # ledstatus = request.POST('led_status')

    # 向网关通信，发送数据
    send_data = {}
    # send_data['func_id'] = '01'
    # send_data['sensor_id'] = '01'
    # send_data['flag'] = str(ledid)
    # send_data['value'] = str(ledstatus)
    send_data['boardid'] = '07'
    send_data['devid'] = '01'
    send_data['dataLen'] = '01'
    send_data['data'] = '01'
    for thread in threads:
        print('send msg!')
        thread.sock.send((json.dumps(send_data)).encode())

    # 创建新的led记录存表
    # led = models.Led()
    # led.led_id = ledid
    # led.led_status = ledstatus
    # led.save()
    return HttpResponse(status=200)

#操作door
def dooroperate(request):

    # request中取数据

    doorid = request.POST('door_id')
    doorstatus = request.POST('door_status')

    # 向树莓派通信，发送数据
    send_data = {}
    send_data['func_id'] = '08'
    send_data['sensor_id'] = '01'
    send_data['value'] = str(doorstatus)
    for thread in threads:
        print('send msg!')
        thread.sock.send((json.dumps(send_data)+"END").encode())

    # 创建door新纪录存表
    door = models.Door()
    door.door_id = doorid
    door.door_status = doorstatus
    door.save()
    return HttpResponse(status=200,content='OK')

#操作blower
def bloweroperate(request):

    # request中获取数据
    blowerid = request.POST('blow_id')
    blowerstatus = request.POST('blow_status')

    # 向树莓派通信，发送数据
    send_data = {}
    send_data['func_id'] = '07'
    send_data['sensor_id'] = '01'
    send_data['value'] = str(blowerstatus)
    for thread in threads:
        print('send msg!')
        thread.sock.send((json.dumps(send_data) + "END").encode())

    # 创建新blower记录存表
    blower = models.Blower()
    blower.blow_id = blowerid
    blower.blow_status = blowerstatus
    blower.save()

    return HttpResponse(200,'ok')