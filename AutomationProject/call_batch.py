import subprocess
from subprocess import Popen
import time

real_time = time.strftime("%Y%m%d_%H%M%S", time.localtime())

def main():
    # Open and read batch file
    p = subprocess.run("D:/Tinghao.Chen/Desktop/SMIGIT/AutomationProject/download_sourcecode.bat", stdout=subprocess.PIPE)   
    str_List = str(p.stdout.decode('cp950')).split('\r\n\r\n')  # i.replace("\r\n", "")  #替換特定字串用
    
    # Write batch output into data.log (寫入)
    with open("data.log", "w") as dataWrite:
        print("Writing str_List into data.log")
        for line in str_List:
            dataWrite.write(line)
            dataWrite.write("\n")


    # Print SHA code of the data.log
    with open("data.log", "r") as dataRead:
        print("Reading SHA code")
        dataSHA = dataRead.readlines()[19]  # Read the specific line (SHA code)
    
    # Write the SHA code into Debug_log file 
    with open(real_time + "_Debug_log.log", "w") as dataWrite:
        print("SHA code is written into Degub_log")
        dataWrite.write(dataSHA)


if __name__ == "__main__":
    main()





    
    # read batch file line by line (測試用)
    # for i in str_List:
    #     print(i)
    #     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Read + Write to log file in this block (測試用)
    # with open("data.log", "r") as dataRead, open("data2.log", "w") as dataWrite:
    #     for line in dataRead:
    #         print(line)
    #         dataWrite.write(line)
    #     dataWrite.write("Writing file successful")