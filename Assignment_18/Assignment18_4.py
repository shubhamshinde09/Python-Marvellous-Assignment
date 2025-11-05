import sys
file1 = sys.argv[1]
file2 = sys.argv[2]

f1 = open(file1,"r").read()
f2 = open(file2,"r").read()

if f1 == f2:
    print("Same content")
else:
    print("content is not same")

