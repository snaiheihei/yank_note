# paramiko ssh远程连接

::: tip 
-  paramiko是一个基于SSH用于连接远程服务器并执行相关操作（SSHClient和SFTPClinet,即一个是远程连接，一个是上传下载服务），使用该模块可以对远程服务器进行命令或文件操作
-  set_missing_host_key_policy()：设置远程服务器没有在know_hosts文件中记录时的应对策略；一般添加==AutoAddPolicy==，即新建立ssh连接时不需要再输入yes或no进行确认.
-  exec_command()：在远程服务器执行Linux命令的方法。
-  open_sftp()：在当前ssh会话的基础上创建一个sftp会话。该方法会返回一个SFTPClient对象。

```python
# 密码方式连接
import paramiko   
 
ssh_client = paramiko.SSHClient()   
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())   
# 连接SSH服务端，以用户名和密码进行认证 ，调用connect方法连接服务器
ssh_client.connect(hostname='192.168.137.105', port=22, username='root', password='123456')   
stdin, stdout, stderr = ssh_client.exec_command('df -hT ') 
print(stdout.read().decode('utf-8'))  
ssh_client.close()


# 私钥方式连接
private = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa') 
#实例化SSHClient
ssh_client = paramiko.SSHClient() 
#自动添加策略，保存服务器的主机名和密钥信息，如果不添加，那么不再本地know_hosts文件中记录的主机将无法连接
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
#连接SSH服务端，以用户名和密码进行认证
ssh_client.connect(hostname='192.168.137.100',port=22,username='root',pkey=private)
sftp_client = ssh_client.open_sftp()
# 执行上传动作
sftp.put(local_path, remote_path)
# 执行下载动作
sftp.get(remote_path, local_path) 
```
:::

