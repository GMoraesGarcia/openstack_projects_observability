import time
import os
from pypsrp.client import Client
from wrapt_timeout_decorator import *


user = os.environ["USERNAME"]
passwd = os.environ["PASSWORD"]




@timeout(45)
def script(host):
    try:
        with Client(host, ssl=False, username=user, password=passwd) as client:
            print("Conectado")
            client.copy("/home/ubuntu/observabilidade/windows_exporter-0.18.1-386.msi",
                        "C:\\Users\\" + user + "\\AppData\\Local\\Microsoft\\windows_exporter-0.18.1-386.msi")
            time.sleep(1)
            print("Copiado")
            time.sleep(1)
            client.execute_cmd("C:\\Users\\" + user + "\\AppData\\Local\\Microsoft\\windows_exporter-0.18.1-386.msi")
            time.sleep(1)
            print("Executando")
            client.close()
    except:
        client.close()
        print("timeout")



