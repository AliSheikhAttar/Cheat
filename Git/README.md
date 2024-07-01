# Git 
## Setup
- system : all users
- global : user all repositories
- local : this repository
### Setup Name, Email, Editor
```bash
git config --global user.name “<Enter your username here>” 
git config --global user.email <Enter your email here> 
git config --global core.editor "code --wait" #wait until the vscode instance is closed
```
### configure the configuration file
```bash
git config --global -e
```
### End of line
- input : don't add /r when pulling from repo/ Mac/Linux
- true : add /r when pulling from repo/ Windows
```bash
git config --global core.autocrlf input 
```
### config
```bash
git config --help
git config -h #short summary
```

### initialize a new repository
```bash
git init
```
## Staging Area & Repo

### add to staging environment
```bash 
git add .
git add -A
git add --all
```
### commit 
- commit staged files
```bash
git commit -m "This commit is a mistake"
git commit # for long messages 
```
### commit without staging
```bash
git commit -a -m “<Enter your message here>”
```

### Push to github
- clone 
` $ git clone <copied URL> <folder name> `
- add remote repo as local repo
` git remote add origin <paste copied URL here> `
- push master branch to remote repo & set it as default remote branch
` git push --set-upstream origin master `
- push local to github
` git push origin ` 

### pull 
- pull from repo
```bash
git pull
```
### pull and merge
```bash
git config pull.rebase false
git pull
```
### files on stagin area
```bash
git ls-files
```
### ignore changes
```bash
git stash
```

### status
- more compact way: left column -> staging area, right column -> working dir
```bash
git status -s #--short
```

### staged changes
- - -> last commit + -> staging area, @-x,y +z,s@ from line x/z y/s lines
```bash
git diff --staged
```

### not staged changes
- - -> staging area + -> working dir, @-x,y +z,s@ from line x/z y/s lines
```bash
git diff
```

### output 1 if any changes detected else 0
```bash
git diff --cached --exit-code
```

### provides a simplified output of the status of the working directory and staging area. If there are any changes (modified, added, deleted files), it will produce output
```bash
git status --porcelain: 
```

## delete from working dir & staging area
```bash
git rm *.txt
```

## delete from staging area
- delete <file> from git index(staging area) and not from local
```bash
git rm --cached <file>
```

## renaming & moving files from working dir & staging area
```bash
git mv <file> <new_file>
```
## log
- history of commits for a repo
` git log `
` git log --oneline ` first seven chars of commit hash  & commit message

## help
- options
` git <command> -help `
- all possible commands
` git help --all `
## revert
- revert to last commit and commit without message
` git revert HEAD --no-edit `

- revert to any commit 
` git reset <commithash>`

- revert to the n-th previous commit

`git revert HEAD~<n>...HEAD`
- revert to specific previous commit discardss to any changes made after that
` git reset <commithash> `

- point the head to the previous commit (rollback one commit)
```bash
git reset --hard HEAD~1
```

## amend
- change the last commit message
` git commit --amend -m “<Commit Message>” `



## .gitignore

- ignore specific formats
*.<fileformat>

- ignore specific directories
<dir_name>               

## Branch
- Create branch
` git branch <banch_name> `
- checkout to branch
` git checkout <branch_name> `
- make branch and checkout to it
` git checkout -b <branch name> `
- list
` git branch --list `
` git branch `
- delete
` git branch --delete <branch name> ` 
` git branch -d <branch name> ` 
- merge branch with master
` git merge <branch name> `
- local and remote branches
` git branch -a `
- remote branches
` git branch -r `