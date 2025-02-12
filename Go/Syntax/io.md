# Input Output

## Print to terminal
```go
import "fmt"
fmt.Printf()
fmt.Println()

// int
fmt.Printf("%d",10)

// string/rune
fmt.Printf("String %s, Char %s", "hello", 'a')

// utf-8 encoded 
for pos, char := range "日本\x80語" { // \x80 is an illegal UTF-8 encoding
    fmt.Printf("character %#U starts at byte position %d\n", char, pos)
}
// output
// character U+65E5 '日' starts at byte position 0
// character U+672C '本' starts at byte position 3
// character U+FFFD '�' starts at byte position 6
// character U+8A9E '語' starts at byte position 7

// type and value
var in interface{}
	fmt.Printf("Type: %T, Value: %v \n",in, in)

```