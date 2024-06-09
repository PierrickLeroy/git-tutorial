# file: module1.py
"file: module1.py"

print("Running module1.py")
print(f"__file__={__file__} in module1.py")

X = 24

def say_hi():
    """module1.py say_hi() function"""
    print("Hi from module1.py")
    print(f"__file__={__file__} in say_hi()")
