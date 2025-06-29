# Git 

- Third-party apps : gitkraken, p4merge
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
- store credentials permanantly
```bash
git credential-osxkeychain #check if keychain helper is installed
git config --global credential.helper osxkeychain
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

- set pull and push default remote branch
```bash
# Push to origin and set upstream so future `git push`/`git pull` use origin/my-feature
git push --set-upstream origin my-feature
# shorthand:
git push -u origin my-feature
```

- set pull and push remote branch
```bash
# pull
git branch --set-upstream-to=origin/r2/trs/sprint-2-head r2/trs/feat/trs-1927
# push
git config branch.r2/trs/feat/trs-1927.pushRemote upstream
```

- verify
```bash
git config --get branch.r2/trs/feat/trs-1927.remote
# pull (origin)

git config --get branch.r2/trs/feat/trs-1927.merge
# merge

git config --get branch.r2/trs/feat/trs-1927.pushRemote
# push (upstream)
```

- initialize a new repository
```bash
git init
```
## Staging Area

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

## Remote
### Push
- Push to github
- clone 
```bash
git clone <copied URL> <folder name> 
```
- add remote repo as local repo
```bash
git remote add origin <paste copied URL here> 
```
- push master branch to remote repo & set it as default remote branch
```bash
git push --set-upstream origin master 
```
- push local to github
```bash
git push origin 
``` 

### pull 
- show remote repos
```bash
git remote

git remote -v
```

- Shows remote tracking branches
```bash
git branch -r
```

- Shows local & remote tracking branches
```bash
git branch -vv
```

- Fetches master from origin (download new commits from remote)
```bash
git fetch origin master
``` 

- Fetches all objects from origin
```bash
git fetch origin
# or
git fetch
```

- pull from repo
```bash
git pull
```

- pull and rebase
```bash
git pull --rebase
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

- output 1 if any changes detected else 0
```bash
git diff --cached --exit-code
```

- delete from working dir & staging area
```bash
git rm *.txt
```

- delete from staging area
- delete <file> from git index(staging area) and not from local
```bash
git rm --cached <file>
```

- renaming & moving files from working dir & staging area
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
- show commits for branching
```bash
git log --oneline --all --graph
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
git log --oneline -3
```
- filter by author
```bash
git log --oneline --author="Mosh"
```
- filter by date
```bash
git log --oneline --before/after="2020-12-2"/"one week ago"
```
- filter by commit message
```bash
git log --oneline --grep="GUI"
```

## show commits diffs
- hashkey : first char till any char as long as its unique
```bash
git show <hashkey>
git show HEAD # most recent
git show HEAD~<n> #nth previous from the last
```
- show commits contents
```bash
git show <hashkey>:<file> 
git show HEAD~<n>:<dir/file> #nth previous from the last
```

- without the commit header
```bash
git show --pretty="" --name-only <commit>
```

- emit names
- diff-filter => A (added) M (modified) D (deleted)
```bash
git show --pretty="" --diff-filter=AM <commit>
```

- diff between two commits
```bash
git diff HEAD^ HEAD #last two commits
git diff HEAD~1 HEAD #last two commits
```

- summary
```bash
git diff --stat HEAD~1 HEAD
```

### tag
- create lightweight tag & assign to <commit>(default: last commit)
```bash
git tag <tagname> <commithash>
```

- annotated tag
```bash
git tag -a <tag> -m "<message>"
```

- push local tags to github 
```bash
git push origin <tag:v1.0> 
``` 

- remove tag
```bash
git push origin --delete <tag>
```

- checkout to labeled commit
```bash
git checkout <tag>
```
- list of all tags
```bash
git tag
```
- list tags along with their messages
```bash
git tag -n
```
- show specific tag
```bash
git show <tag>
```
- delete tag
```bash
git tag -d <tag>
```

### help
- options
```bash
git <command> -help 
```
- all possible commands
` git help --all `

### revert

- point the head to the previous commit (rollback one commit)
> soft : last snapshot reset only
> mixed(default) : last snapshot and staging area reset
> hard : last snapshot, staging area & working dir reset to previous commit snapshot(commit)
```bash
git reset --<option:hard> HEAD~1/<commithash> <--no-edit> # no-edit -> without message
```
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

- checkout to commit
> no branch
```bash
git checkout <commit hash>
```

- undo merge
```bash
git reset --<option:hard> HEAD~1/<commithash>
```

- revert merge
> -m 1 : revert to first parent commit (on Master branch; last commit on master branch before merge)
```bash
git revert -m 1 HEAD
```

- Changes the base of the current branch to master
```bash
git rebase master
```

- replace the current commit head with the remote commit
```bash
git reset --hard origin/main
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
# or rename current branch
git branch -m <new branch name>‍‍‍‍‍‍‍‍
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

# delete
- local
```bash
git branch --delete <branch name> 
``` 
```bash
git branch -d <branch name> 
``` 

- remote
```bash
git push origin --delete <remote>
```

- local and remote branches
```bash
git branch -a 
```
- remote branches
```bash
git branch -r 
```

- push local to remote
```bash
git push -u origin <branch>
```

### Comparing branches
- Lists the commits reachable from <branch1> that aren't in <branch2> 
```bash
git log <branch2>..<branch1>
```
- summary of changes
```bash
git diff main..<branch>
```
```bash
git diff main..<branch>
```

### Stashing
> save changes to working dir before branching or merging
- Create a new stash
```bash
git stash save "New tax rules"
```

- Include untracked files
```bash
git stash -u
```

- List all the stashes
```bash
git stash list
```

- Show the given stash
```bash
git stash show stash@{1}
# shortcut
git stash show 1
```

- Apply latest stash
```bash
git stash apply
```

- Apply the given stash to the working dir
```bash
git stash apply 1
```

- Delete the given stash
```bash
git stash drop 1
```

- Apply and delete given stash
```bash
git stash pop 1
```

- Delete all the stashes
```bash
git stash clear
```


### Merge
> Fast-forward : if branches have not diverged (master doesnt contain any changes after branching)
> 3-way : if branches have diverged (before-code , and after-code snapshots -> the common ancestor and the lates commits in both branches)

- show commits for branching
```bash
git log --oneline --all --graph
```

- after the conflicts -> git status -> open the unmerged path files -> change them -> add & commit

- Set conflict tool
```bash
git config --global merge.tool <tool:p4merge>
git config --global mergetool.p4merge.path "<tool_path>"
```

- Merges the <branch> into the current branch (fast-forward by default)
```bash
git merge <branch>
```
- use tool when conflict
```bash
git mergetool
```

- Creates a merge commit even if FF is possible
```bash
git merge --no-ff <branch>
```

- Disable Fast forwarding
```bash
git config --global ff no # apply to all repos
```

- Performs a squash merge
> add commits of branch to master without merge commit
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

## Remote
### Cloning a repository
- Clone a repository from a URL
```bash
git clone <url>
```

### Syncing with remotes
- Fetches master from origin
```bash
git fetch origin master
```

- Fetches all objects from origin
```bash
git fetch origin
```

- Shortcut for “git fetch origin”
```bash
git fetch
```

- Fetch + merge
```bash
git pull
```

- Pushes master to origin
```bash
git push origin master
```

- Shortcut for “git push origin master”
```bash
git push
```

## cherry pick
```bash
git cherry-pick <commit hash1> <commit hashn>
```