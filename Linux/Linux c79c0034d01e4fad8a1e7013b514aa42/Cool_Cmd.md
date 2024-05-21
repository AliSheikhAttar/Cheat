# Coolz

* At most, we want to view the file sample.txt with line numbers and in a way that all consecutive empty lines are collapsed into one. For example, if you view the contents of the file sample.txt normally, the first 5 lines will be as follows:

This sample is based hugely on the original sample.txt produced

> I used the following options to convert this document:
>  
> We want the above output to be transformed into the following output:


>  1 This sample is based hugely on the original sample.txt produced
>  2
>  5 I used the following options to convert this document:
```bash
less -N sample.txt | awk 'BEGIN {empty=0} /^$/ { if (++empty < 2) print; } !/^$/ {empty=0; print;}'
```
`/^$/` - the line is empty
`!/^$/` - the line is not empty


* Find for windows linux and kill in data.txt and print their two above and under lines and their lines number no case-sensitive
```bash
grep -e windows -e linux -e kill data.txt -C 2 -n -i > clues
```
* find directories at depth at least 1 and max 2 from current directory with name Image
```bash
find . -type d -name 'Image' -mindepth 1 -maxdepth 2
```