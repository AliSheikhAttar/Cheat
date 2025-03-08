Let’s address your questions about memory allocation for arrays and slices in Go, as well as how slices behave when passed to functions.

### 1. **Memory Allocation: Arrays vs. Slices**

#### **Arrays**
When you create an array explicitly, such as `x := [4]int{}`, the memory allocation depends on the context:
- **Stack Allocation**: If the array is a local variable within a function and its size is fixed and known at compile time (like `[4]int`), Go typically allocates it on the **stack**. The stack is used because it’s fast and the array’s lifetime is tied to the function’s scope.
- **Heap Allocation**: However, if the array is large or if Go’s escape analysis determines that it might outlive the function (e.g., if you return it or store a pointer to it), the array is allocated on the **heap** instead. The heap is used for data that needs to persist beyond the function’s execution.

For example:
```go
func main() {
    x := [4]int{}  // Likely allocated on the stack
    fmt.Println(x)  // Outputs: [0 0 0 0]
}
```
Here, `x` is a local variable with a small, fixed size, so it’s typically on the stack. But if you wrote:
```go
func createArray() *[4]int {
    x := [4]int{}
    return &x  // Escapes to the heap
}
```
The array would be allocated on the heap because it escapes the function’s scope.

#### **Slices**
When you create a slice, like `y := []int{1, 2, 3, 4}`, the underlying array is **always allocated on the heap**. Slices are dynamic structures designed to grow or shrink, and their backing arrays need to be flexible. Allocating them on the heap ensures they can be managed (e.g., resized) without stack-related limitations.

For example:
```go
func main() {
    y := []int{1, 2, 3, 4}  // Backing array on the heap
    fmt.Println(y)          // Outputs: [1 2 3 4]
}
```

So, to answer your first question: When you create an array explicitly with `x := [4]int{}`, it is **not necessarily allocated on the heap**—it’s usually on the stack unless it escapes the function. In contrast, a slice’s underlying array is **always on the heap**.

---

### 2. **Passing Slices to Functions: Do Changes Affect the Original?**

Slices in Go are often described as “reference-like,” but let’s clarify what that means:
- A slice is a small data structure (a “slice header”) containing:
  - A **pointer** to the underlying array.
  - The **length** of the slice (number of elements it currently holds).
  - The **capacity** of the slice (total size of the underlying array).
- When you pass a slice to a function, Go passes a **copy of this slice header**. Because the copy includes the pointer to the underlying array, both the original slice and the copy in the function point to the **same underlying array**.

#### **Modifying Elements**
If you modify the elements of the slice within the function, it **does affect the original slice** because you’re altering the shared underlying array.

For example:
```go
func modifySlice(s []int) {
    s[0] = 100  // Modifies the underlying array
}

func main() {
    y := []int{1, 2, 3, 4}
    modifySlice(y)
    fmt.Println(y)  // Outputs: [100 2 3 4]
}
```
Here:
- `y` is passed to `modifySlice`, which gets a copy of the slice header.
- The copy’s pointer still points to the same underlying array as `y`.
- Changing `s[0]` modifies the underlying array, so `y` reflects the change.

#### **Modifying Length or Capacity**
However, if the function changes the **length** or **capacity** of the slice (e.g., by using `append`), the original slice **won’t be affected** unless the modified slice is returned and reassigned. This is because `append` might create a new underlying array if the current capacity is exceeded, and the original slice’s header isn’t updated unless explicitly reassigned.

For example:
```go
func appendToSlice(s []int) []int {
    s = append(s, 5)  // May create a new array if capacity is exceeded
    return s
}

func main() {
    y := []int{1, 2, 3, 4}
    y = appendToSlice(y)  // Reassign the returned slice
    fmt.Println(y)        // Outputs: [1 2 3 4 5]
}
```
If you didn’t reassign `y` (i.e., omitted `y =`), the original `y` would remain `[1 2 3 4]`, because the function’s local `s` would point to a new array after `append`.

---

### **Conclusion**
- **Array Allocation**: When you create an array like `x := [4]int{}`, it’s typically allocated on the **stack** unless it escapes to the heap (e.g., via a pointer or return). Slices, however, always have their underlying arrays on the **heap**.
- **Slices and Functions**: Since slices include a pointer to their underlying array, passing them to a function and modifying their elements **changes the original underlying array**, thus affecting the original slice. However, changes to the slice’s length or capacity (e.g., via `append`) only affect the original if the modified slice is returned and reassigned.

This behavior makes slices powerful for working with dynamic data while keeping memory management efficient in Go!