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
- push local tags to github 
```bash
git push origin <tag:v1.0> 
``` 
- remove tag
```bash
git push origin --delete <tag>
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
### tag
- create lightweight tag & assign to <commit>(default: last commit)
```bash
git tag <tagname> <commithash>
```
- annotated tag
```bash
git tag -a <tag> -m "<message>"
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

- push local to remote
```bash
git push -u origin <branch>
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
- save changes to working dir before branching or merging
- Creates a new stash
```bash
git stash push -m "New tax rules"
```

- Add to stash
```bash
git stash push --all/-a -m "<message>"
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
- Continue rebasing, skipping commit, abort rebasing
```bash
git rebase --continue/skip/abort
```
- disable autmatically creating backup-file from mergetool
```bash
git config --global mergetool.keepBackup false
```

- Applies the given commit on the current branch
```bash
git cherry-pick <dad47ed>
```

- cherrypick a file from branch into master working dir
```bash
git restore --source=<branch_name> -- <file>
```

- replace the current commit head with the remote commit
```bash
git reset --hard origin/main
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

### Sharing tags
- Pushes tag v1.0 to origin
```bash
git push origin v1.0
```

- Deletes tag v1.0 from origin
```bash
git push origin --delete v1.0
```

### Sharing branches
- Shows remote tracking branches
```bash
git branch -r
```

- Shows local & remote tracking branches
```bash
git branch -vv
```

- Pushes <branch> to origin
```bash
git push -u origin <branch>
```

- Removes <branch> from origin
```bash
git push -d origin <branch>
```

### Managing remotes
- Shows remote repos
```bash
git remote
```

- Adds a new remote called <upstream>
```bash
git remote add <upstream> <url>
```

- Removes <upstream>
```bash
git remote rm <upstream>
```

## Browsing history

### Viewing the history
- Shows the list of modified files
```bash
git log --stat
```

- Shows the actual changes (patches)
```bash
git log --patch
```

### Filtering the history
- Shows the last 3 entries
```bash
git log -3
```

- Shows commits by author “Mosh”
```bash
git log --author="Mosh"
```

- Shows commits before 2020-08-17
```bash
git log --before="2020-08-17"
```

- Shows commits after “one week ago”
```bash
git log --after="one week ago"
```

- Shows commits with “GUI” in their message
```bash
git log --grep="GUI"
```

- Shows commits with “GUI” in their patches
```bash
git log -S"GUI"
```

- Shows range of commits between hash1 and hash2
```bash
git log hash1..hash2
```

- Shows commits that touched file.txt
```bash
git log file.txt
```

### Formatting the log output
- Custom log format with author and hash
```bash
git log --pretty=format:"%an committed %H"
```

### Creating an alias
- Creates a log alias for a one-line format
```bash
git config --global alias.lg "log --oneline"
```

### Viewing a commit
- Shows the commit HEAD2
```bash
git show HEAD2
```

- Shows the version of file1.txt in commit HEAD2
```bash
git show HEAD2
.txt
```

### Comparing commits
- Shows the changes between two commits
```bash
git diff HEAD~2 HEAD
```

- Shows changes to file.txt only between two commits
```bash
git diff HEAD~2 HEAD file.txt
```

### Checking out a commit
- Checks out the given commit
```bash
git checkout dad47ed
```

- Checks out the master branch
```bash
git checkout master
```

### Finding a bad commit
- Starts the bisect session
```bash
git bisect start
```

- Marks the current commit as a bad commit
```bash
git bisect bad
```

- Marks the given commit as a good commit
```bash
git bisect good ca49180
```

- Terminates the bisect session
```bash
git bisect reset
```

### Finding contributors
- Shows the contributor list
```bash
git shortlog
```

### Viewing the history of a file
- Shows the commits that touched file.txt
```bash
git log file.txt
```

- Shows statistics (the number of changes) for file.txt
```bash
git log --stat file.txt
```

- Shows the patches (changes) applied to file.txt
```bash
git log --patch file.txt
```

### Finding the author of lines
- Shows the author of each line in file.txt
```bash
git blame file.txt
```

### Tagging
- Tags the last commit as v1.0
```bash
git tag v1.0
```

- Tags an earlier commit
```bash
git tag v1.0 5e7a828
```

- Lists all the tags
```bash
git tag
```

- Deletes the given tag
```bash
git tag -d v1.0
```

## Rewriting History
### Undoing commits
- Removes the last commit, keeps changes staged
```bash
git reset --soft HEAD^
```

- Unstages the changes as well
```bash
git reset --mixed HEAD^
```

- Discards local changes
```bash
git reset --hard HEAD^
```

### Reverting commits
- Reverts the given commit
```bash
git revert 72856ea
```

- Reverts the last three commits
```bash
git revert HEAD~3..
```

- Reverts the last three commits without committing
```bash
git revert --no-commit HEAD~3..
```

### Recovering lost commits
- Shows the history of HEAD
```bash
git reflog
```

- Shows the history of bugfix pointer
```bash
git reflog show bugfix
```

### Amending the last commit
- Amend the last commit
```bash
git commit --amend
```

### Interactive rebasing
- Rebase interactively with the last five commits
```bash
git rebase -i HEAD~5
```
