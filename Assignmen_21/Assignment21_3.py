import os.path
import psutil

class LogProcess:
    def validate_dir(self,dir):
        if not os.path.isabs(dir):
            dir = os.path.abspath(dir)

        if not os.path.exists(dir) and not os.path.isdir(dir):
            print("Invalid Path")

        # dir = dir.split("\\")[0:-1]
        # dir = "\\".join(dir)

        return dir

    def process_info(self,dir):
        fres = []
        for pro in psutil.process_iter():
            res = pro.as_dict(attrs=["name","pid"])
            fres.append(res)
        file_path = dir + "\logfile_3.txt"
        print(file_path)
        fobj = open(file_path,"w")
        fobj.write(str(fres))

    def main(self):
        print("Enter a diretory name : ")
        dir = input()
        dir = self.validate_dir(dir)
        self.process_info(dir)

if __name__ == "__main__":
    obj = LogProcess()
    obj.main()