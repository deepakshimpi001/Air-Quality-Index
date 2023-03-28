# module.py

def foo():
    print("Hello, world!")

print("Module name: ", __name__)

if __name__ == "__main__":
    print("This code will only be executed when the script is run directly, not when the module is imported.")
    foo()
