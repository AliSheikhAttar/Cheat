In modern C++, using `auto` instead of explicitly specifying the type (like `int`) generally has **no performance impact** at runtime.  The compiler deduces the type at compile time, and the resulting compiled code is usually identical (or very nearly so) to what it would be if you had written the type explicitly.

Here's a breakdown:

1. **Compile-Time Deduction:** `auto` is a compile-time feature.  The compiler analyzes the code and figures out the actual type of the variable based on its initializer.  This deduction happens during compilation, not when the program is running.

2. **No Runtime Overhead:** Once the compiler has determined the type, it generates the same machine code as if you had written the type explicitly.  There's no extra work or lookup required at runtime to determine the type.

3. **Potential for Optimization:** In some (rare) cases, `auto` can even *help* the compiler optimize the code slightly better.  This is because the compiler might have more information about the type than you explicitly provide (especially with template code or complex expressions).  However, this is usually a very minor optimization and not something you should rely on.

4. **Example:**

   ```c++
   auto x = 10; // The compiler deduces that x is an int
   int y = 10;  // Same as above (in terms of runtime performance)

   auto z = 3.14; // The compiler deduces that z is a double
   double w = 3.14; // Same as above (in terms of runtime performance)
   ```

   The compiled code for the `auto` versions will be essentially the same as the code for the explicitly typed versions.

**When to use `auto`:**

*   **Readability:** `auto` can make code more concise and easier to read, especially when dealing with complex types (e.g., iterators, template types).
*   **Maintainability:** If the type of a variable might change in the future, using `auto` can make it easier to update the code without having to change the type declaration in multiple places.
*   **Type deduction with templates:**  `auto` is essential when working with templates, as the exact type might not be known until the template is instantiated.

**When to avoid `auto`:**

*   **Clarity:** In some cases, explicitly writing the type can improve code clarity, especially for simple types like `int` or `bool`.  If using `auto` makes the code harder to understand, it's better to be explicit.
*   **Type promotion/conversion:** Be mindful of type promotion and conversion when using `auto`.  Sometimes, the deduced type might not be what you expect, especially with mixed-type arithmetic.  In these cases, explicit casts might be necessary.

**In summary:** Using `auto` is generally a good practice in modern C++.  It doesn't make your code slower at runtime and can improve readability and maintainability.  Just be sure to use it judiciously and consider the potential impact on code clarity.  Don't be afraid to use explicit types when they make the code easier to understand.
