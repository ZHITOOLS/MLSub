import base64
import json
import socket
import socketserver
import urllib.parse
import urllib.request
from http.server import HTTPServer, BaseHTTPRequestHandler

data = {'result': 'mlSub'}
host = ('0.0.0.0', 8080)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (HTML, like Gecko) '
                         'Chrome/101.0.4951.54 Safari/537.36'}
# v2ray订阅地址
subscribeUrl = ''
hostName = ''
serverName = ''
vmessCode = ''


class MyThreadingHTTPServer(socketserver.ThreadingMixIn, HTTPServer):
    pass


class Request(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        resolve(self)
        self.wfile.write(vmessCode)  # 返回内容


def resolve(self):
    global vmessCode
    subscribe_url = self.path.split("&&")[1]
    host_name = self.path.split("&&")[2]
    server_name = urllib.parse.unquote(self.path.split("&&")[3])
    print("subscribeUrl:", subscribe_url)
    print("hostName:", host_name)
    print("serverName:", server_name)
    socket.setdefaulttimeout(10)  # 请求超时设置为5s
    req = urllib.request.Request(url=subscribe_url, headers=headers)
    return_content = urllib.request.urlopen(req).read()
    print("请求到的内容为：", return_content)
    # base64 decode should meet the padding rules
    if len(return_content) % 3 == 1:
        return_content += b"="
    elif len(return_content) % 3 == 2:
        return_content += b"=="
    base64_str = base64.urlsafe_b64decode(return_content)  # 进行base64解码
    print("解码后内容：", base64_str)
    print("开始处理...\r")
    share_links = base64_str.splitlines()  # \r\n进行分行
    add = ""
    for share_link in share_links:
        share_link = bytes.decode(share_link)  # 转换类型
        if share_link.find("vmess://") == -1:
            # print("")
            # vmessCode = "抱歉，您的订阅链接不是vmess链接。"
            pass
        else:
            # print("服务器参数：", share_link)
            share = share_link.split("ss://")
            resolve_char = base64.urlsafe_b64decode(share[1]).decode('UTF-8')  # 解析VMESS参数得到json字符串 后面解析unicode
            # resolve_char = base64.urlsafe_b64decode(share[1]) # 解析VMESS参数得到json字符串 后面解析unicode
            print("vmess参数解析得到json内容：", resolve_char)
            dictionary = json.loads(resolve_char)  # 转换成字典
            if self.path.count("&&") == 4:
                for index in range(len(self.path.split("&&")[4].split('.'))):
                    if str(dictionary["port"]) == str(self.path.split("&&")[4].split('.')[index]):
                        add = add + output(dictionary, self)
            elif self.path.count("&&") == 4 and str(dictionary["port"]) == str(self.path.split("&&")[4]):
                add = add + output(dictionary, self)
            elif self.path.count("&&") == 3:
                add = add + output(dictionary, self)
            else:
                pass
    vmessCode = base64.b64encode(add.encode('UTF-8'))
    print("订阅内容：")
    print(vmessCode)


def output(subscribe_dict, self):
    hostname = self.path.split("&&")[2]
    servername = urllib.parse.unquote(self.path.split("&&")[3])
    # print("转换为字典后内容:", subscribe_dict)
    subscribe_dict["ps"] = servername + subscribe_dict["ps"]
    subscribe_dict["host"] = hostname
    # subscribe_dict["path"] = pathname
    json1 = json.dumps(subscribe_dict)  # 转换成json
    print("添加混淆参数后json内容：", json1)
    json2 = 'vmess://' + bytes.decode(base64.b64encode(json1.encode('UTF-8'))) + "\r\n"  # 拼接vmess头
    return json2


if __name__ == '__main__':
    server = MyThreadingHTTPServer(host, Request)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()
