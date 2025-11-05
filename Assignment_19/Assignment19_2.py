import os
import sys

class CopyFiles:
    def __init__(self):
        self.fobj = open("logfile.txt","w")

    def copyfiles(self,dirname,ex1,ex2):
        if not os.path.isabs(dirname) :
            dirname = os.path.abspath(dirname)

        dirname = dirname.split("\\")[0:-1]
        dirname = "\\".join(dirname)

        if not os.path.exists(dirname) and not os.path.isdir(dirname):
            print("Invalid Path, please provide a correct path")

        for folder, subfolder, files in os.walk(dirname):
            for file in files:
                filename = os.path.join(folder,file)
                newfilename = filename.replace(ex1,ex2)
                if filename.endswith(ex1):
                    os.rename(filename,newfilename)
                    self.fobj.write("File Renamed : " + filename + "with extension : "+ex2)

    def main(self):
        dirname1 = sys.argv[1]
        ex1 = sys.argv[2]
        ex2 = sys.argv[3]
        self.copyfiles(dirname1,ex1,ex2)



if __name__ == "__main__":
    obj = CopyFiles()
    obj.main()
