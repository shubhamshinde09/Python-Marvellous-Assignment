import psutil

def process_info(pr_name):
    for pro in psutil.process_iter():
        if pro.name() == pr_name:
            print("Process is running,below is the information about the process")
            print(pro.as_dict())


def main():
    print("enter a process name : ")
    process_name = input()
    process_info(process_name)

if __name__ == "__main__":
    main()