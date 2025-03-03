# Comment

Comments that appear before top-level declarations, with no intervening newlines, are considered to document the declaration itself. These “doc comments” are the primary documentation for a given Go package or command.

```go
/*
multi-line comment
*/

func (p *Person /*in line comment*/) FullName() string {
	return p.FirstName + " " + p.LastName
}

// single line comment
```