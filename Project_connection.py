import json
import os
import requests


ID = os.environ["ID"]
SECRET = os.environ["SECRET_KEY"]


class connect():
    def conn(self):
        url = "https://identity.wse.zone/v3/auth/tokens"
        id = ID
        secret = SECRET

        request = {
            "auth": {
                "identity": {
                    "methods": [
                        "application_credential"
                    ],
                    "application_credential": {
                        "id": id,
                        "secret": secret
                    }
                }


            }
        }

        headers = {'Content-type': 'application/json'}
        response = requests.post(url, headers=headers, data=json.dumps(request))
        token = response.headers['X-Subject-Token']
        return token

    def get_vms(self):
        headers = {'Content-type': 'application/json', 'X-Auth-Token': self.conn()}
        url = "https://compute.wse.zone/v2.1/servers/detail"

        response = requests.get(url, headers=headers)

        return response.json()



    def get_server_by_id(self, server_id):
        headers = {'Content-type': 'application/json', 'X-Auth-Token': self.conn()}
        url = "https://compute.wse.zone/v2.1/servers/"+server_id

        response = requests.get(url, headers=headers)

        return response.json()

    def get_vol_by_vol_id_project_id(self, project_id, vol_Id):
        headers = {'Content-type': 'application/json', 'X-Auth-Token': self.conn()}
        url = "https://volume.wse.zone/v3/"+project_id+"/volumes/"+vol_Id

        response = requests.get(url, headers=headers)

        return response.json()
