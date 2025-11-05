import sys 



def copy_file_to_demo(source_file):
    try:
          with open(source_file, 'r') as src, open ("Demo.txt", 'w') as dest:
             dest.write(src.read())
          print(f"contents copied from {source_file} to Demo.txt successfully.") 
    except FileExistsError:
         print(f"Error : {source_file} not found .")
    except Exception as e:
         print("Error : ",e)


if __name__ == "__main__":
    if len(sys.argv)  !=2:
       print("Usage : python copy_to_demo.py <source_file>")
    else:
        copy_file_to_demo(sys.argv[1])  
