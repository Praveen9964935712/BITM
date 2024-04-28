def greet():
    print("Hello from the sample_module!")

# If this script is executed directly, _name_ will be '_main_'
if _name_ == "_main_":
    print("This script is being run directly.")
    greet()
else:
    print("This script is being imported as a module.")