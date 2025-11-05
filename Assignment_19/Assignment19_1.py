import os
import sys

class DirectorySearch:

    def __init__(self):
        self.fobj = open("logfile.txt","w")

    def search(self, dirname, ex):
        try:
            if not os.path.isabs(dirname):
                dirname = os.path.abspath(dirname).split("\\")[0:-1]
                dirname = "\\".join(dirname)

            if not os.path.exists(dirname) and not os.path.isdir(dirname):
                print("The path is invalid")

            for FolderName, SubFolderNames, FileNames in os.walk(dirname):
                for file in FileNames:
                    if file.endswith(ex):
                        self.fobj.write(file+"\\")
        except Exception as e:
            print(e)


    def main(self):
        dirname = sys.argv[1]
        ex = sys.argv[2]
        self.search(dirname, ex)


if __name__ == "__main__":
    obj = DirectorySearch()
    obj.main()
