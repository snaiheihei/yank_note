# os

::: tip 
python脚本中默认的变量
- \_\_file__ 执行脚本的名字python  (/aa/bb/xxx.py)取整体名字 
- \_\_name__  为“_\_main__"
:::

::: tip 💌os path
[Link](https://zhuanlan.zhihu.com/p/388550931)
- os.getcwd() 执行脚本时所在路径
- ==os.path.abspath(\_\_file__)== 在脚本执行中获取该脚本所在的绝对路径（常用）
- os.path.dirname("path") 取字符串"\\"的前部分
- os.path.basename("path")  取字符串"\\"的后部分
- os.remove(file_name)                # 删除文件
- os.path.isfile(path)                # 判断指定路径目标是否为文件
- os.path.isdir(path)                 # 判断指定路径目标是否为目录
- os.path.join(path,*paths)           # 字符串以'\\'拼接
- ==os.listdir(path)==                    # 列出指定目录path的所有文件和目录名（常用）
示例，取出某个目录下的所有文件，包含递归
```python
all_files = []
def find_all_file(path=None):
    if path is None:
        path = "local_code_path"
    lsdir = os.listdir(path)
    file_ls = [os.path.join(path, item) for item in lsdir if os.path.isfile(os.path.join(path, item))]
    dir_ls = [os.path.join(path, item) for item in lsdir if os.path.isdir(os.path.join(path, item))]
    all_files.append(file_ls)
    if dir_ls:
        # 递归参数向默认结果收敛,避免进入死循环
        for item in dir_ls:
            find_all_file(item)
# 二维列表，扁平化处理
result = [j for i in all_files for j in i]
```


:::

