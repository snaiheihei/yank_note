# ELK


[Include document](https://blog.csdn.net/qq_33204709/article/details/117256185)


## elasticsearch  start issues note

::: tip elasticsearch.yml configure
* network.host: 0.0.0.0
* http.port: 9200
* node.name: node-1
* cluster.initial_master_nodes: [“node-1”]
* bootstrap.system_call_filter: false
* xpack.security.enabled: false 
:::


:::: warning 
bootstrap checks failed:max virtual memory areas vm.max_map_count [65530] is too low,increase to at least [262144]

- [ ] su - 
- [ ] vim /etc/sysctl.conf 编辑此文件 添加  vm.max_map_count=262144 在文件末尾
- [ ] sysctl -p 立即生效
::::
:::: warning
bootstrap checks failed：the default discovery settings are unsuitable for production use; at least one of [discovery.seed_hosts, discovery.seed_providers, cluster.initial_master_nodes] must be configured

- [ ] vim elasticsearch.yml
- [ ] 修改 discovery下的 cluster.initial_master_nodes: ["node-1","node-2"] 
- [ ] node.name: node-1
      cluster.initial_master_nodes: ["node-1"] 
::::
:::: warning
max file descriptors [4096] for elasticsearch process is too low, increase to at least [65535]

- [ ] su -
- [ ] vim /etc/security/limits.conf
- [ ] * soft nofile 65536
      * hard nofile 65536
       或者限定某个用户
      elsearch soft nofile 65536
      elsearch hard nofile 65536
- ulimit -Sn/Hn 显示当前用户最大文件描述符
- su - elsearch 重切该用户生效
::::
::: tip 跨域访问
http.cors.enabled: true
http.cors.allow-origin: "*"
:::

## kibana start issue
::: tip kibana.yml configure
* server.port: 5601
* server.host: "IP"
* elasticsearch.hosts: ["http://IP:9200"]
:::

::: warning error one
'master_not_discovered_exception: [master_not_discovered_exception] Reason: null'
* vim elasticsearch.yml
* 添加 node.name: node-1
       cluster.initial_master_nodes: [“node-1”]
* restart elasticsearch
:::
::: tip beat 数  据采集器
- metricbeat modules lsit/enable/disable 展示modules, enable某个module
-   安装仪表盘
    - vim metricbeat.yml 添加： setup.kibana: 
                                 host xxxx:5601
   - metricbeat setup --dashboards
   - ./metricbeat modules enable xxxmodule 
   - vim ./modules.d/xxx.yml 开启所要记录的参数
   - ./metricbeat 开启收集
   -[更多modules介绍](https://www.elastic.co/guide/en/beats/metricbeat/7.13/metricbeat-module-docker.html)
:::
 