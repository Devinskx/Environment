import json
import socket

tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('127.0.0.1',10001)

tcp_client.connect(server_addr)
tcp_client.send((json.dumps({'first_dir':'UP'})+" END").encode())

send_data = {}

flag = input('input:')

if flag == 'test':
    data = [{'a': 0x01, 'b': 0x02, 'c': 0x03, 'd': 0x14, 'e': 0x2a}]
    datajson = json.dumps(data)+"END"
    tcp_client.send(datajson.encode())
if flag == 'led':
    send_data['boardid'] = '01'
    send_data['devid'] = '01'
    send_data['dataLen'] = '01'
    send_data['data'] = '1a'

    tcp_client.send((json.dumps(send_data)+"END").encode())

elif flag  == 'infrared':
    send_data['boardid'] = '01'
    send_data['devid'] = '02'
    send_data['dataLen'] = '01'
    send_data['data'] = '01'

    tcp_client.send((json.dumps(send_data) + "END").encode())

elif flag  == 'co2':
    send_data['boardid'] = '02'
    send_data['devid'] = '01'
    send_data['dataLen'] = '01'
    send_data['data'] = '2a'

    tcp_client.send((json.dumps(send_data) + "END").encode())

elif flag  == 'temperature':
    send_data['boardid'] = '02'
    send_data['devid'] = '02'
    send_data['dataLen'] = '01'
    send_data['data'] = '31'

    tcp_client.send((json.dumps(send_data) + "END").encode())

elif flag  == 'ch4':
    send_data['boardid'] = '03'
    send_data['devid'] = '01'
    send_data['dataLen'] = '01'
    send_data['data'] = '01'

    tcp_client.send((json.dumps(send_data) + "END").encode())

elif flag  == 'smoke':
    send_data['boardid'] = '03'
    send_data['devid'] = '02'
    send_data['dataLen'] = '01'
    send_data['data'] = '01'

    tcp_client.send((json.dumps(send_data) + "END").encode())

elif flag  == 'fire':
    send_data['boardid'] = '03'
    send_data['devid'] = '03'
    send_data['dataLen'] = '01'
    send_data['data'] = '01'

    tcp_client.send((json.dumps(send_data) + "END").encode())

elif flag  == 'pm':
    send_data['boardid'] = '04'
    send_data['devid'] = '01'
    send_data['dataLen'] = '01'
    send_data['data'] = '1b'

    tcp_client.send((json.dumps(send_data) + "END").encode())

elif flag  == 'humidity':
    send_data['boardid'] = '04'
    send_data['devid'] = '02'
    send_data['dataLen'] = '01'
    send_data['data'] = '2b'

    tcp_client.send((json.dumps(send_data) + "END").encode())

elif flag  == 'blower':
    send_data['boardid'] = '07'
    send_data['devid'] = '01'
    send_data['dataLen'] = '01'
    send_data['data'] = '01'

    tcp_client.send((json.dumps(send_data) + "END").encode())

elif flag  == 'door':
    send_data['boardid'] = '08'
    send_data['devid'] = '01'
    send_data['dataLen'] = '01'
    send_data['data'] = '01'

    tcp_client.send((json.dumps(send_data) + "END").encode())

# def send_data(scoket):
#     if flag == 'led':
#         send_data['boardid'] = '01'
#         send_data['devid'] = '01'
#         send_data['dataLen'] = '01'
#         send_data['data'] = '1a'
#
#         socket.send((json.dumps(send_data) + "END").encode())
#
#     elif flag == 'infrared':
#         send_data['boardid'] = '01'
#         send_data['devid'] = '02'
#         send_data['dataLen'] = '01'
#         send_data['data'] = '01'
#
#         socket.send((json.dumps(send_data) + "END").encode())
#
#     elif flag == 'co2':
#         send_data['boardid'] = '02'
#         send_data['devid'] = '01'
#         send_data['dataLen'] = '01'
#         send_data['data'] = '2a'
#
#         socket.send((json.dumps(send_data) + "END").encode())
#
#     elif flag == 'temperature':
#         send_data['boardid'] = '02'
#         send_data['devid'] = '02'
#         send_data['dataLen'] = '01'
#         send_data['data'] = '31'
#
#         socket.send((json.dumps(send_data) + "END").encode())
#
#     elif flag == 'ch4':
#         send_data['boardid'] = '03'
#         send_data['devid'] = '01'
#         send_data['dataLen'] = '01'
#         send_data['data'] = '01'
#
#         socket.send((json.dumps(send_data) + "END").encode())
#
#     elif flag == 'smoke':
#         send_data['boardid'] = '03'
#         send_data['devid'] = '02'
#         send_data['dataLen'] = '01'
#         send_data['data'] = '01'
#
#         socket.send((json.dumps(send_data) + "END").encode())
#
#     elif flag == 'fire':
#         send_data['boardid'] = '03'
#         send_data['devid'] = '03'
#         send_data['dataLen'] = '01'
#         send_data['data'] = '01'
#
#         socket.send((json.dumps(send_data) + "END").encode())
#
#     elif flag == 'pm':
#         send_data['boardid'] = '04'
#         send_data['devid'] = '01'
#         send_data['dataLen'] = '01'
#         send_data['data'] = '1b'
#
#         socket.send((json.dumps(send_data) + "END").encode())
#
#     elif flag == 'humidity':
#         send_data['boardid'] = '04'
#         send_data['devid'] = '02'
#         send_data['dataLen'] = '01'
#         send_data['data'] = '2b'
#
#         scoket.send((json.dumps(send_data) + "END").encode())
#
#     elif flag == 'blower':
#         send_data['boardid'] = '07'
#         send_data['devid'] = '01'
#         send_data['dataLen'] = '01'
#         send_data['data'] = '01'
#
#         socket.send((json.dumps(send_data) + "END").encode())
#
#     elif flag == 'door':
#         send_data['boardid'] = '08'
#         send_data['devid'] = '01'
#         send_data['dataLen'] = '01'
#         send_data['data'] = '01'
#
#         socket.send((json.dumps(send_data) + "END").encode())
#
# def rece_data(socket):
#     print('111')
#     while True:
#         total_data = ""
#         while True:
#             data = socket.recv(1024).decode()
#             # print(data)
#             if "END" in data:
#                 total_data += data[:data.index("END")]
#                 break
#             total_data += data
#         print(total_data)
#         print("-----------------")
#         try:
#             data = json.loads(total_data, encoding="utf-8")
#             func_id = data['boardid']  # 功能板id
#             sensor_id = data['devid']  # 传感器id
#             value = data['data']  # 数据值（16进制的字符串形式）
#             if func_id == '01':
#                 if sensor_id == '01':  # led
#                     led_value = int(value, 16)
#                     print('led:{}',led_value)
#                 elif sensor_id == '02':  # infrared
#                     infrared_value = int(value, 16)
#                     if infrared_value:
#                         print('有人')
#                     else:
#                         print('没人')
#             elif func_id == '02':
#                 if sensor_id == '01':  # co2
#                     co2_value = int(value, 16)
#                     print('co2:{}',co2_value)
#                 elif sensor_id == '02':  # temperature
#                     tem_value = int(value, 16)
#                     print('temperature:{}', tem_value)
#             elif func_id == '03':
#                 if sensor_id == '01':  # ch4
#                     ch4_value = int(value, 16)
#                     if ch4_value:
#                         print('液化气泄露')
#                     else:
#                         print('液化气无泄漏')
#                 elif sensor_id == '02':  # smoke
#                     smoke_value = int(value, 16)
#                     if smoke_value:
#                         print('有烟雾')
#                     else:
#                         print('无烟雾')
#                 elif sensor_id == '03':  # fire
#                     fire_value = int(value, 16)
#                     if fire_value:
#                         print('有火')
#                     else:
#                         print('无火')
#             elif func_id == '04':  # PM2.5
#                 if sensor_id == '01':
#                     pm_value = int(value, 16)
#                     print('PM2.5:{}',pm_value)
#                 elif sensor_id == '02':
#                     humidity_value = int(value, 16)
#                     print("humidity:{}",humidity_value)
#             elif func_id == '07':  # blower
#                 if sensor_id == '01':
#                     blower_value = int(value, 16)
#                     if blower_value:
#                         print('风扇开')
#                     else:
#                         print('风扇关')
#             elif func_id == '08':  # door
#                 if sensor_id == '01':
#                     door_value = int(value, 16)
#                     if door_value:
#                         print('门开')
#                     else:
#                         print('门关')
#         except json.decoder.JSONDecodeError as e:
#             print("error data:" + total_data)
#
#
#
#
#

# threading.Thread(rece_data(tcp_client)).start()


