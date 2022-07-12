import time
from datetime import datetime
c="hosts"
c2=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
site_list=["www.google.com", "www.facebook.com", "www.yahoo.com"]

while True:
    #print(datetime.now())
    if datetime( datetime.now().year,datetime.now().month,datetime.now().day,6,00 ) < datetime.now() < datetime( datetime.now().year,datetime.now().month,datetime.now().day,7,00 ):
        with open(c, 'r+')as file:
            content =file.read()
            print("its working hours")
            for website in site_list:
                if website in content:
                    pass
                else:
                    file.write("\n" +redirect+ " " + website)
        ##time.sleep(7)

    else:
        f = open(c, "r+")
        d = f.readlines()
        f.seek(0)
        for line in d:
            if not any(website in line for website in site_list):
                f.write(line)
        f.truncate()
        print("fun hours")
        time.sleep(5)


