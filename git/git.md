# git


[git脑图](https://naotu.baidu.com/file/a7dcc552a46c8912e20d991d1249ad85)



::: tip command
- git log 查看提交历史 ==alias git-log='git log -all --pretty=oneline --abbrev-commit --graph'==
- 版本切换：git reset --hard commitID
- git reflog 可以查看到删除掉的提交记录
- .gitignore (*.txt 指定不被git管理的文件)
- git branch -vv查看分支详细信息
- ==git checkout -b xxxbranch== 新建并切换到该分支
- git branch -d xxxbranch删除分支（-D强制删除）
- git merge dev 合并dev分支到当前分支
    - 解决冲突：确认冲突文件，手动确认修改，之后再git add . ---> git commit；
- 分支master 生产分支  develop 开发分支  feature/xxxx分支 hostfix/xxxx分支
:::
![Img](./FILES/git.md/img-20220816000241.png)

![Img](./FILES/git.md/img-20220815233421.png)


::: tip 更换远程仓库
- git remote -v :查看远程仓库信息
- git remote remove origin :删除远程仓库信息
- git clone  xxx.git :直接克隆远程仓库👻==推荐直接clone==
    - git push origin HEAD:dev (推送当前分支到远程dev分支，远程dev不存在会创建)
    - git branch --set-upstream-to=origin/main  dev 关联当前分支到远程分支,devtrack remote branch
-----
- git remote add  origin  <url>
    - url : git@url.git  / https://url.git
    - git pull origin master --allow-unrelated-histories(本地仓库有文件，远程仓库也有文件)   
    - git branch --set-upstream-to=origin/main  dev
    - git push origin HEAD:dev (推送当前分支到远程dev分支，远程dev不存在会创建) 
:::

