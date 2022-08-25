# gitlab server create


[脑图](https://naotu.baidu.com/file/2cadc79c0c5adba8514d1af2302b5512)
[Refe Link](https://www.cnblogs.com/diaomina/p/12830449.html)
[docker-compose.yml](../docker/docker-compose.yml)


::: tip 
- 初始账号：root/gitlab123456
- 重置root密码
    - gitlab-rails console -e production
    - user = User.where(username:"root").first
    - user.password = "新密码" (密码加引号）
    - user.password_confirmation ="再次确认密码"
    - user.save!
:::
::: tip container gitlab config
- vi /etc/gitlab/gitlab.rb 加入三行
   定义container内容网络和端口
   ```raw
   external_url 'http://gitlab:80'
   gitlab_rails['gitlab_ssh_host'] = 'gitlab'
   gitlab_rails['gitlab_shell_ssh_port'] = 22
   ```
- gitlab-ctl reconfigure 配置生效,会重新gitlab.yml文件
- vi /opt/gitlab/embedded/service/gitlab-rails/config/gitlab.yml
   ```yml
    gitlab settings:
    host: kunvm1.ap.health.ge.com
    port: 9980
    https: false
    ssh_host: kunvm1.ap.health.ge.com
   ```
   ==gitlab 网页对repo操作提示所用，clone操作提示地址==
- gitlab-ctl restart 重启gitlab
- clone repo支持http和ssh协议  

:::




