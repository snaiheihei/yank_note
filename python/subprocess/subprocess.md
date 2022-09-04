# subprocess执行系统命令

::: tip 

- 指定命令一般重定向标准输出和错误到文件，不交互标准输入也不读取标准输出和错误到缓存
- shell：如果该参数为 True，将通过操作系统的 shell 执行指定的命令，就使用shell来解释执行这个字符串。如果args是个列表，则第一项被视为命令，其余的都视为是给shell本身的参数。
- p.stdin, p.stdout, p.stderr：分别表示程序的标准输入、输出、错误句柄
- Popen.pid 该子进程pip
- Popen.kill() 结束子进程，需要延时poll才能获取到正确的状态
- Popen.poll()检查子进程状态：0 正常结束  None 在运行  -num 被该程序终止
```python
import subprocess
import time

cmd = "nohup ping 10.189.130.233 2>&1 > /dev/null & "
# 指定命令一般重定向标准输出和错误到文件，不交互标准输入也不读取标准输出和错误到缓存
# 示例popen对象
p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#p.stdout.read()
#p.stderr.read()
print(p.pid)
print(p.poll())

p.kill()
time.sleep(1)
print(p.poll())
```

:::

