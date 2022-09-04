# process_bar

::: tip 显示进度条
tqdm示例参数含义
- total (int) 迭代总次数,==需与可迭代次数一致==
- desc（'str'）: 传入进度条的前缀
- mininterval（float）：最小的更新时间 [default: 0.1] seconds
- ascii（bool or str）：如果调整为True的话会使用#显示进度条
- ncols（int）：整个输出信息的长度
- colour（str）：进度条的颜色
- tqdm.update(1) 每次更新进度条步进
```python
import time
from tqdm import tqdm

with tqdm(total=50, desc='前缀', ascii=True, ncols=100, colour="green") as t:
    for i in range(50):
        time.sleep(0.03)
        t.update(1)
```
![Img](./FILES/process_bar.md/img-20220904221952.png)
- 获取命令行参数
```python
import sys
# 第一参数为脚本名 
print(sys.argv)
```
:::

::: tip loguru日志
[参考](https://blog.csdn.net/cui_yonghua/article/details/107498535)
- 常用日志level💌: info debug warning error critical
- logger.add('file_{time}.log', level="INFO", rotation='5 MB', encoding='utf-8')
- 记录日志文件时：level: 信息等级高于此等级的
- 循环，rotation，达到指定大小后建新日志或定时新建日志。
- 保留，retention，定期清理。
- 压缩，compression，压缩节省空间。
```python
from loguru import logger

logger.add("file_1.log", rotation="500 MB")  # 自动循环过大的文件
logger.add("file_2.log", rotation="12:00")  # 每天中午创建新文件
logger.add("file_3.log", rotation="1 week")  # 一旦文件太旧进行循环

logger.add("file_X.log", retention="10 days")  # 定期清理

logger.add("file_Y.log", compression="zip")  # 压缩节省空间
```

:::





