import os
import sys
import time
import hashlib
import schedule
import smtplib
from email.message import EmailMessage

def CalculateCheckSum(path, BlockSize = 1024):
    fobj = open(path,"rb")  # read in binary

    hobj = hashlib.md5()

    buffer = fobj.read(BlockSize)
    while(len(buffer) > 0 ):
        hobj.update(buffer)
        buffer = fobj.read(BlockSize)

    fobj.close()
    return hobj.hexdigest()

def DirectoryWatcher(DirectoryName = "Marvellous"):
     
     flag = os.path.isabs(DirectoryName)

     if(flag == False):
         DirectoryName = os.path.abspath(DirectoryName)

     flag = os.path.exists(DirectoryName)
     
     if(flag == False):
         print("The path is Invalid ")
         exit()

     flag = os.path.isdir(DirectoryName)

     if(flag == False):
         print("The path is valid but not Directory")
         exit()


     for FolderName , SubFolderNames,  Filenames in os.walk(DirectoryName):
        for fname in Filenames:
            fname = os.path.join(FolderName,fname)
            checksum = CalculateCheckSum(fname)     
            print("File name is",fname)
            print("Checksum is:",checksum)  
            print()     

     timestamp = time.ctime()

     filename = "marvellousLog%s.log" %(timestamp)
     filename = filename.replace(" ","_")
     filename = filename.replace(":","_")

    
     fobj = open(filename,"w")
     Border = "-"*54

     fobj.write(Border+"\n")
     fobj.write("This is the log file of Marvellous Automation Script\n")
     fobj.write("This is Directory Cleaner Script\n")

     fobj.write(Border+"\n")


     fobj.write("\n\n\n\n\n\n")
     

     #fobj.write("The Empty Count is:",EmptyCount,'\n')
     fobj.write("\n\n\n\n\n\n")

     fobj.write(Border+"\n")
     fobj.write("This file is created at:"+timestamp+"\n")
     fobj.write(Border+"\n")

          

def FindDuplicate(DirectoryName = "Marvellous"):
     
     flag = os.path.isabs(DirectoryName)

     if(flag == False):
         DirectoryName = os.path.abspath(DirectoryName)

     flag = os.path.exists(DirectoryName)
     
     if(flag == False):
         print("The path is Invalid ")
         exit()

     flag = os.path.isdir(DirectoryName)

     if(flag == False):
         print("The path is valid but not Directory")
         exit()
        
     Duplicate = {}

     for FolderName , SubFolderNames,  Filenames in os.walk(DirectoryName):
        for fname in Filenames:
            fname = os.path.join(FolderName,fname)
            checksum = CalculateCheckSum(fname)  

            if checksum in Duplicate:
                Duplicate[checksum].append(fname)
            else:
                Duplicate[checksum] = [fname]  

     return Duplicate 

def DisplayResult(MyDict):
    Result = list(filter((lambda x : len(x)>1), MyDict.values()))
    print(Result)
    count = 0
    for value in Result:
        for subvalue in value:
            count = count +1 
            print(subvalue)
        
        print("-------------------------------------------------")
        print("Count value is",count)
        print("-------------------------------------------------")
        count = 0

def DeleteDuplicate(path = "Marvellous"):
    
    MyDict = FindDuplicate(path)
    Result = list(filter((lambda x : len(x)>1), MyDict.values()))
    #print(Result)
    count = 0
    cnt = 0

    for value in Result:
        for subvalue in value:
            count = count +1 
            if(count>1):
                print("Deleted File ",subvalue)
                os.remove(subvalue)
                cnt = cnt +1
        count = 0
    print("Total Deleted Files",cnt)


def CreateLog(path , Email):
    
    MyDict = FindDuplicate(path)
    Result = list(filter(lambda X : len(X) > 1, MyDict.values()))
    timestamp = time.ctime()

    FileName = "MarvellousLog_%s.log" %(timestamp)
    FileName = FileName.replace(" ","_")
    FileName = FileName.replace(":","_")
    
    fobj = open(FileName,"w")


    Border = "-"*63

    fobj.write(Border+"\n")
    fobj.write("This is a log file of Marvellous Automation Script \n")
    fobj.write("This is a directory cleaner script used to delete duplicate files \n")
    fobj.write(Border+"\n")
    fobj.write("\n\n\n\n")

    Count = 0
    Cnt = 0

    for value in Result:
        for subValue in value:
            Count += 1
            if(Count > 1):
                fobj.write(subValue)
                fobj.write("\n")
                os.remove(subValue)
                Cnt += 1
        Count = 0
    fobj.write("Total deleted file : ")
    fobj.write(str(Cnt))
    fobj.write("\n\n\n\n")
    fobj.write(Border+"\n")
    fobj.write("This file is created at : "+timestamp +"\n")
    fobj.write(Border+"\n")
    fobj.close()
    print("Total deleted file :",Cnt)

    SendMail(Email, FileName)

def SendMail(recaiver_mail, LogFile):
    sender_mail = "coderjoy104@gmail.com"
    sender_password = "zmhj pzrc wulb kqve"

    body = "These are name of deleted files"
    # Create email
    msg = EmailMessage()
    msg['Subject'] = "Deleted Duplicate Files"
    msg['From'] = sender_mail
    msg['To'] = recaiver_mail
    msg.set_content(body)

    # Attach file
    fobj = open(LogFile, 'rb')
    msg.add_attachment(fobj.read(), maintype='application', subtype='octet-stream', filename=fobj.name)

    # Send email
    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp.login(sender_mail, sender_password)
    smtp.send_message(msg)
    smtp.quit()

    print("Email sent successfully!")
           
def main():
    Border = "-"*52
    print(Border)
    print("--------------Marvellous Automation-----------------")
    print(Border)
   
    if(len(sys.argv)== 2): 
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This Application Is Used To Perform directory Cleaning")
            print("This Is The Directory Automation Script")

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use The given Script as:")
            print("ScripName.py NameOfDirectory TimeInterval")
            print("Pleease Provide Valid Absolute path")

    if(len(sys.argv) == 4):
        schedule.every(int(sys.argv[2])).minutes.do( CreateLog, sys.argv[1], sys.argv[3])

        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        print("Invalid Number of Command line Arguments")
        print("Use the Given Flag As :")
        print("--h : Used to display help")
        print("--u : Used to display usage")

    print(Border)
    print("------------ Thank You For Using Our Script---------")
    print("--------------Marvellous Infosystems----------------")
    print(Border)


if __name__ == "__main__":
    main()