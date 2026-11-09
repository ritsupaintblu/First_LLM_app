import sys

print("Hello from my machine!")
if len(sys.argv) > 1:
    print("You passed:", sys.argv[1])