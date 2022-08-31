# bugdispatch

```python
# -*- coding: utf-8 -*-
import requests
import os
from git import Repo
import re
# import shutil
import time 
import datetime
from threading import Thread

class BugDispatch(object):
    
    def __init__(self, local_code_path):
        self.local_code_path = local_code_path
        self.origin_git = "xxxx.git"
        self.all_files = []
        # 开启一线程异步同步代码 self.clone_timer(),主线程结束应停止该线程daemon=True
        t1 = Thread(target=self.clone_timer, daemon=True)
        t1.start()

    def files_map(self):
        # 文件名和文件的绝对路径映射表
        mapping_data = {}
        self.find_all_file()
        # 二维列表数据扁平化处理
        files_data = [j for i in self.all_files for j in i]
        try:
            for doc in files_data:
                mapping_data[doc.split('/')[-1]] = doc
                # mapping_data[os.path.basename(doc)] = doc
        except Exception as e:
            print(e)
        return mapping_data

    def find_all_file(self, path=None):
        # 第一次传参取本地备份代码repo,递归取到该repo下的所有文件绝对路径列表（二维）
        if path is None:
            path = self.local_code_path
        lsdir = os.listdir(path)
        file_ls = [os.path.join(path, item) for item in lsdir if os.path.isfile(os.path.join(path, item))]
        dir_ls = [os.path.join(path, item) for item in lsdir if os.path.isdir(os.path.join(path, item))]
        self.all_files.append(file_ls)
        if dir_ls:
            # 递归参数向默认结果收敛,避免进入死循环
            for item in dir_ls:
                self.find_all_file(item)

    # 手动初始化一次仓库
    # def clone_repo(self):
    #     # 克隆仓库并复制文件,初始化clone一次仓库，后续pull更新
    #     Repo.clone_from(Repo=self.origin_git, path=self.local_code_path)
    #     # shutil.copy(self.download_path, self.local_code_path)

    def clone_timer(self): 
        # 定时pull代码更新,不应放到主进程中，应放到一个线程中异步执行
        while True:
            if datetime.datetime.now().minute % 59 == 0:
            # do something 
                Repo.pull(self.origin_git)
                time.sleep(60)

    def parse_bug(self, log_url):
        # 分析android crash bug txt文件，定位报错文件和行号
        header = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"\
"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"} 
        data = requests.get(url=log_url, headers=header).content.decode('utf-8')
        try:
            pattern = r'\w+\.java:\d+'
            regex = re.compile(pattern)
            file_name_list = [i.split(":")[0] for i in regex.findall(data)]
            file_name = regex.findall(data)[0].split(":")[0]
            # 从映射文件表取出bug文件绝对路径
            mapping_data = self.files_map()
            bug_file_name = mapping_data.get(file_name)
            bug_file_num = regex.findall(data)[0].split(":")[1]
            bug_file_num_list = [ i.split(":")[1] for i in regex.findall(data)]
            # 日志文件 bug flie & bug file num
            self.map_file_num = zip(file_name_list, bug_file_num_list)
            # print(dict(self.map_file_num))
            return  bug_file_name, bug_file_num
        except Exception as e:
            print(e)

    def get_bug_author(self, log_url):
        # icode_path = '/Users/wangxue29/Downloads/bug_project/'
        # 实例一个本地Repo仓库
        repo = Repo(path=self.local_code_path)
        git_bash = repo.git
        if  self.parse_bug(log_url) is not None:
            file_name,file_num = self.parse_bug(log_url)

            self.get_map_author_data(git_bash)
            if file_name is None:
                return None
            # git blame 查看修改改行代码的作者
            log_info = git_bash.blame( file_name)
            try:
                crash_line = [doc.strip() for doc in log_info.split('\n')][int(file_num)-1]
                author_name = crash_line.split("(")[1].strip("(").strip().split(" ")[0].replace(',', '')
                return author_name
            except Exception as e:
                print(e)
                return None
        else:
            return None

    def get_map_author_data(self,bash):
        mapping_data = self.files_map()
        map_file_num_author = {}
        try:
            for i, j in self.map_file_num:
                try:
                    log_info = bash.blame(mapping_data.get(i))
                    crash_line = [doc.strip() for doc in log_info.split('\n')][int(j)-1]
                    author_name = crash_line.split("(")[1].strip("(").strip().split(" ")[0].replace(',', '')
                    map_file_num_author[i] = [j,author_name]    
                except:
                    map_file_num_author[i] = [j,None]
        except Exception as e:
            print(e)
        print(map_file_num_author)
        return map_file_num_author


if __name__ == '__main__':
    bug = BugDispatch('/Users/v_gaofuli/code_baidu/androidtrunk')
    author = bug.get_bug_author('http://bj.bcebos.com/v1/xmonkey-android/online/980188/TOOSJOB_20200819122206_332946_980188_20200819122523848/20200819122523848/Run1/crash/08-19%2012:32:59.505_efad3590a1c21ebe59dad2c68a065146.txt')
    print(author)

```
