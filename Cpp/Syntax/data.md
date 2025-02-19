# Data structure

## cast
- cast to type
```cpp
long long res;
res = (long long)x * 2;
```
- safer/c++ casting
> without unexpected operation
```cpp
static_cast<double>(a)
```

## vector
```cpp
#include <vector>

// initialize
vector<int> numbers;

// initialize with size
int n = 100;
vector<int> numbers(n);

// access
numbers[i]

// access with bound checking
numbers.at(i)

// push data
numbers.push_back(data);

// push data, more efficient, constructing the object in the vector memory directly
numbers.emplace_back(data);
[more info]()

// remove value
numbers.pop_back(data);

// last element
numbers.back()

// empty
numbers.empty()

// remove at
numbers.erase(numbers.begin() + delIdx);

// swap
swap(numbers[i], numbers[j]);

// reserve memory (capacity), prevent reallocation, better performance
numbers.reserve(n)
[more info](./complementary/reserve.md);

// iterator the the begining of vector
std::vector<int>::iterator = numbers.begin()
*numbers.begin() // value

// iterator pointing one position past the last element
numbers.end()

// copy vectors
std::copy(numbers.begin() + left, numbers.begin() + right, a.begin() + left); 
// copy from index 0+left till (excluding) 0+right from numbers into a from index 0+left


//length
int len = numbers.size;
```

## tuple
```cpp
#include <tuple>

// Declare a tuple that can hold an int, a string, and a double.
std::tuple<int, std::string, double> myTuple;
// It's effectively: std::tuple<int, const char*, double> tuple1;  (note: "hello" is const char*)

// 2. Initialize using constructor syntax:
std::tuple<int, std::string, double> tuple2(20, std::string("world"), 2.718);
// tuple2 holds (20, "world", 2.718). Types are explicitly specified.

// 3. Initialize using uniform initialization (C++11 and later):
std::tuple<int, std::string, double> tuple3 = {30, "example", 1.414};
// tuple3 holds (30, "example", 1.414).  Another initialization style.


 // Access elements, index is 0-based.
int firstElement = std::get<0>(tuple1); // Access the first element (index 0) - it's an int.
std::string secondElement = std::get<1>(tuple2); // Access the second element (index 1) - it's a std::string.

// type
using Tuple1Type = decltype(tuple1); // Get the type of tuple1

// size
constexpr size_t tuple1Size = std::tuple_size<Tuple1Type>::value; // tuple1Size is 3

// concatenate
auto tuplePart1 = std::make_tuple(1, 2);
auto tuplePart2 = std::make_tuple("part", "two");
auto combinedTuple = std::tuple_cat(tuplePart1, tuplePart2); 
// Access element from combined tuple.
std::cout << "Combined tuple element 0: " << std::get<0>(combinedTuple) << std::endl; 
std::cout << "Combined tuple element 2: " << std::get<2>(combinedTuple) << std::endl;

// Unpacking Tuples using tie
std::tuple<int, std::string, double> dataTuple = std::make_tuple(100, "data", 5.5);
int number;
std::string text;
double value;

// Unpack tuple elements into variables.
std::tie(number, text, value) = dataTuple; 
// number now holds 100, text holds "data", value holds 5.5

// Unpacking with structured bindings (C++17 and later - often cleaner)
auto personTuple = std::make_tuple("John", 30, "Engineer");
auto [name, age, job] = personTuple; 
// Structured binding - declare and initialize variables from tuple.
```

## pair
> Hold exactly two elements
**Key Features of std::pair**
- Holds Two Elements: A std::pair always contains two elements. No more, no less.
- Heterogeneous Types: The two elements in a std::pair can be of different data types. For example, you can have a pair containing an int and a std::string.
- Named Members: The elements of a std::pair are accessed using the names first and second. This makes the code readable and indicates the intended purpose of each element.
Automatic Generation of Operators: std::pair automatically gets relational operators defined for it (like ==, !=, <, >, <=, >=). These comparisons are lexicographical, meaning pairs are compared based on their first elements, and if the first elements are equal, then they are compared based on their second elements.
- Lightweight and Efficient: std::pair is very lightweight and efficient. It’s essentially just a simple structure to hold two values.

```cpp
#include <utility>

// declaration
std::pair<int, std::string> myPair; 

// declaration with value
std::pair<int, std::string> pair1(10, "Hello");

// declaration with make_pair
auto pair2 = std::make_pair(25, "World"); // Type is automatically deduced as std::pair<int, const char*>
auto pair3 = std::make_pair(3.14, true); 
std::pair<double, bool> pair4 = std::make_pair(1.618, false);  // explicit

// Uniform Initialization (C++11 and later - using curly braces {}):
std::pair<int, std::string> pair5 = {42, "Example"}; 
std::pair<int, std::string> pair6{100, "Another"};  // Direct list initialization


// Copy Initialization and Assignment:
std::pair<int, char> originalPair = std::make_pair(1, 'a');
std::pair<int, char> copiedPair = originalPair;  // Copy initialization
std::pair<int, char> assignedPair;
assignedPair = originalPair;                   // Assignment

// Access
std::pair<int, std::string> myData = std::make_pair(123, "Data Value");

int firstValue = myData.first;    // Accesses the first element (int)
std::string secondValue = myData.second; // Accesses the second element (std::string)

// Comparison
std::pair<int, std::string> pairA = std::make_pair(1, "apple");
std::pair<int, std::string> pairB = std::make_pair(1, "banana");
std::pair<int, std::string> pairC = std::make_pair(2, "apple");
std::pair<int, std::string> pairD = std::make_pair(1, "apple");

std::cout << std::boolalpha; // To print bool as true/false

std::cout << "pairA == pairB: " << (pairA == pairB) << std::endl; // Output: pairA == pairB: false
std::cout << "pairA == pairD: " << (pairA == pairD) << std::endl; // Output: pairA == pairD: true
std::cout << "pairA <  pairB: " << (pairA < pairB) << std::endl;  // Output: pairA <  pairB: true (because "apple" < "banana")
std::cout << "pairA <  pairC: " << (pairA < pairC) << std::endl;  // Output: pairA <  pairC: true (because 1 < 2, second elements are not checked)

// unpack
std::pair<int, std::string> dataPair = std::make_pair(500, "Pair Data");

auto [number, text] = dataPair; // Structured binding
```

## array parameters
```cpp
long function(vector<int>& numbers){}
```

- constant
```cpp 
const auto a
```

## map
[map vs unordered map](./complementary/map-vs-unorderedmap.md)
```cpp
#include <map>      // For std::map
#include <unordered_map> // For std::unordered_map

// Delaration ---
// Declare a map where keys are strings and values are integers (ordered map)
std::map<std::string, int> myMap;

// Declare an unordered_map with string keys and integer values (unordered map)
std::unordered_map<std::string, int> myUnorderedMap;


// Insertion
myMap["Alice"] = 30;           // Using operator[] (if key exists, it's updated)
myMap["Bob"] = 25;
myMap.insert({"Charlie", 35}); // Using insert with initializer list (C++11+)
myMap.insert(std::make_pair("David", 40)); // Using insert with std::pair

// Access & Lookup
int aliceAgeMap = myMap["Alice"]; // Access using operator[] (creates entry if key not found!)
// int eveAgeMap = myMap["Eve"];    // Be CAREFUL: if "Eve" doesn't exist, it will INSERT with default value (0 for int)!

int bobAgeMap = myMap.at("Bob");    // Access using .at() (throws exception if key not found)
// int eveAgeMapAt = myMap.at("Eve"); // Throws std::out_of_range exception if "Eve" is not in myMap

// Check if key exists BEFORE accessing (safer):
if (myMap.count("Alice")) {
    int safeAliceAgeMap = myMap["Alice"]; // Now it's safe to use operator[] because we checked count
    std::cout << "Alice's age in map: " << safeAliceAgeMap << std::endl;
}

auto itMap = myMap.find("Bob");      // Returns iterator to element if found, myMap.end() if not
if (itMap != myMap.end()) {
    std::cout << "Bob's age in map: " << itMap->second << std::endl; // Access value using iterator
}

// Iteration

// Iteration syntax is IDENTICAL.  The ORDER of iteration is the main difference.
// map: sorted by key; unordered_map: arbitrary.

// --- Iteration
std::cout << "Iterating through map (sorted order):" << std::endl;
for (const auto& pair : myMap) { // Range-based for loop (C++11+)
    std::cout << "Name: " << pair.first << ", Age: " << pair.second << std::endl;
    // 'pair' is a std::pair<const std::string, int>  (key is const string)
}

// Size
std::cout << "\nSize of map: " << myMap.size() << std::endl;

// reserve capacity for reallocation prevention and better performance
myMap.reserve(n)
```

