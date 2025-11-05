import psutil

def process_info():
    for pro in psutil.process_iter():
        res = pro.as_dict(attrs=["name","pid","username"])
        print(res)

def main():
    process_info()

if __name__ == "__main__":
    main()