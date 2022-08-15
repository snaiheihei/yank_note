# git


[git脑图](https://naotu.baidu.com/file/a7dcc552a46c8912e20d991d1249ad85)



::: tip 
Content
:::

::: tip 更换远程仓库
- git remote -v :查看远程仓库信息
- git remote remove origin :删除远程仓库信息
- git clone  xxx.git :直接克隆远程仓库 
- git remote add  origin  <url>
    - url : git@url.git  / https://url.git
    - git pull origin master --allow-unrelated-histories(本地仓库有文件，远程仓库也有文件)   
    - git branch --set-upstream-to=origin/main  dev
    - git config --global push.default simple (设置推送默认分支后续步骤）
    
:::

