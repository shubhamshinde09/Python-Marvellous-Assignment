file = input("please enter file name : ")
string = input("please enter a string you want to find in the file : ")

fobj = open(file,"r").read()

re = fobj.count(string)
print(re)
