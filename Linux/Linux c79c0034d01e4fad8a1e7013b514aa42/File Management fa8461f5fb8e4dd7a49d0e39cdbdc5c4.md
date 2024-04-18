# File Management
- enable AppImage files to run
```bash
chmod +x ./*.AppImage
```
- run AppImage file
```bash
./<x>.AppImage
```
- mv multiple Files
 ```bash
 mkdir Micro; for i in {0..10}; do mv ../Downloads/"AVR Microcontroller$i.pdf" ./Micro; done
```

- unzip tar files
```bash
tar -xvzf <archive>
```
  - The -x flag is used to extract the content of the archive.
  - The -v flag is used to output the list of files being extracted.
  - The -z flag is used to decompress the file using gzip.
  - The -f flag is used to specify the path of the archive file.
  - archive is the path to the tar.gz file you want to unzip.
  
- the umask acts as a filter to remove certain permissions from the default permission set. It helps enforce security policies by restricting the default access granted to newly created files and directories.
```bash
umask <value ex. 777>
```

- Current Absolute path
```bash
pwd
```

- Move to root
```bash
cd ~
```

- Run command inside a file
    - ```bash
        . / <file.txt>
      ```
    - ```bash
        bash <file.txt>
      ```
    - ```bash
        sh <file.txt>
      ```

- Find files
```bash
find options starting/path expression
```
  - options
  - -O1	(Default) -> filter based on file name first.
  - -O2	-> File name first, then file type.
  - -O3	-> Allow find to automatically re-order the search based on efficient use of resources and likelihood of success.
  - -maxdepth X ->	Search current directory as well as all sub-directories X levels deep.
  - -iname ->	Search without regard for text case.
  - -not ->	Return only results that do not match the test case.
  - -type f ->	Search for files.
  - -type d ->	Search for directories.

- Find a File in Linux by last modified Time; returns files modified in the last <days> days
```bash
find <directory> -name <name or expression> -mtime -<days>
find </> -name <"*conf"> -mtime -<7>
find </home/exampleuser/> -name <"*conf"> -mtime -<3>
```
- Find a File in Linux Based on Content
The find command can only filter the directory hierarchy based on a file’s name and metadata. If you need to search based on the file’s content, use a tool like grep. Consider the following example:
```bash 
find . -type <f> -exec grep <"example"> '{}' \; -print
```
find . -type f -exec grep "example" '{}' \; -print
This searches every object in the current directory hierarchy (.) that is a file (-type f) and then runs the command grep "example" for every file that satisfies the conditions. The files that match are printed on the screen (-print). The curly braces ({}) are a placeholder for the find match results. The {} are enclosed in single quotes (') to avoid handing grep a malformed file name. The -exec command is terminated with a semicolon (;), which should be escaped (\;) to avoid interpretation by the shel


- Find and Process a File in Linux; -exec option runs commands against every object that matches the find expression. Consider the following example:
```bash
find . -name "rc.conf" -exec chmod o+r '{}' \;
```
This filters every object in the current hierarchy (.) for files named rc.conf and runs the chmod o+r command to modify the find results’ file permissions.

The commands run with the -exec are executed in the find process’s root directory. Use -execdir to perform the specified command in the directory where the match resides. This may alleviate security concerns and produce a more desirable performance for some operations.

The -exec or -execdir options run without further prompts. If you prefer to be prompted before action is taken, replace -exec with -ok or -execdir with -okdir


- Delete the results
```bash
find . -name <"*.bak"> -delete
```

```bash
ls -t
```

```bash
ls -l
```

```bash
ls -r
```

```bash
ls -h
```

```bash
ls -R
```

```bash
ls -l -t
```

```bash
ls -lh "path"
```

```bash
mkdir -p "a"/"inside_a"
```

```bash
mkdir "test{1..5}"
```

```bash
mkdir "test"/{'D', 'Q', 'P'}
```

```bash
rmdir -p "a"/"inside_a"
```

```bash
rm -rf "a"
```

```bash
touch "a.txt" "b.txt" ...
```

```bash
rm "a.txt"
```

```bash
cat "a.txt"
```

```bash
cat -n "a.txt"
```

```bash
cat -b "a.txt"
```

- type into the file
```bash
cat > <file>
```

```bash
cat "file1.txt" "file2.txt" "file3.txt" > "file4.txt"
```

```bash
cat "file1.txt" "file2.txt" "file3.txt" | sort > "file4.txt"
```

```bash
cat "file5.txt" >> "file4.txt"
```

```bash
cat >> "a.txt"
```

```bash
cp "a.txt" "test"/"b.txt"
```

```bash
cp "source/a.txt" "dest/b.txt"
```

```bash
cp -r "source/" "test/dest"
```

```bash
cp -r "source/" "source.copy/"
```

```bash
cp -v "source/" "source.copy/" > copy_result.txt
```

```bash
mv "source/file" "dest/"
```

```bash
mv "old_name" "new_name"
```

```bash
mv "old_dir_name/" "new_dir_name/"
```

```bash
rm "test/a.txt"
```

```bash
rm -r "test/"
```

```bash
ls --help
```

```bash
info ls
```

```bash
man ls
```
