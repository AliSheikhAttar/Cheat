# Git 

## To revert multiple recent commits, you can specify a range, from oldest to newest. One new commit will be created for each reverted commit.
## will create a new commit doing the opposite of the one above
` git add .`
`git commit -m "This commit is a mistake"`
`git revert HEAD `

## revert the last three commits

`git revert HEAD~3...HEAD`

## Delete previous commits and revert to commit 

`git reset --hard HEAD~` 

## .gitignore

- ignore specific formats
*.<fileformat>

- ignore specific directories
<dir_name>                  