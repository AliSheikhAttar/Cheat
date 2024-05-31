# Git 
## Setup
- Setup
` git config --global user.name “<Enter your username here>” `
` git config --global user.email “<Enter your email here>” `
` git init `

## Push to github
- clone 
` $ git clone <copied URL> <folder name> `
- add remote repo as local repo
` git remote add origin <paste copied URL here> `
- push master branch to remote repo & set it as default remote branch
` git push --set-upstream origin master `
- push local to github
` git push origin ` 

## add to staging environment
` git add .`
` git add -A `
` git add --all `

## commit 
- commit staged files
`git commit -m "This commit is a mistake"`
- commit without staging
` git commit -a -m “<Enter your message here>” `

## status
- more compact way
` git status --short ` 

## delete from git repo
- delete <file> from git index(staging area) and not from local
```bash
git rm --cached <file>
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