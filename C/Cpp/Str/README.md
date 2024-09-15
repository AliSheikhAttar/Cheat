# String

## C

- define
```C
char mystr[8] = "hello"
```

- length
```C 
strlen(str)
```

- copy string
```C
strcp(des_str, src_str)
```

- concatenate
```C
strcat(des_str, src_str)
```

- comparison
```C
strcmp(str1, str2) // => equal --> == 0 
```

## C++

- define
```Cpp
String my_str = "hello"
```

- length
```Cpp
str.length()
```

- concatenate
```Cpp
str.concat(str1)
```

- substring
```Cpp
str.substring(start_index, end_index)
```

- find character
```Cpp
str.indexOf(char)
```

- Access a particular character of the string.
```Cpp
char c = str.charAt(n);
char c = str[n];
```

- Appends the parameter to a string.
```Cpp
str.concat(parameter);
str = str + parameter;
```

- Tests whether or not a string ends with string2.
```Cpp
bool result = str.endsWith(string2);
```

- Compares two strings for equality (case sensitive).
```Cpp
bool isEqual = str.equals(string2);
bool isEqual = str == string2;
```

- Locates val in a string by searching forward starting from start index.
```Cpp
int index = str.indexOf(val, start);
```

- Locates val in a string by searching backward starting from start index.
```Cpp
int index = str.lastIndexOf(val, start);
```

- Returns the length of the string, in characters.
```Cpp
int len = str.length();
```

- Removes all characters (or count characters if given) from a string starting from the index.
```Cpp
str.remove(index, count);
```

- Replaces all instances of substring1 in a string with substring2.
```Cpp
str.replace(substring1, substring2);
```

- Sets a character to c at index of the string.
```Cpp
str.setCharAt(index, c);
```

- Tests whether or not a string starts with string2.
```Cpp
bool result = str.startsWith(string2);
```

- Gets a substring of a string, from inclusive to exclusive.
```Cpp
string sub = str.substring(from, to);
```

- Converts a valid string to an integer or float.
```Cpp
int num = str.toInt();
float num = str.toFloat();
```

- Get a lower-case or upper-case version of a string.
```Cpp
string lower = str.toLowerCase();
string upper = str.toUpperCase();
```

- Gets a version of the string with any leading and trailing whitespace removed.
```Cpp
string trimmed = str.trim();
```

- Input from serial
```C
Serial.readString()
```

- set timeout
```C 
Serial.setTimeout(200); // only waits 200 miliseconds after inputing to output rather than default 1000
```