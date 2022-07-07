from subprocess import Popen

def main():
    p = Popen("test.bat", cwd= "D:\Tinghao.Chen\Desktop\diskTest")   #download_sourcecode.bat
    #p.stdout.readline()
    stdout, stderr = p.communicate()
    
    # with open("data.log", "w") as data:
    #     #for line in data.readline():
    #     data.write(p)

    # for line in iter(p.stdout.readline,''):
    #     print(line.rstrip())


if __name__ == "__main__":
    main()