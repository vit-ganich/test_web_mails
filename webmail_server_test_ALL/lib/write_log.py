from datetime import datetime


def writeLog(test_name, message='Null'):   
    try: 
        time_now = datetime.today().strftime("%d.%m.%Y %H:%M:%S")
        with open(r'C:\Sikuli\log.txt','a') as f:
            f.write("%s %s %s\n" % (time_now, message, test_name))
    except:
        print("logging error")

if __name__ == "main":
    pass