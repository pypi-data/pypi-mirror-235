class Request:
    def __init__(self, path, headers, body):
        self.path = path
        self.headers = headers
        self.body = body

def Response(headers:list[dict]=[],data:bytes=b"ERROR",code:int=1):
    strHead = ""
    for header in headers:
        strHead += header["name"] + ":" + header["value"] + "\n"
    if strHead == "":
        strHead = "None"
    retH= f"code:{str(code)}[haeders={strHead}]".encode("utf-8")
    retdata:bytes = retH+data
    return retdata
