# Standard Stream

- stdin    = Standard Stream Input   0  (Input to processer)
- stdout = Standard Stream Output 1 (Output from processer)
- stderr  = Standard Stream Error     2 (Error from Processer)

![Screenshot 2024-02-13 153251.png](Standard%20Stream%203e15e4dd7ff74cbd8a94ba5b39710fd1/Screenshot_2024-02-13_153251.png)

## Redirecting streams
### Output
```bash
command -options arguments 1> destination
command -options arguments > destination
```
### Input
```bash
command -options arguments 0< input_source
command -options arguments < input_source
```
### Error
```bash
command -options arguments 2> destination
```
### Output & Error
```bash
command -options arguments 1> output_destination 2> error_destination
```

```bash
wc < file-new.txt
```

```bash
command << MARKER
data
MARKER
```

```bash
wc << EOF
hello world
linux is gooood
bye
EOF
```

```bash
cat <<EOF > data.txt
hello guys
linux is so powerful
goodbye
EOF
```

## Pipline

![Screenshot 2024-02-15 131901.png](Standard%20Stream%203e15e4dd7ff74cbd8a94ba5b39710fd1/Screenshot_2024-02-15_131901.png)

command1 | command2 | command3 | ... | commandn

Stdin → Command1 → Command2 → Command3 → Command4 → stdout

```bash
cat <<EOF | sort
hello
from
alireza
in quera
to
you
EOF
```

```
Output : 

alireza
from
hello
in quera
to
you
```

```bash
echo "My account name is $(whoami)."
```

Output = My account  name is ASA