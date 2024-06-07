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


## vim
- insert - i
- normal - ESC 
- command - :
### normal
- u : undo
- cntrl + r : redo
- y+y : copy the line
- d + d : cut the line
- y + G : copy till end of the file
- y + gg : copy till start of the file
- p : paste the line down
- shift + p : paste in the above
- r + <char> : replace
- x : delete char
- d + 0 : delete till start of line
- d + $ : delete till end of line
- b : go to start of word / prev
- w : go to start of word / after
- e : go to end of word / prev
- shift+e : end of line
- <n ex:20> e : <n> prev word
- o : new line 
- shift + o : new line above
- 0 : start of line down
- $ : end of line
- g + g: start of file 
- shift + g : end of file
- <n> + shift + g : go to line <n>
- '*'*<n> : go to <n>next occurence/s
- '#'*<n> : go to prev <n>occurence/s
- /<string> + shift+n/n : find the prev/next occurence 
### command 
- set number : lines numbered
- w : save
- q : quit
- wq : w & q
- q! : quit without save
- qa : quit all open buffers and exit Vim. It closes all open files and terminates the Vim session. If there are unsaved changes in any of the buffers, Vim will prompt you to save or discard those changes before quitting.
- install clipboard: `sudo apt-get install vim-gtk3`


## Unzip
- unzip tar files
```bash
tar -xvzf <archive>
```
  - The -x flag is used to extract the content of the archive.
  - The -v flag is used to output the list of files being extracted.
  - The -z flag is used to decompress the file using gzip.
  - The -f flag is used to specify the path of the archive file.
  - archive is the path to the tar.gz file you want to unzip.
- unzip
```bash
unzip 'zip/rar file'
``` 

## Find

```bash
find options starting/path expression
```
  - options
  - -O1	(Default) -> filter based on file name first.
  - -O2	-> File name first, then file type.
  - -O3	-> Allow find to automatically re-order the search based on efficient use of resources and likelihood of success.
  - -maxdepth X ->	Search current directory as well as all sub-directories at most X levels deep.
  - -mindepth X ->	Search current directory as well as all sub-directories at least X levels deep.
  - -iname ->	Search without regard for text case(not case sensitive).
  - -name -> with name ...
  - -not ->	Return only results that do not match the test case.
  - -type f ->	Search for files.
  - -type d ->	Search for directories.
  - -empty -> empty directories
  - -not -empty -> not empty directories
  

- Find a File in Linux by last modified Time; returns files modified in the last <days> days
```bash
find <directory> -name <name or expression> -mtime -<days>
find </> -name <"*conf"> -mtime -<7>
find </home/exampleuser/> -name <"*conf"> -mtime -<3>
```

- Delete the results
```bash
find . -name <"*.bak"> -delete
```

- show files with their contents
```bash
find / -name "*.log" | less
```

- show top <n> files 
```bash
find / -name "*.log" | head -n <n>
```
- specify depth
```bash
find . -maxdepth <2> -name <"name">
```
- Find based on size
  - files with 100bytes size
  ```bash
  find . -type f -size 100c 
  ```
  - all files that have less than 1M size
  ```bash
  find . -size -1M
  ```
  - files have sizes between 1 and 20 M
  ```bash
  find . -size +1M -size -20
  ```
  - all files that have more than 1M size
  ```bash
  find . -type f -size +1M 
  ```
  c ⇒ byte

  k ⇒ KB

  M ⇒ MB

  G ⇒GB

- execute post process : -exec <command> <placeholder for outputs> <endof command args: (; or +)> 
';' execute process on each result and feth the next result but '+' fetch all result and execute on all of them 
  - ask and delete each founded files
  ```bash
  find . -name "*.txt" -exec rm -i {} \;
  ```
  - find string in lines of founded files => find and execute at each step
  ```bash
  find . -name "*.txt" -exec grep string {} \;
  ```
  - find string in lines of founded files => find at once and execute all
  ```bash
  find . -name "*.txt" -exec grep string {} +
  ```
  -  ';' takes more resource than '+' because of number of process steps
  - print the founded files
  ```bash
  find . -type f -name "name" -print
  ```
  - delete the founded files
  ```bash
  find . -type f -name "name" -delete
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


## Directories & files

- show all directories and files of current directory as tree structure 
```bash
tree "Directory name"
```

- Current Absolute path
```bash
pwd
```
- Move to home : /home/<USERNAME>
```bash
cd ~
```
- Move to root
```bash
cd /
```

- direcories & files
```bash
  ls [option] <option>
```
  - -a : list all files including hidden file starting with '.'
  - --color	: colored list [=always/never/auto]
  - -d : list directories - with ' */'
  - -F : add one char of */=>@| to enteries
  - -i : list file's inode index number
  - -l : list with long format - show permissions
  - -la: list long format including hidden files
  - -lh: list long format with readable file size
  - -ls: list with long format with file size
  - -r : list in reverse order
  - -R : list recursively directory tree
  - -s : list file size
  - -S : sort by file size
  - -t : sort by time & date
  - -X : sort by extension name 
  - -h : more human
  - -ltha : with full details


- Create all path
```bash
mkdir -p "a"/"inside_a"
```
- Create files
```bash
touch "a.txt" "b.txt" ...
```
- delete file
```bash
rm "a.txt"
```

- Create multi-dirs
  - ```bash
  mkdir "test{1..5}"
  ```

  - ```bash
  mkdir "test"/{'D', 'Q', 'P'}
  ```

- delete all path(empty directories)
```bash
rmdir -p "a"/"inside_a"
```
- delete everything in folder
```bash
rm -rf "a"
```

- Copy file and past as file in another directory
  - ```bash
  cp "a.txt" "test"/"b.txt"
  ```

  - ```bash
  cp "source/a.txt" "dest/b.txt"
  ```
- Copy directory by contents into another directory
  - ```bash
  cp -r "source/" "test/dest"
  ```

  - ```bash
  cp -r "source/" "source.copy/"
  ```

- Writes the details of copy to the copy_result.txt
```bash
cp -v "source/" "source.copy/" > copy_result.txt
```

- Cut file from Dir to another Dir
```bash
mv "source/file" "dest/"
```
- Rename files
```bash
mv "old_name" "new_name"
```
- Rename folders
```bash
mv "old_dir_name/" "new_dir_name/"
```
- Delete empty file
```bash
rm "test/a.txt"
```

- Delete non-empty directory
```bash
rm -r "test/"
```
- File type and info
```bash
file [option] <file>
```
  - b
  only type

- disk storage usage by directories and files
```bash
du [option] <directory>
```
  - -h : human
  - -s : summery
  - -a : all directories & files
  - -c : total
  - --time : last access time

## Content of file

```bash
cat <file> [option]
```
  - none : show the contents of the file in the console
  - -n : show the contents of the file in the console line by line
  - -b : show the contents of the file line by line but ignore empty lines\

- over writes text into file. write our text and ctrl +D.
```bash
cat > <file>
```
- concatenate files into a file
```bash
cat "file1.txt" "file2.txt" "file3.txt" > "file4.txt"
```
- Concatenate files text alphabetically (based on text in each file) into a file
```bash
cat "file1.txt" "file2.txt" "file3.txt" | sort > "file4.txt"
```
- append lines of a text into a file
```bash
cat "file5.txt" >> "file4.txt"
```
- Append text into file. write our text and ctrl +D.
```bash
cat >> "a.txt"
```


- show the contents of the file
```bash
more <"filename">
```
```bash
less [option] <"filename">
```
  `more +50 sample.txt` - show 50th line and more
  after open file:
  - [option] = -N => lines number
  - [option] = -s => skipping empty lines (print one for consequtive empty lines)
  - enter => next line
  - = => We can see the content of the current line number
  - space => next page
  - ctrl+b => Previous page
  - q => exit from more and back to terminal
  - g => go to first page
  - g + shift => go to last page
  - :<number> + enter => goes to the next <number> lines


- show first 10 lines
```bash
head <"filename">
```
- show last 10 lines
```bash
tail <"filename">
```
- show last/first <n> lines
```bash
tail/head -n <n>  <"filename">
```
- show last/first <c> characters
```bash
tail/head -c <n> <"filename">
```
- show from <n>th line till end
```bash
tail +<n> <"filename">
```

- first we open file with cat then we take first 50 lines, after that we select line 20 to the end of file.(lines 20-50 selected)
```bash
cat <"filename"> | head -50 | tail +20
```

- show characters of each line
```bash
cut [option] <filename> 
```
- notes

> N => N'th byte, character or field, counted from 1
> N- => from N'th byte, character or field, to end of line
> N-M => from N'th to M'th (included) byte, character or field
> -M => from first to M'th (included) byte, character or field

- options
  - -b --bytes=LIST
        select only these bytes
  - -c, --characters=LIST
        select only these characters

  - -d, --delimiter=DELIM
        use DELIM instead of TAB for field delimiter

  - -f, --fields=LIST
        select only these fields;  also print any line that contains no
        delimiter character, unless the -s option is specified

  - --complement
        complement the set of selected bytes, characters or fields

  - -s, --only-delimited
        do not print lines not containing delimiters

  - --output-delimiter=STRING
        use  STRING  as  the output delimiter the default is to use the
        input delimiter

  - -z, --zero-terminated
        line delimiter is NUL, not newline

- Ex. of cut
```bash
cut -d "," -f 1,4 chocolate.txt "seperates by ',' then cut columns 1 and 4"
cat chocolate.txt | head -n 20 | cut -d "," -f 1,4 "seperates by ',' then cut columns 1 and 4 of the first 20 lines"
cat chocolate.txt | head -n 20 | cut -d "," -f 1,4 --output-delimiter='*' "seperates by ',' then cut columns 1 and 4 of the first 20 lines and replace ',' with '*'"
```
- show in table format
```bash
table <filename>
```
- file content info
```bash
wc [option] <"filename"> 
```
- output: number1 number2 number3 filename
number1 = count of lines , number 2 = count of words , number3 = count of characters
- -l => only show count of lines
- -w => only show count of words
- -m => only show count of characters
- -c => only show count of bytes


- ouput without file name
```bash
cat wc-file | wc
```
## Sort

- show first 10 lines
```bash
sort <<EOF
HELLO
hello
h2llo
Bye
bye
1-bye
EOF
```
- sort reverse
```bash
sort -r <<EOF => reverse
```
- sort numbers
```bash
sort -n <<EOF => sort numbers
```
- sort by column <m>
```bash
sort -k <m = 2> -n <<EOF
ali    1
reza    8
mammad    5
arshia    7
soltan    10
EOF
```
- output:
ali     1
mammad  5
arshia  7
reza    8
soltan  10

## grep

Example:

```bash
cat <<EOF > "filename"
We all love linux,
and its very strong in
doing things
we're learning it in
quera college
finished!
EOF
```
- looking for <string> in <filename>
```bash
grep <string> "filename"
```
- print lines that contains “we”.(case sensitive)
```bash
grep we "filename"
```
print lines that contains “we”.(not case sensitive)
```bash
grep -i we "filename"
```

- match
```bash
grep <in> "filename"
```

- match whole word - first of string or preceded by non-word
```bash
grep -w <in> "filename"
```

- match whole word
```bash
grep -x <in> "filename"
```
- print lines that doesn’t contain string 
```bash
grep -v string "filename"
```
- count of lines that contain string
```bash
grep -cw string "filename" 
```
- show lines that contain string and the number of that line and write in out.txt. 
```bash
grep -in string "filename" > out.txt
```

- Regex(*Regular Expression):*
- find words that start with “l” and end with “x” and anything between them .
```bash
grep -E "l[a-z]*x" quera-file
```
- multiple cases
```bash
grep -e pattern1 -e pattern2 -e pattern3 <filename>
```
```bash
grep -E 'pattern1|pattern2' <filename>
```
- <n> lines above and n lines under
```bash
-C <n> 
```
- with lines numbers
```bash
-n
``` 
## Wildcards

- “ * ”  ⇒ It means zero or more of each character.

- “ ? ” ⇒ It means there is only one number of each character.

- “ [ ] ” ⇒ It means there is only one number of the characters provided inside the brackets.

- [! ] or [^ ] (Negation) -> Matches any one character NOT specified within the brackets.
Example: [^0-9]* matches any filename that doesn't start with a digit.

- start (any of a, b, d, c, i, o) after l and before s
```bash
ls -lha l[abdcio]st.sh
```

***brace expansion***
- create a1, a2, ... a200
```bash
touch a{1..200}.txt
```
- print 01, 02, ..., 20
```bash
echo {01..20}
```

- -n: not to append a newline character at the end of the output.
```bash
echo -n "\$word "
```
- -e: characters that come after \ as special chars
ex: \r in text means the new line to echo be echoed in the first(previous line) and replace the previous chars
if the lenght is less than the previous one the old remaining chars remain

## Compression & archive

- Compresses the file delete the main file save it as filename.gz and we can’t open it
```bash
gzip "filename"
```
- Decompress
```bash
gunzip "filename.gz"
```
- Zip
```bash
bzip2 "filename"
```
- Unzip
```bash
bunzip2 "filename.bz2"
```
> bzip2 takes more time while compresses more efficiently means the compressed file would have less volume
- Archive

```bash
tar -cvf archive.tar file{3..10} folder{1..2}
```
  - -c => determines we want to archive
  - -x => determines we want to unarchive
  - -v => output the process result
  - -f => archive name
  - -r => add files and directories to existing archive file without unarchiving it

- see inside archive without open it
```bash
tar -tf archive.tar
```

after we archived our files and folders now we can compress it.

```bash
gzip archive.tar
```
- unarchive
```bash
gunzip archive.tar.gz
tar -xvf archive.tar
```

- archive and compress
```bash
tar -zcvf archive.tar.gz file{3..10} folder{1..2}
```
- decompress and unarchive
```bash
tar -zxvf archive.tar.gz
```

## awk
- process table structured texts
```bash
awk '{action}' <my_file>
```
text = 
FirstName    LastName    Country

Alirof    Shamsky    Earth
Arshatof    Akhamsky    Jupiter
Aliof    Bamsky    Pluto
Ali    Daei    Seimare River

- print <n-th> column
```bash
awk '{print $n}' awk_file.txt
```
- print column 1 and 2
```bash
awk '{print $1, $2}' awk_file.txt
```
- print the last column
```bash
awk '{print $NF}' awk_file.txt
```
- REGEX returns the rows which contains the regex pattern in them
```bash
awk '/regex pattern/{action}' my_file
```
- print the column 1 and 3 of those which contains pattern "of" in them
```bash
awk '/of/{print $1, $3}' awk_file.txt
```
output = Alirof Earth
Arshatof Jupiter
Aliof Pluto

- seperate the columns based on character <c>
```bash
awk -F\<c> '{print $1" "$2" "$3}' data.txt
```
ali-10-20
bahram-65-33
danial-44-55
```bash
awk -F\- '{print $1" "$2" "$3}' data.txt
```
- show without empty lines
```bash
awk 'NF' <sample.txt> 
```

```bash 
awk -F ',' -v kw="$keyword" 'BEGIN{OFS=","} $3 ~ kw {print FNR" | "$1" | "$2" | "$3}' tasks.csv
awk -v task_id="$task_id" -F ',' 'BEGIN {OFS = FS} 
                NR == task_id {$1 = 1} {print}' tasks.csv > tasks.tmp && mv tasks.tmp tasks.csv
```

- -v : declare variable
- begin : runs before processing
- OFS : output delimiter
- FS : input delimiter
- FNR processed line in current file
- NR processed line in all files
- int1 == int2 {expression1} ... {expression n} : numerical equality
- str1 ~ str2 {expression1} ... {expression n} : is used to match a variable against a regular expression.
- > tasks.tmp && mv tasks.tmp tasks.csv : if awk command was ok then replace the result