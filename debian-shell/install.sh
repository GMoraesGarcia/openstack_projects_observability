sudo apt update -y
sudo apt install apt-transport-https ca-certificates curl gnupg2 software-properties-common -y
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"
sudo apt update -y
sudo apt install docker-ce -y
sudo docker run -d --restart always -p 9100:9100 --name bc-monitoring-agent prom/node-exporter