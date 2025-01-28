Certainly! Here's a comprehensive explanation of **Object-Oriented Programming (OOP)** using **C++** with examples covering the four core principles: **Encapsulation**, **Inheritance**, **Polymorphism**, and **Abstraction**.

---

### **1. Encapsulation**  
**Bundling data and methods into a single unit (class) and controlling access via access modifiers.**  

#### **Example**:  
```cpp
#include <iostream>
using namespace std;

class BankAccount {
private: // Data is hidden (encapsulated)
    double balance;

public:
    // Constructor to initialize balance
    BankAccount(double initialBalance) : balance(initialBalance) {}

    // Public method to modify balance
    void deposit(double amount) {
        if (amount > 0) balance += amount;
    }

    // Public method to read balance
    double getBalance() const {
        return balance;
    }
};

int main() {
    BankAccount account(1000.0);
    account.deposit(500.0);
    cout << "Balance: $" << account.getBalance() << endl; // Balance: $1500
    return 0;
}
```
- **Key Points**:  
  - `balance` is `private` and can only be modified via public methods (`deposit`, `getBalance`).  
  - Protects data integrity (e.g., preventing negative deposits).  

---

### **2. Inheritance**  
**Creating hierarchical relationships between classes (base → derived).**  

#### **Example**:  
```cpp
#include <iostream>
using namespace std;

// Base class
class Vehicle {
protected:
    string brand;

public:
    Vehicle(string b) : brand(b) {}
    void honk() const {
        cout << "Honk honk!" << endl;
    }
};

// Derived class
class Car : public Vehicle {
private:
    int numDoors;

public:
    Car(string b, int doors) : Vehicle(b), numDoors(doors) {}
    void displayInfo() const {
        cout << "Brand: " << brand << ", Doors: " << numDoors << endl;
    }
};

int main() {
    Car myCar("Toyota", 4);
    myCar.honk();       // Inherited from Vehicle
    myCar.displayInfo(); // Brand: Toyota, Doors: 4
    return 0;
}
```
- **Key Points**:  
  - `Car` inherits `brand` and `honk()` from `Vehicle`.  
  - `protected` allows derived classes to access `brand`.  

---

### **3. Polymorphism**  
**Using a single interface to represent different underlying forms (e.g., overriding methods).**  

#### **Example (Runtime Polymorphism)**:  
```cpp
#include <iostream>
using namespace std;

// Base class with virtual function
class Shape {
public:
    virtual double area() const = 0; // Pure virtual function (abstract)
};

class Circle : public Shape {
private:
    double radius;

public:
    Circle(double r) : radius(r) {}
    double area() const override {
        return 3.14159 * radius * radius;
    }
};

class Rectangle : public Shape {
private:
    double width, height;

public:
    Rectangle(double w, double h) : width(w), height(h) {}
    double area() const override {
        return width * height;
    }
};

int main() {
    Shape* shapes[] = {new Circle(5), new Rectangle(4, 5)};

    for (Shape* shape : shapes) {
        cout << "Area: " << shape->area() << endl;
    }

    // Output:
    // Area: 78.5397
    // Area: 20
    return 0;
}
```
- **Key Points**:  
  - `virtual` enables dynamic binding (runtime polymorphism).  
  - `override` ensures the derived class correctly overrides the base method.  

---

### **4. Abstraction**  
**Hiding complex implementation details and exposing only essential features.**  

#### **Example (Abstract Class)**:  
```cpp
#include <iostream>
using namespace std;

// Abstract class with pure virtual function
class Animal {
public:
    virtual void makeSound() const = 0; // Pure virtual function
};

class Dog : public Animal {
public:
    void makeSound() const override {
        cout << "Woof!" << endl;
    }
};

class Cat : public Animal {
public:
    void makeSound() const override {
        cout << "Meow!" << endl;
    }
};

int main() {
    Animal* animals[] = {new Dog(), new Cat()};

    for (Animal* animal : animals) {
        animal->makeSound();
    }

    // Output:
    // Woof!
    // Meow!
    return 0;
}
```
- **Key Points**:  
  - `Animal` is abstract (cannot be instantiated).  
  - Derived classes **must** implement `makeSound()`.  

---

### **5. Key OOP Features in C++**  
| **Feature**       | **C++ Syntax**                          | **Purpose**                                   |
|--------------------|-----------------------------------------|-----------------------------------------------|
| **Class**          | `class MyClass { ... };`                | Blueprint for objects (data + methods).       |
| **Inheritance**    | `class Derived : public Base { ... };`  | Reuse and extend base class functionality.    |
| **Polymorphism**   | `virtual` and `override` keywords       | Dynamic method resolution at runtime.         |
| **Encapsulation**  | `private`, `public`, `protected`        | Control access to data and methods.           |
| **Abstraction**    | Pure virtual functions (`= 0`)          | Define interfaces without implementation.     |

---

### **Why OOP in C++?**  
1. **Modularity**: Break code into reusable classes.  
2. **Maintainability**: Isolate changes to specific classes.  
3. **Code Reuse**: Inheritance and composition reduce redundancy.  
4. **Real-World Modeling**: Objects map naturally to entities (e.g., cars, users).  

---

### **Summary**  
C++ implements OOP through:  
- **Classes** for encapsulation.  
- **Inheritance** for code reuse.  
- **Virtual functions** for polymorphism.  
- **Abstract classes** for abstraction.  

This paradigm helps build scalable, organized, and maintainable software systems. Let me know if you’d like to dive deeper into any concept! 🚀