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
```bash
pwd
```

```bash
cd ~
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

```bash
cat > "a.txt"
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
