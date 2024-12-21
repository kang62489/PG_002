---
Established: 2024-12-21
Last Updated: 2024-12-21
Description: The cheat sheet of Git basic operations (English Version)
---
# Basic Operation

```git title:"Check git version"
git version
```

```git title:"Check git configuration of local repository"
git config --list
``` 

```git title:"Set local user's name"
git config --global user.name "YOUR NAME"
``` 

```git title:"Set local user's email"
git config --global user.email "YOUR EMAIL"
```


# Create local/remote repository

```git title:"Set folder as local repository"
git init
``` 

```git title:"Clone any remote repository"
git clone "HTTPS LINK"
```


# add/remove files to the index for commit

```git title:"add one (changed) file"
git add FULL-FILENAME
``` 

```git title:"add all (changed) file"
git add .
``` 

```git title:"check status of local repository"
git status
```

```git title:"Show history of local repository"
git log
git log --oneline
``` 

```git title:"Commit the changes of files in the added index"
git commit -m "Updating info"
```


# Recovery

```git title:"Roll back 1 time of commit log"
git reset HEAD^
git reset HEAD~1
```

```git title:"Roll back 2 times of commit log"
git reset HEAD^^
git reset HEAD~2
```

```git title:"Roll back 5 times of commit log"
git reset HEAD~5
```

```git title:"Roll back to a certain commit log"
git reset <commit hash>
```

```git title:"Roll back a file to last commit log"
git reset HEAD <Filename>
# The default setting of git reset will delete the commit logs which were rolled back (--hard) 
```

 ```git title:"Recover from git reset"
git reset ORIG_HEAD --hard 
``` 

```git title:"Delete last commit log but keep the modified contents"
git reset HEAD~1 --soft 
``` 

```git title:"Cancel added files"
git reset
```

```git title:"Adding files to last commit (after committed)"
git commit --amend
```

# Branch

```git title:"Show all local branches"
git branch -a
``` 

```git title:"Create new branch"
git branch NAME-OF-YOUR-BRANCH
``` 

```git title:"Switching in different branches"
git checkout NAME-OF-THE-BRANCH
```

```git title:"Merge a branch to current branch"
git merge NAME-OF-THE-BRANCH
``` 

```git title:"Delete a branch"
git branch -d NAME-OF-THE-BRANCH
```


# Remote repository
Build New remote repository

## From Github
1. Create a new repository on Github first
2. Clone remote repository to the directory of your local PC
```git
git clone "HTTPS-LINK of your remote repository"
```

## From local PC
1. Create a new repository on Github first
2. Push local repository to remote repository
```git title:"add remote repository"
git remote add origin git@github.com:username/reponame.git
```

```git title:"add remote repository (example)"
#e.g. Adding Github and Bitbucket with specific names
git remote add githubNub https://github.com/kang62489/Nub.git
git remote add bitbucketNub https://kang62489@bitbucket.org/kang62489/nub.git
```

```git title:"Change name of remote repository that added in your local PC"
git remote rename <orignal name> <new name>
```

```git title:"Modify the link of added remote repository"
git remote set-url origin https://github.com/USERNAME/OTHERREPOSITORY.git
```

```git title:"Query remote repository(Need to use the comment in the directory of your local repository)"
git remote
git remote -v
``` 


```git title:"Push current branch in local repository to a branch in remote repository (and set upstream)"
git push -u NAME-OF-REMOTE-REPO NAME-OF-REMOTE-BRANCH
```
If you don't want to set upstream, no need to add "-u" 
Use --force to force git push commit logs to remote depo
Set upstream means your current branch will automatically switch to the one you pushed

```git title:"Update a local branch by merging remote branch"
git pull
```

# Tags you can use before commit

```git title:"Check tags of each committed log"
git tag
``` 

```git title:"Check full-length of your tags"
git tag -n
```

```git title:"Delete tag"
git tag -d NAME-OF-TAG
``` 

```git title:"Add a light tag"
git tag NAME-OF-TAG
``` 

```git title:"Add a tag with comments"
git tag -am "INFO OF THE TAG" NAME-OF-TAG
```
# Temporary preserve your changes of a local repository

```git title:"Temporary store your current working status"
git stash
``` 

```git title:"Query all temporarily saved status"
git stash list 
``` 

```git title:"Open and return to the status of the latest temporarily saved log"
git stash pop
``` 

```git title:"Remove the latest temporarily saved log"
git stash drop
``` 

```git title:"Remove all temporarily saved logs"
git stash clear
```
