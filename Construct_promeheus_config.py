import yaml
import os
CLUSTER_NAME = os.environ["CLUSTER_NAME"]
class prometheus_config:

    def build_yaml_gamb(self):
        prometheys_yaml = """
global:
  scrape_interval: 5s
  external_labels:
    cluster: """+CLUSTER_NAME+"""
    monitor: 'bc-monitor'
scrape_configs:
  - job_name: 'node-exporter'
    file_sd_configs:
    - files:
        - '/etc/prometheus/linux.json'
  - job_name: 'win-exporter'
    file_sd_configs:
    - files:
      - '/etc/prometheus/win.json'
  - job_name: 'thanos'
    scrape_interval: 5s
    static_configs:
      - targets:
        - 'thanos-sidecar:10902'
        - 'thanos-store-gateway:10902'
        - 'thanos-querier:10902'
          # THANOS RECEIVE
#remote_write:
  #- url: 'http://10.0.1.182:10908/api/v1/receive'
        """


        with open('prometheus.yaml', 'w') as testefile:
            testefile.write(prometheys_yaml)
    def build_prometheus(self):
        teste = [{'job_name': 'node-exporter'}]

        prometheu_yaml = {
           'global': {
               'scrape_interval': '5s',
               'external_labels': {
                   'cluster': CLUSTER_NAME,
                   'monitor': 'bc-monitor'
               }
           },
            'scrape_configs': {
                teste
            }


        }
        with open('prometheus.yaml', 'w') as testefile:
            yaml.dump(prometheu_yaml, testefile)

