import requests
import threading
import queue


q = queue.Queue()

valid_proxies = []

with open("./proxies.txt",'r') as file:
    proxies = file.read().split("\n")
    for p in proxies:
        q.put(p)

def send_proxy(): 
    '''
    Checking if a proxy is valid by making a test request.
    By Sending requests to a target URL using a proxy from the queue.

    '''
    global q
    while not q.empty():
        proxy = q.get()
        try:
            res = requests.get("http://ipinfo.io/json",proxies={"http":proxy,
                                                                "https":proxy})
        except:
            continue

        if(res.status_code == 200):
            with open('./valid_proxies.txt','w') as f:
                f.write(f"{proxy}\n")


for _ in range(10):
    threading.Thread(target=send_proxy).start()
