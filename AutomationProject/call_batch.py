import subprocess
from subprocess import Popen

def main():
    p = subprocess.run("D:/Tinghao.Chen/Desktop/SMIGIT/AutomationProject/download_sourcecode.bat", stdout=subprocess.PIPE)   #D:\Tinghao.Chen\Desktop\SMIGIT\AutomationProject\download_sourcecode.bat
    str_List = str(p.stdout.decode('cp950')).split('\r\n\r\n')
    
    #print(str_List)

    

    #read batch file line by line (測試用)
    for i in str_List:
        #for j in i:
        print(i)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
    # i.replace("\r\n", "")  #替換特定字串用
    
    
    with open("data.log", "w") as dataWrite:
        for line in str_List:
            dataWrite.write(line)
            dataWrite.write("\n")


    # 問題: 很奇怪的是執行完call_batch.py之後，這個python檔的code會自動刪減掉with open()這一大段(會回溯到我一開始寫的那個版本)
    # 目前: 可以讀batch file，把裡面的資訊一行一行存取並寫入到data.log裡面



    
    # Read + Write to log file in this block (測試用)
    # with open("data.log", "r") as dataRead, open("data2.log", "w") as dataWrite:
    #     for line in dataRead:
    #         print(line)
    #         dataWrite.write(line)
    #     dataWrite.write("Writing file successful")
        
            

    


if __name__ == "__main__":
    main()