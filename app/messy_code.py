# messy_code.py


# Function with unused variable
def calculate_sum(numbers):
    total = sum(numbers)  # unused variable
    return sum(numbers)


# Mutable default argument (unsafe-fix can handle this)
def append_to_list(item, my_list=[]):
    my_list.append(item)
    return my_list


# Inconsistent string quotes (--fix can handle this)
name = "Alice"
greeting = "Hello"
message = "Welcome to " + "Python"

# Unnecessary f-string (--fix can handle this)
simple_string = "This is a simple string"

# Line too long (--fix can't fix the logic, only format it)
very_long_string = "This is an extremely long string that goes well beyond the recommended line length limit and would typically be flagged by most linters including Ruff"


# Extra whitespace at end of lines (--fix can handle this)
def whitespace_issues():
    print("Hello")
    return True


# Bare except clause (Ruff can't fix automatically)
try:
    result = 10 / 0
except:
    print("An error occurred")


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print(calculate_sum(numbers))
