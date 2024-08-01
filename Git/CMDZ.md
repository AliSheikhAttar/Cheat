# CMDZ

## pull directory of repo
```bash
git init
git remote add [REMOTE_NAME] [GIT_URL]
git fetch REMOTE_NAME
git checkout REMOTE_NAME/BRANCH -- path/to/directory
```
- Description
When used together, these commands allow you to efficiently pull a specific directory from a remote repository without cloning the entire repository:

1. Initialize a Git repository in your current directory to prepare it for version control.
2. Add a remote repository reference to link your local repository to the remote one.
3. Fetch the latest data from the remote repository to ensure you have the most recent state.
4. Check out a specific directory from a specific branch in the remote repository, bringing only that directory into your local repository.