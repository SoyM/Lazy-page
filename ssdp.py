# -*- coding: UTF-8 -*-
import socket
import select

HOST = '192.168.191.2'
PORT = 1982
SSDP_ADDR = '239.255.255.250'
SSDP_PORT = 1982
data = "M-SEARCH * HTTP/1.1\r\n" + \
       "HOST:239.255.255.250:1982\r\n" + \
       "MAN:\"ssdp:discover\"\r\n" + \
       "ST: wifi_bulb"

address = (HOST, PORT)
device_id = '0x0000000003b0d926'


class SSDPClient:
    def __init__(self):
        self.__s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # # INFO: 若绑定，服务端收到的是固定的地址和端口号
        self.__s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # local_ip = socket.gethostbyname(socket.gethostname())
        local_ip = '192.168.191.1'
        self.__s.bind((local_ip, 50000))

    def start(self):
        self.__send_search()
        while True:
            reads, _, _ = select.select([self.__s], [], [], 5)
            if [reads]:
                data, addr = self.__s.recvfrom(1024)
                conn = Connection(self.__s, data, addr)
                conn.handle_request()
                if conn.is_find_service:
                    break
            else:  # timeout
                self.__send_search()
        self.__s.close()

    def wait_notify(self):
        while True:
            print(1)
            data, addr = self.__s.recvfrom(1024)
            print(data)
            conn = Connection(self.__s, data, addr)
            conn.handle_request()

    def __send_search(self):
        print("Sending search...")
        # INFO: 发送到SSDP组播地址上
        self.__s.sendto(bytes(data, "utf-8"), address)


class Connection:
    def __init__(self, s, data, addr):
        self.__s = s
        self.__data = data
        self.__addr = addr
        self.is_find_service = False

    def handle_request(self):
        if self.__data.startswith(bytes('M-SEARCH * HTTP/1.1\r\n', 'utf-8')):
            self.__handle_search()
        elif self.__data.startswith(bytes('HTTP/1.1 200 OK\r\n', "utf-8")):
            self.__handle_ok()
        elif self.__data.startswith(bytes('NOTIFY * HTTP/1.1\r\n', "utf-8")):
            self.__handle_notify()

    def __handle_search(self):
        props = self.__parse_props()
        if not set([b'HOST', b'MAN', b'ST', b'MX']).issubset(set(props.keys())):
            return
        if not props:
            return
        if props['HOST'] != '%s:%d' % (SSDP_ADDR, SSDP_PORT) \
                or props['MAN'] != '"ssdp:discover"' \
                or props['ST'] != 'ssdp:all':
            return
        print('RECV: %s' % str(self.__data))
        print('ADDR: %s' % str(self.__addr))

        response = 'HTTP/1.1 200 OK\r\nST: \r\n\r\n'
        self.__s.sendto(response, self.__addr)

    def __handle_ok(self):
        print("handle_ok")
        props = self.__parse_props()
        if not props:
            return
        if props[b'id'] != bytes(device_id, "utf-8"):
            return
        print('RECV: %s' % str(self.__data))
        print('ADDR: %s' % str(self.__addr))
        print('Find service!!!!')
        self.is_find_service = True
        tcpConnnection = tcpConn()
        tcpConnnection.connect()

    def __handle_notify(self):
        print("hadle notify")
        props = self.__parse_props()
        if not props:
            return
        if props[b'id'] != bytes(device_id, "utf-8"):
            return

    def __parse_props(self):
        lines = self.__data.split(bytes('\r\n', "utf-8"))
        props = {}
        for i in range(1, len(lines)):
            if not lines[i]:
                continue
            index = lines[i].find(b':')
            if index == -1:
                return None
            props[lines[i][:index]] = lines[i][index + 1:].strip()
        print(props)
        return props


class tcpConn:
    def __init__(self):
        self.__s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.__s.connect((HOST, 49154))
        print(self.__s.recv(1024))
        self.__s.send('{"id":1,"method":"set_power","params":["on", "smooth", 500]}')
        print(self.__s.recv(1024))


if __name__ == '__main__':
    port = SSDPClient()
    port.start()
