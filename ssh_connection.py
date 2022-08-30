import time

import paramiko


class ssh_connection:

    def ubuntu_conn_install_exporter(self, ip, username, key_file_name="key.pem"):
        print(username)
        print(key_file_name)
        try:
            host = ip
            key = paramiko.RSAKey.from_private_key_file(key_file_name)
            conn = paramiko.SSHClient()
            conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            conn.connect(hostname=host, username=username, pkey=key)
            print("conectado")
            command_list_docker_update = ["sudo apt update -y", "sudo apt install docker.io -y",
                                "sudo docker run -d --restart always -p 9100:9100 --name bc-monitoring-agent prom/node-exporter"]

            for value in command_list_docker_update:
                stdin, stdout, stderr = conn.exec_command(value)
                lines = stdout.readlines()
                print(lines)

            conn.close()
            del conn, stdin, stdout, stderr
            return "exporter instalado"
        except:
            self.change_username(ip, username, key_file_name)

    def centos_conn_install_exporter_7(self, ip, username, key_file_name="key.pem"):
        try:
            centos_username = "centos"
            host = ip
            key = paramiko.RSAKey.from_private_key_file(key_file_name)
            conn = paramiko.SSHClient()
            conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            conn.connect(hostname=host, username=centos_username, pkey=key)
            print("conn sucess")
            command_docker_verify = (
                "sudo systemctl status docker")  # sudo apt install docker -y;sudo docker run -d --restart always -p 9100:9100 prom/node-exporter; sudo docker ps

            stdin, stdout, stderr = conn.exec_command(command_docker_verify)
            lines = stdout.readlines()
            print(lines)

            if len(lines) == 0:
                print("nova instalacao")
                command_list_install_docker = ["sudo yum update -y",
                                               "sudo yum install docker -y", "sudo systemctl start docker", "sudo docker run -d --restart always -p 9100:9100 --name bc-monitoring-agent prom/node-exporter"]
                for value in command_list_install_docker:
                    stdin, stdout, stderr = conn.exec_command(value)
                    lines = stdout.readlines()
                    print(lines)
            else:
                command_docker_ps = "sudo docker run -d --restart always  -p 9100:9100 --name bc-monitoring-agent prom/node-exporter" #"sudo " + dependency_manager + " remove docker.io -y; sudo " + dependency_manager + " remove docker-compose -y"
                stdin, stdout, stderr = conn.exec_command(command_docker_ps)
                lines = stdout.readlines()
                print(lines)


            conn.close()
            del conn, stdin, stdout, stderr
            return "deu bom"
        except:
            self.change_username(ip, username, key_file_name)

    def centos_conn_install_exporter_8(self, ip, username, key_file_name="key.pem"):
        try:
            centos_username = "centos"
            host = ip
            key = paramiko.RSAKey.from_private_key_file(key_file_name)
            conn = paramiko.SSHClient()
            conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            conn.connect(hostname=host, username=centos_username, pkey=key)
            print("conn sucess")
            command_docker_verify = (
                "sudo systemctl status docker")  # sudo apt install docker -y;sudo docker run -d --restart always -p 9100:9100 prom/node-exporter; sudo docker ps

            stdin, stdout, stderr = conn.exec_command(command_docker_verify)
            lines = stdout.readlines()
            print(lines)

            if len(lines) == 0:
                print("nova instalacao")
                command_list_install_docker = ["sudo sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*",
                                               "sudo sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*",
                                               "sudo yum update -y",
                                               "sudo yum install docker -y", "sudo systemctl start docker", "sudo docker run -d --restart always -p 9100:9100 --name bc-monitoring-agent prom/node-exporter"]
                for value in command_list_install_docker:
                    stdin, stdout, stderr = conn.exec_command(value)
                    lines = stdout.readlines()
                    print(lines)
            else:
                command_docker_ps = "sudo docker run -d --restart always  -p 9100:9100 --name bc-monitoring-agent prom/node-exporter" #"sudo " + dependency_manager + " remove docker.io -y; sudo " + dependency_manager + " remove docker-compose -y"
                stdin, stdout, stderr = conn.exec_command(command_docker_ps)
                lines = stdout.readlines()
                print(lines)


            conn.close()
            del conn, stdin, stdout, stderr
            return "deu bom"
        except:
            self.change_username(ip, username, key_file_name)

    def debian_conn_install_exporter(self, ip, username, key_file_name="key.pem"):
        try:
            debian_username = "debian"
            host = ip
            key = paramiko.RSAKey.from_private_key_file(key_file_name)
            conn = paramiko.SSHClient()
            conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            conn.connect(hostname=host, username=debian_username, pkey=key)

            print("conn sucess")
            command_docker_verify = (
                "sudo docker version")  # sudo apt install docker -y;sudo docker run -d --restart always -p 9100:9100 prom/node-exporter; sudo docker ps

            stdin, stdout, stderr = conn.exec_command(command_docker_verify)
            lines = stdout.readlines()
            print(lines)
            if len(lines) == 0:
                print("nova instalacao")

                command_list_docker_update = ["cd /home/debian",
                                              "wget https://object.wse.zone/v1/AUTH_37c68a88eed54efea7245b395e34893a/bashfiles/install.sh",
                                              "source install.sh"]

                for value in command_list_docker_update:
                    stdin, stdout, stderr = conn.exec_command(value)
                    time.sleep(5)
                    lines = stdout.readlines()
                    print(lines)
            else:
                command_docker_ps = "sudo docker run -d --restart always  -p 9100:9100 --name bc-monitoring-agent prom/node-exporter" #"sudo " + dependency_manager + " remove docker.io -y; sudo " + dependency_manager + " remove docker-compose -y"
                stdin, stdout, stderr = conn.exec_command(command_docker_ps)
                lines = stdout.readlines()
                print(lines)

            conn.close()
            del conn, stdin, stdout, stderr
            return "deu bom"
        except:
            self.change_username(ip, username, key_file_name)

    def change_username(self, ip, username_actual, key_file_name):
        print("changing username")
        new_key = key_file_name
        if username_actual == "ubuntu":
            new_username = "debian"
        if username_actual == "debian":
            new_username = "fedora"
        if username_actual == "fedora":
            new_username = "core"
        if username_actual == "core":
            new_key = self.change_key(key_file_name)
            print("mudando chave")
            new_username = "ubuntu"

        return self.ubuntu_conn_install_exporter(ip, new_username, new_key)

    def change_key(self, key_file_name):
        if key_file_name == "key.pem" and not self.empty_key_file("key2.pem"):
            print("chave2")
            return "key2.pem"
        if key_file_name == "key2.pem" and not self.empty_key_file("key3.pem"):
            print("chave3")
            return "key3.pem"
        if key_file_name == "key3.pem":
            return Exception('chave não encontrada')

        return Exception('chave não encontrada')

    def empty_key_file(self, file_name):
        with open(file_name) as file:
            items = len(file.readlines())
            if items <= 3:
                return True

        return False


