import os
import sys
import hashlib


class DirectoryDuplicates:
    def __init__(self):
        self.lobj = open("asg3_logfile.txt","w")

    def __del__(self):
        self.lobj.close()

    def validatedir(self,dir,filename=None):
        if not os.path.isabs(dir):
            dir = os.path.abspath(dir)

        if not os.path.exists(dir) and not os.path.isdir(dir):
            print("Invalidate path")

        dir = dir.split("\\")[0:-1]
        dir = "\\".join(dir)
        return True

    def findchecksum(self,dirname):
        resdir = {}
        for folder,sf,files in os.walk(dirname):
            for file in files:
                algo = hashlib.md5()
                filename = os.path.join(folder,file)
                fobj = open(filename,"rb")
                buffer = fobj.read(1000)
                while len(buffer) > 0:
                    algo.update(buffer)
                    buffer = fobj.read(1000)
                fobj.close()
                chksum =algo.hexdigest()
                if chksum in resdir:
                    resdir[chksum].append(filename)
                else:
                    resdir[chksum] = [filename]
        return resdir

    def find_deleteduplicate(self,res):
        duplicatefilecount = 0
        totalduplicatefilecount = 0
        for chksum,filenames in res.items():
            for file in filenames:
                duplicatefilecount = duplicatefilecount + 1
                if duplicatefilecount > 1:
                    os.remove(file)
                    self.lobj.write(file)
                    totalduplicatefilecount = totalduplicatefilecount +1
            duplicatefilecount = 0
        print("Total deleted files : ",totalduplicatefilecount)

    def writelogs(self,res):
        try:
            self.lobj.write(res)
        except Exception as e:
            print(e)

    def main(self):
        dir = sys.argv[1]
        if self.validatedir(dir):
            res = self.findchecksum(dir)
            self.find_deleteduplicate(res)
#


if __name__ == "__main__":
    obj = DirectoryDuplicates()
    obj.main()