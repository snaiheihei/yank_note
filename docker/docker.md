# docker
[Docker Doc](https://docs.docker.com/)
[Docker Hub](https://hub.docker.com/)
[视频](https://www.bilibili.com/video/BV1CJ411T7BK?p=2&vd_source=327b91fe5f132d5f43cffb262b7cc19d)
![Img](./FILES/docker.md/img-20220823234430.png)

::: tip 
docker 是一种容器技术，解决软件环境迁移问题，沙箱机制，开销低
- 安装 yum install docker-ce
- docker 所在安装目录/var/lib/docker
- 卸载docker
    - 1
    - 2
:::

::: tip 
- 阿里云镜像加速配置[Link](https://cr.console.aliyun.com/cn-hangzhou/instances/mirrors)
    - 个人加速器地址：https://gebghx7u.mirror.aliyuncs.com
    ```sh
    sudo mkdir -p /etc/docker
    sudo tee /etc/docker/daemon.json <<-'EOF'
    {
    "registry-mirrors": ["https://gebghx7u.mirror.aliyuncs.com"]
    }
    EOF
    sudo systemctl daemon-reload
    sudo systemctl restart docker
    ```
    
    
:::


