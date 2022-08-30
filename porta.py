import time
import os
from pypsrp.client import Client
from wrapt_timeout_decorator import *


user = os.environ["USERNAME"]
passwd = os.environ["PASSWORD"]

@timeout(15)
def open_door(host):
    try:
        with Client(host, ssl=False, username=user, password=passwd) as client:
            client.execute_cmd("netsh advfirewall firewall add rule name= Port_9182 dir=in action=allow protocol=TCP localport=9182")
            print("Saida ok")
            time.sleep(1)
            client.close()
            print("Finalizado")
    except:
        client.close()
        print("Erro")
