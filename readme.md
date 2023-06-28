# :construction: Ops Package

This package provides a decorator for logging operations in a CSV file.

Despite being under development, this code is already functional and can be used in your projects.

### Advantages of using Ops Package
- Easy Logging: By simply decorating your functions with the @ops decorator, you can automatically log the execution of operations.
- CSV File Format: The operations are logged in a CSV file, which allows for easy data manipulation and analysis.
- Detailed Information: The logged information includes the date, start time, end time, process name, IP address, hostname, internet connection status, errors, execution time, and result of the operation.
- Error Handling: Any exceptions raised during the operation will be captured and logged, providing visibility into error occurrences.
- Customizable: You can easily extend or modify the functionality of the ops decorator and OpsRecorder class to suit your specific logging requirements.
- Please note that this library is still in development, and further improvements and features may be added in future updates.


## Usage
1. Clone the repository and copy the `operations` folder to your project directory.
```bash
git clone 
```

2. Import the `ops` decorator from the `operations` module:

```python
import time
from operations import ops

@ops
def my_operation(name, age):
    print(f"name: {name}")
    time.sleep(5)
    print(f"age: {age}")
    return None

# Call the function
my_operation("John", 25)
```
3. The operation will be logged in a CSV file with the following fields:
    - Date: The date when the operation was executed.
    - Start Time: The start time of the operation.
    - End Time: The end time of the operation.
    - Process: The name of the process.
    - IP: The IP address of the machine where the - operation was executed.
    - Hostname: The hostname of the machine where the operation was executed.
    - Connection: Indicates whether there is an internet connection (True/False).
    - Errors: Any errors that occurred during the operation.
    - Execution Time: The total execution time of the operation.
    - Result: The result of the operation.

## Error Handling
If an exception occurs during the execution of the decorated function, the error will be captured and logged automatically.

To test error handling, uncomment the following code block in the example:
```python
import time
from operations import ops

@ops
def my_operation(name, age):
    print(f"name: {name}")
    time.sleep(5)
    raise Exception("This is an error") # <-- Forced error
    print(f"age: {age}")
    return None

# Call the function
my_operation("John", 25)
```
This will intentionally raise an exception and log the error in the CSV file.

## Note
Make sure to create a "logs" folder in the same directory as your script before running the decorated function. The log files will be stored in this folder.