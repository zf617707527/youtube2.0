import json
import telnetlib
import requests
proxy_url = "https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list"


requests.adapters.DEFAULT_RETRIES = 20
s = requests.session()
# s.proxies = {"http": "27.152.8.152:9999","https":"117.57.91.131:24978"}
s.keep_alive = False
def save_ip(ip, port, type):
    proxies = {}
    try:
        # 测试是否能使用
        telnet = telnetlib.Telnet(ip, port=port, timeout=3)
    except Exception:
        print('unconnected')
    else:
        print('connected successfully')
        # proxyList.append((ip + ':' + str(port),type))
        proxies['type'] = type
        proxies['host'] = ip
        proxies['port'] = port
        proxiesJson = json.dumps(proxies)
        with open('verified_proxies.json', 'a+') as f:
            # f.write(proxiesJson + '\n')
            json.dumps(proxiesJson,f)
        print("已写入：%s" % proxies)


def getProxy(proxy_url):
    response = requests.get(proxy_url)
    proxy_list = response.text.split("\n")
    for proxy_str in proxy_list:
        proxy_json = json.loads(proxy_str)
        host = proxy_json["host"]
        port = proxy_json["port"]
        type = proxy_json["type"]
        save_ip(host, port, type)

if __name__ == "__main__":
    getProxy(proxy_url)
