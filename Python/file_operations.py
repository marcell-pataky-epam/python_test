f = open('temp', 'w')

f.write("test string")

f.close()

f = open('temp', 'r')

print(f.readline())

f.close()

# with open("myfile.txt") as f:
#     for line in f:
#         print(line, end="")

# The with statement allows objects like files to be used in a way
# that ensures they are always cleaned up promptly and correctly.
