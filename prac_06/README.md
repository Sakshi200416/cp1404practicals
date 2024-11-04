# Practical 06
# Practical 06: Classes and Object-Oriented Programming

This practical focuses on building a deeper understanding of Python classes, object-oriented programming, and how to encapsulate data and functionality within a class structure.

## Files and Descriptions

### 1. `car.py`
- **Description**: Contains the `Car` class, which models the basic behavior of a car, including fuel management and distance tracking.
- **Key Methods**:
  - `__init__()`: Initializes the car with a fuel level and other parameters.
  - `add_fuel(amount)`: Adds a specified amount of fuel.
  - `drive(distance)`: Simulates driving the car a certain distance, consuming fuel accordingly.
  - `__str__()`: Returns a formatted string representing the car's current state.

### 2. `used_cars.py`
- **Description**: Demonstrates and tests the `Car` class functionality.
- **Key Features**:
  - Creates instances of `Car` objects.
  - Manipulates and prints car properties using defined methods.

### 3. `programming_language.py`
- **Description**: Contains the `ProgrammingLanguage` class for modeling various properties of a programming language.
- **Key Methods**:
  - `__init__()`: Initializes the language's properties (name, typing type, reflection, and year).
  - `is_dynamic()`: Checks if the language is dynamically typed.
  - `__str__()`: Returns a formatted string describing the language.

### 4. `languages.py`
- **Description**: Uses the `ProgrammingLanguage` class to list programming languages with specific properties.
- **Key Features**:
  - Demonstrates the use of `is_dynamic()` to filter and display dynamically typed languages.

### 5. `guitar.py`
- **Description**: Defines the `Guitar` class to represent a guitar's name, year, and cost.
- **Key Methods**:
  - `__init__()`: Initializes the guitar with provided properties.
  - `get_age()`: Calculates the guitar's age.
  - `is_vintage()`: Checks if the guitar is vintage (50 or more years old).
  - `__str__()`: Provides a formatted string representation of the guitar.

### 6. `guitar_test.py`
- **Description**: A test script to verify the functionality of `get_age()` and `is_vintage()` methods from the `Guitar` class.
- **Key Features**:
  - Prints the expected and actual outputs for various test cases.

### 7. `guitars.py`
- **Description**: A program to input and manage a list of guitars, displaying them with relevant information.
- **Key Features**:
  - Collects user input for new guitars.
  - Displays a formatted list of owned guitars and indicates vintage status.

## Running the Programs

- To run each program, ensure you have Python installed and run the file from your terminal or IDE using:
  ```bash
  python <filename>.py

