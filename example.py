import time
from operations import ops

@ops
def my_operation(name, age):
    print(f"name: {name}")
    time.sleep(5)
    print(f"age: {age}")
    return None

my_operation("Elliot", 30)


# ERROR EXAMPLE
# @ops
# def my_operation(name, age):
#     print(f"name: {name}")
#     time.sleep(5)
#     raise Exception("Error message")
#     print(f"age: {age}")
#     return None

# my_operation("Elliot", 30)
