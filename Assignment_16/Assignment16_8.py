# Task 8
infile = input("Enter input file name: ")
outfile = input("Enter output file name: ")

try:
    fin = open(infile, "r")
    fout = open(outfile, "w")
    for line in fin:
        if line.strip() != "":
            fout.write(line)
    print("Blank lines removed.")
    fin.close()
    fout.close()
except FileNotFoundError:
    print("Input file not found.")
