import json
from pwshell import script
from app import instances_info
from ssh_connection import ssh_connection
from porta import open_door
from Construct_promeheus_config import prometheus_config

ssh = ssh_connection()
instances = instances_info()
build_prometheus = prometheus_config()
class prometheus_env:
    def build_target(self):
        instances_ips = instances.get_ips()
        ips_port = self.valid_ips(instances_ips)
        print(ips_port)

        target_dict_linux = [
            {
                "targets": ips_port['ips_port_linux'],
                "labels": {
                    "job": "node-exporter"
                }

            }

        ]

        target_dict_win = [
            {
                "targets": ips_port['ips_port_win'],
                "labels": {
                    "job": "win-exporter"
                }

            }

        ]

        with open('linux.json', 'w') as prometheus_targets_linux:
            json.dump(target_dict_linux, prometheus_targets_linux)

        with open('win.json', 'w') as prometheus_targets_win:
            json.dump(target_dict_win, prometheus_targets_win)

        return self.install_exporter(instances_ips)

    def install_exporter(self, instances_ip):
        if not len(instances_ip['windows_ips']) == 0:
            self.build_connection_windows(instances_ip)

        if not len(instances_ip['linux_ubuntu_ips']) == 0:
            self.build_connection_ubuntu(instances_ip)

        if not len(instances_ip['linux_centos_7_ips']) == 0:
            self.build_connection_centos_7(instances_ip)

        if not len(instances_ip['linux_centos_8_ips']) == 0:
            self.build_connection_centos_8(instances_ip)

    def valid_ips(self, ips_dict):
        ips_port_win = []
        ips_port_linux = []
        for keys in ips_dict:
            for ips in ips_dict[keys]:
                if keys == 'windows_ips':
                    ips_port_win.append(str(ips+":9182"))
                else:
                    ips_port_linux.append(str(ips+":9100"))
        return {
           "ips_port_win": ips_port_win,
            "ips_port_linux": ips_port_linux
        }

    def build_connection_ubuntu(self, instances_ip):
        print(instances_ip)
        for ips in instances_ip['linux_ubuntu_ips']:
            ssh.ubuntu_conn_install_exporter(ips, "ubuntu")

    def build_connection_windows(self, instances_ip):
        for ips in instances_ip['windows_ips']:
            script(ips), open_door(ips)


    def build_connection_centos_7(self, instances_ip):
        for ips in instances_ip['linux_centos_7_ips']:
            ssh.centos_conn_install_exporter_7(ips, "centos", "yum")

    def build_connection_centos_8(self, instances_ip):
        for ips in instances_ip['linux_centos_8_ips']:
            ssh.centos_conn_install_exporter_8(ips, "centos", "yum")

batman = prometheus_env()
def teste():
    build_prometheus.build_yaml_gamb()
    batman.build_target()

teste()