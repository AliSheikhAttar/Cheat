# Scripting

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