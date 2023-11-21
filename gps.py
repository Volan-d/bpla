# # открываем файл для чтения
# with open('gps.txt') as f:
#     # читаем содержимое файла
#     gps_data = f.readlines()
#
#     # удаляем служебные символы
#     # Способ 1
#     # for i in range(len(gps_data)):
#     #     gps_data[i] = gps_data[i].strip()[1:-1]
#
#     # Способ 2
#     gps_data = list(map(lambda x: x.strip()[1:-1], gps_data))
#
#     # поиск строки с нужной информацией
#     for data in gps_data:
#         if 'RMC' in data:
#             # разбиваем строку на значения
#             RMC = data.split(',')
#             if RMC[2] == 'A':
#                 gps = dict()
#                 gps['gps_time'] = RMC[1][:2] + ' hour ' + RMC[1][2:4] + ' minutes ' + RMC[1][4:] + ' seconds'
#                 gps['lat'] = 'Lat: ' + RMC[3] + RMC[4]
#
#     print(gps)
#
import ftplib
ftp = ftplib.FTP()
host = '5.180.137.21'
port = 21
login = 'user'
passwd = 'user'

# функция загрузки на сервер
def ftp_upload(obj, path):
    with open(path, 'rb') as fobj:
        ftp.storbinary('STOR ' + path, fobj, 1024)

# функция выгрузки с сервера
def ftp_download(obj, ftp_path, local_path):
    with open(local_path, 'wb') as f:
        obj.retrbinary('RETR ' + ftp_path, f.write)

try:
    # подключение к серверу
    connect_str = ftp.connect(host=host, port=port, timeout=10)
    # Авторизация
    ftp.login(user=login, passwd=passwd)
    # получить содержимое каталога
    print(ftp.dir())
    # создать новый каталог
    # ftp.mkd("dir")
    # перейти в каталог
    # ftp.cwd("dir")
    # скачать файл
    ftp_download(ftp, 'kot.jpg', 'k2k.jpg')
    # загрузить файл
    # ftp_upload(ftp, 'kot.jpg')
    # удалить файл
    # ftp.delete('1.txt')
    # закрыть соединение
    # ftp.close()

except:
        print("Error")
