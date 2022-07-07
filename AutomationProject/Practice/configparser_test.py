import configparser

#讀取ini
# config = configparser.ConfigParser()
# config.read("test.ini")

# host = config["http"]["host"]
# #port = config["http"]["port"]
# port = config["http"].getint("port")

# print(host)
# print(port)
# print(type(port))


#寫入ini
host = "https://www.google.com"
port = 87

config = configparser.ConfigParser()
config["http"] = {}
config["http"]["host"] = host
config["http"]["port"] = str(port)


with open("config.ini", mode = "w") as f:
    config.write(f)




