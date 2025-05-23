In Go (Golang), clean code adheres to conventions that emphasize readability, simplicity, and maintainability. Naming conventions play a critical role in achieving these goals. Below are the key naming conventions for writing clean and idiomatic Go code:

---

The convention in Go is to use MixedCaps or mixedCaps rather than underscores to write multiword names.

---

## General Naming Principles
- **Be Descriptive but Concise**: Names should clearly convey the purpose of the variable, function, or type, but avoid being overly verbose.
  - ✅ `userID` (clear and concise)
  - ❌ `u` (too short and unclear)
  - ❌ `idOfTheUser` (too verbose)

- **Use CamelCase**: Go uses camel case for naming (e.g., `userID`, `GetUserInfo`). There is no underscore `_` in names unless it’s a constant or a test function.

- **Avoid Abbreviations**: Use full words unless the abbreviation is widely recognized (e.g., `URL`, `HTTP`, `ID`).
  - ✅ `userID`
  - ❌ `usrID`

- **Match the Context**: The name should reflect the entity's purpose and scope. For example:
  - Use `users` for a slice of users.
  - Use `user` for a single user object.

---

## Package Naming
- **Use Short, Lowercase Names**: Package names should be short, descriptive, and lowercase. Avoid underscores, dashes, or mixed case.
  - ✅ `math`, `http`, `json`
  - ❌ `Math`, `Http`, `my_package`

- **Avoid Redundancy**: Package names should not repeat the context of their usage. For example:
  - ✅ `import "auth"`
  - ❌ `import "auth/authentication"`

- **Name Imports Clearly**: When importing packages, avoid aliasing unless there’s a conflict or the alias improves clarity.
  - ✅ `import "math"`
  - ✅ `import m "math"` (only if necessary)

---

## Variable Naming
- **Use Short Names for Short Scopes**: For variables with limited scope (e.g., loop variables), single-letter names are acceptable (`i`, `j`, `v`, etc.).
  - ✅ `for i := 0; i < n; i++ { ... }`
  - ✅ `v := user.Name`

- **Use Descriptive Names for Longer Scopes**: For variables with broader scope, use descriptive names.
  - ✅ `userID := 123`
  - ❌ `id := 123` (unclear in a larger scope)

- **Avoid Stuttering**: Do not repeat the package name in variable names.
  - ✅ `user := auth.User{}`
  - ❌ `authUser := auth.User{}`

---

## Function Naming
- **Use Verbs for Actions**: Function names should describe the action they perform.
  - ✅ `GetUser()`, `SaveFile()`, `CalculateSum()`
  - ❌ `User()`, `File()`, `Sum()`

- **Avoid Redundancy**: The function name should not repeat the package name or type unnecessarily.
  - ✅ `func (u *User) Save()`
  - ❌ `func (u *User) SaveUser()`

- **Exported Functions**: Use PascalCase for exported functions (public functions).
  - ✅ `func GetUser()`
  - ❌ `func getUser()`

- **Unexported Functions**: Use camelCase for unexported functions (private functions).
  - ✅ `func getUser()`
  - ❌ `func GetUser()`

---

## Constant Naming
- **Use UpperCamelCase for Exported Constants**: For constants that are exported, use PascalCase.
  - ✅ `const MaxRetries = 3`
  - ❌ `const maxRetries = 3`

- **Use ALL_CAPS for Unchanging Values**: For unexported constants or values that represent configuration or environment variables, use all caps with underscores.
  - ✅ `const API_KEY = "12345"`
  - ✅ `const MAX_RETRIES = 3`

---

## Struct and Interface Naming
- **Use Nouns for Structs**: Struct names should be nouns that describe the entity they represent.
  - ✅ `type User struct`
  - ❌ `type DoSomething struct`

- **Use Adjectives or Descriptive Phrases for Interfaces**: Interface names should describe the behavior they represent, often ending in `-er` or `-able`.
  - ✅ `type Reader interface`
  - ✅ `type Stringer interface`
  - ❌ `type Data interface`

- **Avoid "I" Prefix for Interfaces**: Do not prefix interface names with `I` (e.g., `IReader`), as Go does not use this convention.

---

## Test Function Naming
- **Use `Test` Prefix**: Test function names must start with `Test` followed by the function or behavior being tested.
  - ✅ `func TestAddNumbers(t *testing.T)`
  - ❌ `func AddNumbersTest(t *testing.T)`

- **Use Snake Case for Subtests**: Use underscores in subtest names for clarity.
  - ✅ `t.Run("empty_input", func(t *testing.T) { ... })`

---

## Error Naming
- **Use `Err` Prefix for Error Variables**: Error variables should start with `Err` and describe the issue.
  - ✅ `var ErrNotFound = errors.New("not found")`
  - ❌ `var NotFoundError = errors.New("not found")`

- **Descriptive Error Messages**: Error messages should be clear and concise.
  - ✅ `return fmt.Errorf("user %d not found", userID)`
  - ❌ `return fmt.Errorf("error in user retrieval")`

---

## Receiver Naming
- **Use Short, Meaningful Names**: For methods on structs, use a short, meaningful name for the receiver (often one or two letters).
  - ✅ `func (u *User) Save()`
  - ✅ `func (c *Config) Load()`
  - ❌ `func (this *User) Save()`

- **Avoid Generic Names**: Avoid using generic names like `this` or `self`.

---

## File Naming
- **snake case**: File names should be all lowercase with underscores.
  - ❌ `user.go`
  - ✅ `user_handler.go`

---

## Setters and Getters

If you have a field called owner (lower case, unexported), the getter method should be called Owner (upper case, exported), not GetOwner. The use of upper-case names for export provides the hook to discriminate the field from the method. A setter function, if needed, will likely be called SetOwner. Both names read well in practice
```go
owner := obj.Owner()
if owner != user {
    obj.SetOwner(user)
}
```
---

## interface name
By convention, one-method interfaces are named by the **method name plus an -er suffix** or similar modification to construct an agent noun: *Reader, Writer, Formatter, CloseNotifier* etc.

To avoid confusion, *if your type implements a method with the same meaning as a method on a well-known type, give it the same name and signature*; **call your string-converter method String not ToString**.

---
## Redeclaration and reassignment
```go
f, err := os.Open(name)
```
This statement declares two variables, f and err. A few lines later, the call to f.Stat reads,
```go
d, err := f.Stat()
```
which looks as if it declares d and err. Notice, though, that err appears in both statements. This duplication is legal: **err is declared by the first statement, but only re-assigned in the second. This means that the call to f.Stat uses the existing err variable declared above, and just gives it a new value**.

In a := declaration a variable v may appear even if it has already been declared, provided:

- this declaration is in the same scope as the existing declaration of v (if v is already declared in an outer scope, the declaration will create a new variable §),
- the corresponding value in the initialization is assignable to v, and there is at least one other variable that is created by the declaration.
> This unusual property is pure pragmatism, making it easy to use a single err value, for example, in a long if-else chain. You'll see it used often.
