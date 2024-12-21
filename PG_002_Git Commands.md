---
Established: 2024-12-21
Last Updated: 2024-12-21
Description: The cheat sheet of Git basic operations
---
# 基礎設定
```git
查詢版本
git version
 
查詢設定列表
git config --list
 
輸入姓名
git config --global user.name "你的名字"
 
輸入email
git config --global user.email "你的email"
# 新增本地/遠端數據庫

在本地資料夾新增數據庫
git init
 
複製遠端數據庫
git clone 遠端數據庫網址
# 增加/刪除檔案

增加檔案進入索引
git add 檔案名稱
 
增加全部檔案進入索引
git add .
 
查詢狀態
git status
 
顯示歷史紀錄
git log
git log --oneline
 
將索引提交到數據庫
git commit -m "更新訊息"
訊息要用雙引號
```
# 還原指令
```
回復工作目錄與索引到目前倒退一次commit紀錄
git reset HEAD^
git reset HEAD~1

回復工作目錄與索引到目前倒退兩次commit紀錄
git reset HEAD^^
git reset HEAD~2

回復工作目錄與索引到目前倒退五次commit紀錄
git reset HEAD~5

回復工作目錄與索引到某次commit紀錄
git reset <commit hash>

回復單一檔案到目前倒退一次commit紀錄
git reset HEAD 檔案名稱 

git reset 預設為 --hard 會自動刪除commit紀錄 
 
上面語法如果刪除錯了可以再用此語法還原
git reset ORIG_HEAD --hard
 
刪除最近一次 commit，但保留異動內容
git reset HEAD~1 --soft
 
commit 後發現有幾個檔案忘了加入進去，想要補內容進去時
git commit --amend
```

# 分支
```git
顯示所有本地分支
git branch
 
新增分支
git branch 分支名稱
 
切換分支
git checkout 分支名稱
 
檢視單一檔案到最新 commit 狀態
git checkout 檔案名稱

合併指定分支到目前的分支
git merge 分支名稱
 
刪除分支
git branch -d 分支名稱


```

# 遠端數據庫操作
```git
需要先在遠端數據庫開新的repository
複製遠端數據庫
git clone 遠端數據庫網址

推送本地事先建好的repository到遠端上
git remote add origin git@github.com:username/reponame.git

e.g. add github and bitbucket
git remote add githubNub https://github.com/kang62489/Nub.git
git remote add bitbucketNub https://kang62489@bitbucket.org/kang62489/nub.git


修改遠端數據庫名字
git remote rename <orignal name> <new name>

修改遠端數據庫位址
git remote set-url origin https://github.com/USERNAME/OTHERREPOSITORY.git

查詢遠端數據庫(必須要在有做過git init的資料路徑下)
git remote
git remote -v
 
將本地分支推送到遠端分支(同時修改upstream)
git push -u 遠端數據庫名稱 遠端分支名稱
單純只推送到遠端數據庫不用加-u
強制推送加上 --force

將遠端分支拉下來與本地分支進行合併
git pull
```

# 標籤
```git
查詢標籤
git tag
 
查詢詳細標籤
git tag -n
 
刪除標籤
git tag -d 標籤名稱
 
新增輕量標籤
git tag 標籤名稱
 
新增標示標籤
git tag -am "備註內容" 標籤名稱
```
# 暫存
```git
暫時儲存當前目錄
git stash
 
瀏覽 stash 列表
git stash list 
 
還原暫存
git stash pop
 
清除最新暫存
git stash drop
 
清除全部暫存
git stash clear
```

