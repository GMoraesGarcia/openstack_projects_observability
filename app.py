
from Project_connection import connect


conn = connect()
class instances_info:

    def load_server_infos(self):
        servers = conn.get_vms()['servers']
        server_inf = []
        # SEPARA AS INFORMACOES NECESSARIAS DAS INSTANCIAS
        for server in servers:
            server_infos = {
                "server_id": server['id'],
                "server_vols": server['os-extended-volumes:volumes_attached'],
                "network": server['addresses'],
                "project_id": server['tenant_id']
            }
            server_inf.append(server_infos)
        return server_inf

    def load_server_network(self, valid_server_list):
        network_inf = []
        ips = []
        for net in valid_server_list:
            network = net['network']
            for network_name in network:
                network_inf = network[network_name]
            for ipv4 in network_inf:
                if ipv4['OS-EXT-IPS:type'] == "fixed":
                    ips.append(ipv4['addr'])
        return ips

    def get_ips(self):
        linux_instance_ubuntu = []
        linux_instance_centos_7 = []
        linux_instance_centos_8 = []
        windows_instances = []
        valid_instances = self.load_server_volumes()
        print(valid_instances)
        if not len(valid_instances['linux_instance_ubuntu']) == 0:
            linux_instance_ubuntu = self.load_server_network(valid_instances['linux_instance_ubuntu'])
        if not len(valid_instances['win_instances']) == 0:
            windows_instances = self.load_server_network(valid_instances['win_instances'])
        if not len(valid_instances['linux_instance_centos_7']) == 0:
            linux_instance_centos_7 = self.load_server_network(valid_instances['linux_instance_centos_7'])
        if not len(valid_instances['linux_instance_centos_8']) == 0:
            linux_instance_centos_8 = self.load_server_network(valid_instances['linux_instance_centos_8'])

        return {
            "linux_ubuntu_ips": linux_instance_ubuntu,
            "linux_centos_7_ips": linux_instance_centos_7,
            "linux_centos_8_ips": linux_instance_centos_8,
            "windows_ips": windows_instances
        }

    def load_server_volumes(self):
        linux_instance_ubuntu = []
        win_instances = []
        linux_instance_centos_7 = []
        linux_instance_centos_8 = []

        try:
            for vol in self.load_server_infos():
                project_id = vol['project_id']
                for vol_ids in vol['server_vols']:
                    vol_infs = conn.get_vol_by_vol_id_project_id(project_id, vol_ids['id'])
                    #print(vol_infs)
                    if vol_infs['volume']['bootable'] == 'true':

                        if not vol_infs['volume']['volume_image_metadata']['image_name'] == 'BC-OPNsense-20.7' or \
                                vol_infs['volume']['volume_image_metadata']['image_name'] == 'BC-pfSense-2.5.2':
                            os_type = vol_infs['volume']['volume_image_metadata']['os_type']

                            if os_type == 'linux' and 'os_distro' in vol_infs['volume']['volume_image_metadata']:
                                os_distro = vol_infs['volume']['volume_image_metadata']['os_distro']
                                if os_distro == "ubuntu" or os_distro == "fedora-atomic" or os_distro == "fedora-coreos" or os_distro == "debian":
                                    linux_instance_ubuntu.append(vol)
                                if os_distro == "centos" and "7" in vol_infs['volume']['volume_image_metadata']['os_version']:
                                    print("centos7")
                                    linux_instance_centos_7.append(vol)
                                if os_distro == "centos" and "8" in vol_infs['volume']['volume_image_metadata']['os_version']:
                                    print("centos8")
                                    linux_instance_centos_8.append(vol)

                            if os_type == 'windows':
                                win_instances.append(vol)
            return {
                "linux_instance_ubuntu": linux_instance_ubuntu,
                "linux_instance_centos_7": linux_instance_centos_7,
                "linux_instance_centos_8": linux_instance_centos_8,
                "win_instances": win_instances
            }
        except:
            return "Not found volume Information in server " + str(vol_infs)

