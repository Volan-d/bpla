import ftplib
ftp = ftplib.FTP()
host = '5.180.137.21'
port = 21
login = 'user'
passwd = 'user'

# функция загрузки на сервер
def ftp_upload(obj, path):
    with open(path, 'rb') as fobj:
        obj.storbinary('STOR ' + path, fobj, 1024)

try:
    connect_str = ftp.connect(host=host, port=port, timeout=10)
    ftp.login(user=login, passwd=passwd)
    ftp.cwd("V_Sedov")
    print(ftp.dir())
    ftp_upload(ftp, '2.txt') # тут полное имя своего файла!
    print(ftp.dir())
    ftp.close()
except:
        print("Error")
