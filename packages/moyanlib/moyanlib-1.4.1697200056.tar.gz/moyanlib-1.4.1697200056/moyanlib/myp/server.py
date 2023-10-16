import socket
from moyanlib import myp

class Server:
    def __init__(self, hosts="0.0.0.0",port:int=8000):
        self.hosts = hosts
        self.routes = {}

    def route(self, path):
        def decorator(func):
            self.routes[path] = func
            return func
        return decorator
    def _loadClientData(text:str):
        t1 = text.split("\n")
        path = t1[0]
        t2 = t1[1].split("[")
        t2 = t2[1].split("]")
        headers = t2.split("\n")
        headers = [i.split(":") for i in headers]
        data = {
            "path":path,
            "headers":headers
        }

    def _handle_request(self, content:bytes,addr):
        data = self._loadClientData(content.decode())

        if data["path"] in self.routes:
            pass
        else:
            # 处理路径不存在的情况
            return myp.Response(code=2)

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.hosts, self.port))
            s.listen()
            while True:
                conn, addr = s.accept()
                ret = conn.recv(4096)
                request = myp.Request(ret,addr)
                response = self._handle_request(request)
                conn.send(response)
                conn.close()