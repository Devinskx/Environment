# -*- coding:utf-8 -*-
__author__ = 'Threedog'
__Date__ = '2018/7/20 15:23'
# python版本中转服务器代码，在服务器端运行

import socket
import threading
import json
import pymysql # 导入pymysql包
import datetime
db = pymysql.connect(host="127.0.0.1", user="root", database="csu", password="SSWssw1314")  # 打开数据库，配置数据库
cursor = db.cursor()  # 数据库操作
# 监听端口
server_addr = ('0.0.0.0',10001)

def recv_sockdata(the_socket):
    total_data = ""
    while True:
        data = the_socket.recv(1024).decode()
        # data = the_socket.recv(1024).decode('unicode-escape')
        if "END" in data:
            total_data += data # [:data.index("END")]
            break
        total_data += data
    # print("-----------------")
    return total_data


class MyThread(threading.Thread,object):

    def __init__(self,sock,addr):
        threading.Thread.__init__(self)
        self.sock = sock
        self.addr = addr
        self.direction = 21840

    def run(self):
        print('Accept new connection from {}...'.format(self.addr))
        try:
            self.recv_data()
        except (ConnectionResetError,ConnectionAbortedError):
            print('Connection from {} closed.'.format(self.addr))
            self.sock.close()
            threads.remove(self)

    def recv_data(self):
        while True:
            res_data = recv_sockdata(self.sock)
            try:
                print(res_data)
                data_dict = json.loads(res_data[:-3])  # 去掉结尾的END
                if 'first_dir' in res_data:
                    self.direction = data_dict.get('first_dir')
                    continue

                # 就比如如果当前数据方向是UP，说明是网关发上来的数据，那么就转化后插入数据库
                if self.direction == 21840:
                    print('111')
                    func_id = data_dict.get('boardid')
                    sensor_id = data_dict.get('devid')
                    value = data_dict.get('data')
                    # cmd = "insert into ec_test.ec_data(data_type,data_value,data_time) values('Tem',{},now());".format(data)
                    # cursor.execute(cmd)  # 执行cmd命令
                    # db.commit()
                    # cmd = "UPDATE door SET door_status={},currenttime = sysdate() WHERE door_id = 1 ".format(int(data,16))
                    # cursor.execute(cmd)
                    # db.commit()

                    if func_id == 1:
                        if sensor_id == 1:  # led
                            cmd = "UPDATE led SET led_status={},currenttime = sysdate() WHERE led_id = 1 ".format(value)
                            cursor.execute(cmd)
                            db.commit()
                        elif sensor_id == 2:  # infrared
                            cmd = "UPDATE environment SET e_infrared={},currenttime = sysdate() WHERE e_id = 1 ".format(value)
                            cursor.execute(cmd)
                            db.commit()
                            # infrared_value = int(value,16)
                            # environment.e_infrared = infrared_value
                    elif func_id == 2:
                        if sensor_id == 1:  # co2
                            cmd = "UPDATE environment SET e_co2={},currenttime = sysdate() WHERE e_id = 1 ".format(
                                value)
                            cursor.execute(cmd)
                            db.commit()
                            # co2_value = int(value,16)
                            # environment.e_co2 = co2_value
                            if datetime.datetime.now().hour%4==0 and datetime.datetime.now().minute==0:
                                cmd = "UPDATE enhistory SET h_co2={},currenttime = sysdate() WHERE h_id = 1 ".format(
                                    value)
                                cursor.execute(cmd)
                                db.commit()
                                # enhistory.h_co2 = co2_value
                        elif sensor_id == 2:  # temperature
                            cmd = "UPDATE environment SET e_temperature={},currenttime = sysdate() WHERE e_id = 1 ".format(
                                value/100)
                            cursor.execute(cmd)
                            db.commit()
                            # tem_value = int(value,16)
                            # environment.e_temperature = tem_value
                            if datetime.datetime.now().hour%4==0 and datetime.datetime.now().minute==0:
                                cmd = "UPDATE enhistory SET h_temperature={},currenttime = sysdate() WHERE h_id = 1 ".format(
                                    value)
                                cursor.execute(cmd)
                                db.commit()
                                # enhistory.h_temperature = tem_value
                    elif func_id == 3:
                        if sensor_id == 1:  # ch4
                            cmd = "UPDATE environment SET e_ch4={},currenttime = sysdate() WHERE e_id = 1 ".format(
                                value)
                            cursor.execute(cmd)
                            db.commit()
                            # ch4_value = int(value,16)
                            # environment.e_ch4 = ch4_value
                        elif sensor_id == 2:  # smoke
                            cmd = "UPDATE environment SET e_smoke={},currenttime = sysdate() WHERE e_id = 1 ".format(
                                value)
                            cursor.execute(cmd)
                            db.commit()
                            # smoke_value = int(value,16)
                            # environment.e_smoke = smoke_value
                        elif sensor_id == 3:  # fire
                            cmd = "UPDATE environment SET e_fire={},currenttime = sysdate() WHERE e_id = 1 ".format(
                                value)
                            cursor.execute(cmd)
                            db.commit()
                            # fire_value = int(value,16)
                            # environment.e_fire = fire_value
                    elif func_id == 4:  # PM2.5
                        if sensor_id == 1:
                            cmd = "UPDATE environment SET e_pm={},currenttime = sysdate() WHERE e_id = 1 ".format(
                                value)
                            cursor.execute(cmd)
                            db.commit()
                            # pm_value = int(value,16)
                            # environment.e_pm = pm_value
                            if datetime.datetime.now().hour%4 ==0 and datetime.datetime.now().minute==0:
                                cmd = "UPDATE enhistory SET h_pm={},currenttime = sysdate() WHERE h_id = 1 ".format(
                                    value)
                                cursor.execute(cmd)
                                db.commit()
                                # enhistory.h_pm = pm_value
                        elif sensor_id == 2:
                            cmd = "UPDATE environment SET e_humidity={},currenttime = sysdate() WHERE e_id = 1 ".format(
                                value/100)
                            cursor.execute(cmd)
                            db.commit()
                            # humidity_value = int(value,16)
                            # environment.e_humidity = humidity_value
                            if datetime.datetime.now().hour%4==0 and datetime.datetime.now().minute==0:
                                cmd = "UPDATE enhistory SET h_humidity={},currenttime = sysdate() WHERE h_id = 1 ".format(
                                    value)
                                cursor.execute(cmd)
                                db.commit()
                                # enhistory.h_humidity = humidity_value
                    elif func_id == 7:  # blower
                        if sensor_id == 1:
                            cmd = "UPDATE blower SET blow_status={},currenttime = sysdate() WHERE blow_id = 1 ".format(
                                value)
                            cursor.execute(cmd)
                            db.commit()
                            # blower_value = int(value,16)
                            # blower.blow_status = blower_value
                            # blower.save()
                    elif func_id == 8:  # door
                        if sensor_id == 1:
                            cmd = "UPDATE door SET door_status={},currenttime = sysdate() WHERE door_id = 1 ".format(
                                value)
                            cursor.execute(cmd)
                            db.commit()
                            # door_value = int(value,16)
                            # door.door_status = door_value
                            # door.save()
                            # print(door.currenttime)



                elif self.direction == "DOWN":
                    # 如果当前数据方向是DOWN 要找出所有的网络方向是UP的线程（网关线程），将数据发送给网关。
                    for thread in threads:
                        if thread.direction == 21840:
                            print('000')
                            thread.sock.send(res_data.encode())

                # data = json.loads(res_data,encoding="utf-8")
                # print(data)# 收到的数据
                # 一下模拟收到网关数据后进行的操作
                # 我们假设收到的数据是温度数据，将温度数据存入数据库

            except json.decoder.JSONDecodeError as e:
                print("error data:"+res_data)
                continue

#创建Socket
tcpSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定地址
tcpSocket.bind(server_addr)
#监听端口，传入的参数指定等待连接的最大数量
tcpSocket.listen(16)
threads = []
print('Waiting for connection...')
#服务器程序通过一个永久循环来接受来自客户端的连接
def do_service():
    while True:
        # 接受一个新连接:
        sock,addr = tcpSocket.accept()
        # 创建新线程来处理TCP连接:每个连接都必须创建新线程（或进程）来处理，
        # 否则，单线程在处理连接的过程中，无法接受其他客户端的连接：
        mthread = MyThread(sock,addr)
        mthread.start()
        threads.append(mthread)

threading.Thread(target=do_service).start()



