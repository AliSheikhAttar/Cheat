# Script

## Creating
```bash
cat << EOF > script.script
#! /usr/bin/python3
#! /bin/bash
print("hello world!")
echo hello world
EOF
chmod +x script.script
```

## Variables and Arguments

* $0 => name of running script
* $1 - $9 => first nine arguments of script
* $# => number of all arguments
* $* => all arguments as a single string separated by spaces
* $@ => all arguments as an array
* $? => exit code of the last executed process
* $$ => process ID of this script
* $! => process ID of the last background process

- " " instead of variable wihtout use 

```bash
target=quera
echo hello $target #prints hello quera in the terminal
echo hello target  #prints hello target in the terminal
```
```bash
#! /bin/bash
echo "$1 says hello to $2."
```

```bash
./hello.sh arghavan kavus 
# arghavan says hello to kavus.
```

```bash
# gouss law
for i in {0..10}
do
  sum=$((sum+i))
done

echo sum of first 10 integers are: $sum
echo sum of first 10 integers are: $(((10+0)*11/2))
```

```bash
#! /bin/bash
echo "addition of your two numbers are $(($1+$2))"
echo "subtraction of your two numbers are $(($1-$2))"
echo "multiplication of your two numbers are $(($1*$2))"
echo "division of your two numbers are $(($1/$2))"
```
- use output of another function
```bash
./hello.sh $(whoami) ali
```
### shift
```bash

OPTION1=false # Boolean Option with default value
OPTION2=hello # Parameter Option with default value

while [ -n \$1 ]
do
    case $\1 in
        -o1) echo "OPTION1 entered"
             OPTION1=true
             shift ;;

        -o2 | --option2) echo "OPTION2 entered"
             if [ -z \$2 ]; then
                 echo "Option2 needs a parameter"
                 exit 1 # exit with exit code 1
             fi
             OPTION2=\$2
             shift
             shift ;;

         --) shift
             break ;;

          *) echo "\$1 is not an Option"
             exit 1 ;;
    esac
done
echo "Option1: \$OPTION1, Option2: \$OPTION2"
count=1
while [ -n \$1 ]
do
    echo "Parameter #\$count = \$1"
    count=\$[ \$count + 1 ]
    shift
done
# inputs 
bash options.sh -o1 -o2 bye -- Alireza ArshiA SAliB
bash options.sh -o1 --option2 bye -- Alireza ArshiA SAliB
# outputs 
OPTION1 entered
OPTION2 entered
Option1: true, Option2: bye
Parameter #1 = Alireza
Parameter #2 = ArshiA
Parameter #3 = SAliB 
```

## Array

```bash
#! /bin/bash

a1=(1 2 3 4 5 6 7)      # space seperated values

declare -a a2           # first make an empty array
a2+=(ArshiA Alireza)    # fill it with values
a2+=(SAliB)             # append some more values


echo ${a1[@]}           # print the whole array
echo ${a1[*]}           # print the whole array

echo ${a2[@]}           # print the whole array
echo ${a2[*]}           # print the whole array

echo ${a1[0]}           # arrays start at 0
echo ${a1[1]}
echo ${a2[-1]}          # you can use negetive index to index from the end

a1[0]=tahmures          # you can change an index value
a2[2]='+'               # array indices don't have to have the same type
a2[10]='not10'          # accessing an "out of range" index would result in an append!
echo ${a1[@]}
echo ${a2[@]}

echo "the array contains ${#a1[@]} elements" # total length
echo "the array contains ${#a2[@]} elements"

echo "${!a1[@]}" # all indices
echo "${!a2[@]}"

unset a1[1] # delete index
unset a1[3]

echo ${!a1[@]}          # index 1 and 3 are removed =>  0 2 4 5 6
echo ${#a1[@]}          # arrays size is decreased by 2 => 5
echo ${a1[@]}           # the values of those indices are lost too => 1 3 5 6 7
```

## Hash

```bash
declare -A hm

hm=([che]=shekufe [delnavaz]=riz [umadam]=umadam)
hm+=([amma]=amma [ba]=che [naz]=dir [umadam]=umadam)
hm[0]="kaqaz gheichi"
hm[1]="gheichi sang"
hm[2]="sang kaqaz"


echo ${!hm[@]}          # keys
echo ${hm[@]}           # values
# notice that "umadam" key appears once even though we defined it twice
# notice that the index orders are different from how we inserted them
echo ${#hm[@]} 
```

## Condition
- if argument is passed set the variable to argument value else set it to default value

```bash
commit_message=${1:-"new cheatz"}
```
### if else : condition == command => if exit code == 0 => execute
```bash
if command-1; then
    commands-1
elif command-2; then
    commands-2
...
elif command-n; then
    commands-n
else (optional)
    commands-else
fi            
```
#### case
```bash
case variable in
pattern-1) commands-1;;
pattern-2) commands-2;;
...
pattern-n) commands-n;;
*) default-commands;;
esac
```

### test

* options :
- -z INTEGER : is zero
- -n INTEGER : is bigger than zero
- -d FILE    : FILE exists and is a directory
- -e FILE    : FILE exists
- -f FILE    : FILE exists and is a regular file

- equality of numbers
```bash
if test \$num1 -eq \$num2 # if equal => exit code == 0
then
    echo "Equal Numbers: \$num1 == \$num2"
else
    echo "Not Equal Numbers: \$num1 != \$num2"
fi 
```
```bash
if [ \$num1 -eq \$num2 ] # if equal => exit code == 0
then
    echo "Equal Numbers: \$num1 == \$num2"
else
    echo "Not Equal Numbers: \$num1 != \$num2"
fi 
```
- logical expressions
```bash
if [ -z \$word1 ] && [ -n \$word2 ] 
then
   echo "here"
   echo "just word2=\$word2 is given"
elif [ -n \$word1 ] && [ -z \$word2 ]
then
    echo "just word1=\$word1 is given"
elif [ -n \$word1 ] && [ -n \$word2 ]
then
    echo "both word1=\$word1 and word2=\$word2 is given"
else
    echo "nothing given!"
fi
```
- calculator
```bash
var=$2

case $var in
  +) echo addition of your two numbers are $(($1 + $3));;
  -) echo subtraction of your two numbers are $(($1 - $3));;
  \x) echo multiplication of your two numbers are $(($1 * $3));;
  /) if [ $3 -ne 0 ]; then # if not equal zero
     echo division of your two numbers are $(($1 / $3));;
     fi
  *) echo "Invalid operator";;
esac
```
- backup
```bash
SRC=\$1
DST=\$2

if [ -z \$SRC ] || [ -z \$DST ]
then
    echo "Two Arguments needed"
    exit 1
fi

if [ -e \$SRC ]
then
    cp -rv \$SRC \$DST
    echo "Backup Seccussful"
else
    echo "Source Path not exists: \$SRC"
fi
```

## Loop
### for
```bash
for var in list
do
    commands
done
```
#### Manual
```bash
for word in "linux" "is" "perfect" "and" "windows?" "mmm," "not" "bad."
do
    echo -n \$word
done
echo
```

#### List
```bash
cat <<EOF > list
Linux
Changed
My
World!
EOF

#! /bin/bash
for word in \$(cat list)
do
    echo \$word
done

```

#### Folder
```bash
mkdir for3
cd for3
mkdir folder
touch folder/file{1..3}.{txt,png}
mkdir folder/sub-folder{1..2}


for word in $(pwd)/folder/*
do
    if [ -d \$word ]; then # its directory
        echo "\$word is a folder"
    elif [ -f \$word ]; then # its file
        echo "\$word is a file"
    fi
done

```
#### iterator
```bash
for (( i = 1; i <= 10; i++ ))
do
    echo "Round \$i"
done
```

### While
```bash
var=10
while [ \$var -gt 0 ]
do
    echo "Round \$var"
    var=\$[ \$var - 1 ]
done
```
```bash
break
continue
```