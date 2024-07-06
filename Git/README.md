# Git 

## Setup
- system : all users
- global : user all repositories
- local : this repository
- Setup Name, Email, Editor
```bash
git config --global user.name “<Enter your username here>” 
git config --global user.email <Enter your email here> 
git config --global core.editor "code --wait" -wait until the vscode instance is closed
```
- configure the configuration file
```bash
git config --global -e
```
- End of line
- input : don't add /r when pulling from repo/ Mac/Linux
- true : add /r when pulling from repo/ Windows
```bash
git config --global core.autocrlf input 
```
- config
```bash
git config --help
git config -h -short summary
```

- initialize a new repository
```bash
git init
```
## Staging Area & Repo

- add to staging environment
```bash 
git add .
git add -A
git add --all
```
### commit 
- commit staged files
```bash
git commit -m "This commit is a mistake"
git commit - for long messages 
```
- commit without staging
```bash
git commit -a -m “<Enter your message here>”
```
### Push
- Push to github
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
- pull and merge
```bash
git config pull.rebase false
git pull
```
## status & diff
- more compact way: left column -> staging area, right column -> working dir
```bash
git status -s --short
```

- provides a simplified output of the status of the working directory and staging area. If there are any changes (modified, added, deleted files), it will produce output
```bash
git status --porcelain: 
```

- files on stagin area
```bash
git ls-files
```
- ignore changes
```bash
git stash
```

- staged changes
- - -> last commit + -> staging area, @-x,y +z,s@ from line x/z y/s lines
```bash
git diff --staged
```

- not staged changes
- - -> staging area + -> working dir, @-x,y +z,s@ from line x/z y/s lines
```bash
git diff
```

- output 1 if any changes detected else 0
```bash
git diff --cached --exit-code
```
### config diff tool
- set vscode as diff tool
```bash
git config --global diff.tool vscode
```
```bash
git config --global difftool.vscode.cmd "code --wait --diff $LOCAL $REMOTE"
```

-- delete from working dir & staging area
```bash
git rm *.txt
```

-- delete from staging area
- delete <file> from git index(staging area) and not from local
```bash
git rm --cached <file>
```

-- renaming & moving files from working dir & staging area
```bash
git mv <file> <new_file>
```
## log & history
- history of commits for a repo
- sorted from latest to earliest
```bash
git log
```

- reverse sorting
```bash
git log --reverse
```

- first seven chars of commit hash  & commit message - short log
```bash
git log --oneline 
```
- log diffs & status
```bash
git log --oneline --stat
```
- log changes to files in commits
```bash
git log --oneline --patch
```
- n previous commits
```bash
git log --online -3
```
- filter by author
```bash
git log --online --author="Mosh"
```
- filter by date
```bash
git log --online --before/after="2020-12-2"/"one week ago"
```
- filter by commit message
```bash
git log --online --grep="GUI"
```

- show commits diffs
```bash
git show <hashkey> # first char till any char as long as its unique
git show HEAD~<n> #nth previous from the last
```
- show commits contents
```bash
git show <hashkey>:<file> # first char till any char as long as its unique
git show HEAD~<n>:<dir/file> #nth previous from the last
```
- show commits files
- blob : files, tree: dir
```bash
git ls-tree <hashkey>/<HEAD~<n>>
```
- show content of each file/dir
```bash
git show <hashkey of node> # as long as its not ambiguous
```

-- help
- options
` git <command> -help `
- all possible commands
` git help --all `

## revert

- revert to last commit and commit without message
` git revert HEAD --no-edit `

- revert to specific previous commit discardss to any changes made after that
` git reset <commithash> `

- point the head to the previous commit (rollback one commit)
```bash
git reset --hard HEAD~1
```
- change the last commit message
` git commit --amend -m “<Commit Message>” `

- undo changes from staging area
```bash
git restore --staged <file>
```
- undo changes from working dir (restore to last commit)
```bash
git restore <file>
```
```bash
git clean -fd <file> #f : force, d : all dirs
```

- undo changes from working dir (restore to any commit)
```bash
git restore --source=HEAD~<n> <file>
```
           

## Branching & Merging
- Create branch
```bash
git branch <banch_name> 
```

- checkout to branch
```bash
git switch <branch>
```
```bash
git checkout <branch_name> 
```
- rename branch
```bash
git branch -m <old branch> <new branch name>‍‍‍‍‍‍‍‍
```
- make branch and checkout to it
```bash
git checkout -b <branch name> 
```
```bash
git switch -C <branch>
```

- list
```bash
git branch --list 
```
```bash
git branch 
```

- delete
```bash
git branch --delete <branch name> 
``` 
```bash
git branch -d <branch name> 
``` 

- local and remote branches
```bash
git branch -a 
```
- remote branches
```bash
git branch -r 
```
### Comparing branches

- Lists the commits in the <branch> branch not in master
```bash
git log master..<branch>
```

- summary of changes
```bash
git diff master..<branch>
```
```bash
git diff master..<branch>
```
- Changed files
```bash
git diff --name-status <branch>
```

### Stashing

- Creates a new stash
```bash
git stash push -m "New tax rules"
```

- Lists all the stashes
```bash
git stash list
```

- Shows the given stash
```bash
git stash show stash@{1}
```

- Shortcut for stash@{1}
```bash
git stash show 1
```
- Applies the given stash to the working dir
```bash
git stash apply 1
```

- Deletes the given stash
```bash
git stash drop 1
```

- Deletes all the stashes
```bash
git stash clear
```


## Merge

- Merges the <branch> into the current branch
```bash
git merge <branch>
```

- Creates a merge commit even if FF is possible
```bash
git merge --no-ff <branch>
```

- Performs a squash merge
```bash
git merge --squash <branch>
```

- Aborts the merge
```bash
git merge --abort
```

- Shows the merged branches
```bash
git branch --merged
```

- Shows the unmerged branches
```bash
git branch --no-merged
```

- Changes the base of the current branch
```bash
git rebase master
```

- Applies the given commit on the current branch
```bash
git cherry-pick dad47ed
```


