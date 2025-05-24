# Week 5: Python Classes & Exception Handling

Welcome to Week 5 of our Python programming course! This week we dive deep into **Object-Oriented Programming (OOP)** with classes and **Exception Handling** - two fundamental concepts that will make your code more organized, reusable, and robust.

## 📚 Learning Objectives

By the end of this week, students will be able to:

- **Classes & Objects:**
  - Define and create Python classes
  - Understand the difference between class and instance variables
  - Create and use instance methods
  - Implement constructors using `__init__()`
  - Apply basic OOP principles in real-world scenarios

- **Exception Handling:**
  - Understand different types of exceptions in Python
  - Use try-except blocks for error handling
  - Create custom exceptions for specific use cases
  - Implement proper error logging and user-friendly error messages
  - Handle multiple exception types gracefully

## 📁 Repository Structure

```
week5/
├── README.md                          # This file
├── dog_class.py                       # Complete beginner-friendly class example
├── error_handling_example_1.py       # Basic exception handling
├── error_handling_example_2.py       # Multiple exception types
├── custom_exception.py                # Creating custom exceptions
├── exception_with_logging.py          # Advanced custom exceptions
└── baseexception_catch_all.py         # Understanding BaseException
```

## 🐕 Classes Introduction

### What You'll Learn

Classes are blueprints for creating objects. Think of a class as a cookie cutter - you can use it to make many cookies (objects) with the same shape but different decorations (data).

**Key Concepts:**
- **Class**: The blueprint/template
- **Object/Instance**: The actual thing created from the blueprint
- **Attributes**: Data stored in the object (like name, age)
- **Methods**: Functions that belong to the class (like bark, sleep)

### Files to Study

#### 1. `dog_class.py` - Your First Complete Class
This file contains a comprehensive Dog class that demonstrates all the basics:

```python
class Dog:
    # Class variable (shared by all dogs)
    species = "Canis familiaris"
    
    def __init__(self, name, age, breed):
        # Instance variables (unique to each dog)
        self.name = name
        self.age = age
        self.breed = breed
        self.is_sleeping = False
    
    def bark(self):
        return f"{self.name} says: Woof! Woof!"
    
    def sleep(self):
        self.is_sleeping = True
        return f"{self.name} is now sleeping... Zzz"
```

**What to Practice:**
- Run the file and observe how different dog objects behave
- Try creating your own dogs with different names and breeds
- Experiment with calling different methods
- Notice how each dog maintains its own state

## 🛡️ Exception Handling

### What You'll Learn

Exception handling helps your programs deal with errors gracefully instead of crashing. It's like having a safety net for your code.

**Key Concepts:**
- **Exception**: An error that occurs during program execution
- **try-except**: The safety net that catches errors
- **Custom Exceptions**: Your own error types for specific situations
- **Error Logging**: Recording what went wrong for debugging

### Files to Study

#### 1. `error_handling_example_1.py` - Basic Error Handling
Simple division with error protection:
```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
```

#### 2. `error_handling_example_2.py` - Multiple Exception Types
Handling different types of errors:
```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Error: Please enter a valid number")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
```

#### 3. `custom_exception.py` - Creating Your Own Exceptions
```python
class NegativeException(Exception):
    """Custom exception for negative values."""
    pass

def check_positive(value):
    if value < 0:
        raise NegativeException("Negative value encountered.")
    return True
```

#### 4. `exception_with_logging.py` - Advanced Custom Exceptions
Enhanced custom exceptions with logging and suggestions:
```python
class NegativeException(Exception):
    def __init__(self, value, message="Negative value encountered."):
        self.value = value
        self.message = message
        super().__init__(self.message)

    def log_error(self):
        print(f"[LOG] Error logged for value: {self.value}")

    def suggest_fix(self):
        return f"Suggestion: Use abs({self.value}) = {abs(self.value)}"
```

#### 5. `baseexception_catch_all.py` - Understanding Exception Hierarchy
Learn about BaseException and when to use it:
```python
try:
    risky_operation()
except BaseException as e:
    print(f"Caught a base exception: {e}")
```

## 🎯 Practice Exercises

### Beginner Level
1. **Create a Student Class:**
   - Attributes: name, age, grade, subjects (list)
   - Methods: add_subject(), get_info(), promote_grade()

2. **Basic Exception Handling:**
   - Write a function that asks for user age and handles invalid input
   - Create a calculator that handles division by zero

### Intermediate Level
3. **Bank Account Class:**
   - Attributes: account_number, balance, owner_name
   - Methods: deposit(), withdraw(), get_balance()
   - Include error handling for insufficient funds

4. **Custom Exceptions:**
   - Create `InsufficientFundsException` for the bank account
   - Create `InvalidAgeException` for the student class

### Advanced Level
5. **Library Management System:**
   - Classes: Book, Member, Library
   - Include exception handling for book not found, member not found
   - Add logging for all operations

## 🔧 How to Run the Files

1. **Clone/Download** this repository
2. **Navigate** to the week5 directory
3. **Run each file** individually:
   ```bash
   python dog_class.py
   python error_handling_example_1.py
   python custom_exception.py
   # ... and so on
   ```

## 💡 Tips for Success

### For Classes:
- **Start Simple**: Begin with basic attributes and methods
- **Use Descriptive Names**: Make your class and method names clear
- **Think Real-World**: Model classes after real objects you understand
- **Practice**: Create multiple classes to understand the patterns

### For Exception Handling:
- **Be Specific**: Catch specific exceptions rather than using bare `except:`
- **Fail Gracefully**: Always provide meaningful error messages
- **Log Errors**: Keep track of what goes wrong for debugging
- **Test Edge Cases**: Try to break your code to find where exceptions occur

## 📝 Common Mistakes to Avoid

### Classes:
- ❌ Forgetting `self` in method definitions
- ❌ Not calling `super().__init__()` in inheritance
- ❌ Making everything a class (sometimes functions are better)
- ✅ Use classes when you need to maintain state and behavior together

### Exception Handling:
- ❌ Using bare `except:` without specifying exception type
- ❌ Ignoring exceptions silently (using `pass`)
- ❌ Catching exceptions too broadly
- ✅ Be specific about what exceptions you expect and handle them appropriately

## 🤝 Getting Help

If you're stuck or have questions:

1. **Read the code comments** - they explain what each part does
2. **Run the examples** - see the code in action
3. **Modify the examples** - change values and see what happens
4. **Ask questions** - during class or office hours
5. **Practice regularly** - coding is learned by doing!

## 📖 Additional Resources

- [Python Official Documentation - Classes](https://docs.python.org/3/tutorial/classes.html)
- [Python Official Documentation - Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Real Python - Object-Oriented Programming](https://realpython.com/python3-object-oriented-programming/)
- [Real Python - Exception Handling](https://realpython.com/python-exceptions/)

---

**Happy Coding! 🐍✨**

*Remember: The best way to learn programming is by writing code. Don't just read the examples - run them, modify them, and create your own!*
