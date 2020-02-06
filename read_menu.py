import urllib.request
from tika import parser
import io


def get_day(data_array,day):

    cnt = 0
    for a in data_array:
        cnt += 1
        if day + " " in a:
            region = " ".join(a.strip().split(" ")[2:])
            break
    mahlzeit = data_array[cnt]
    zutaten = data_array[cnt+1].split("|")
    print(day + " - " + region)
    print("----------------")
    print(mahlzeit)
    print("zutaten:",end="")
    print(zutaten)
    print()


url = 'https://c338ed44-c4a4-4fd3-be99-0a60df83e515.filesusr.com/ugd/1d0033_88d07061f9144944a932c6c416038717.pdf'
file_name = 'menu.pdf'
urllib.request.urlretrieve(url, file_name)

raw = parser.from_file(file_name)
buff = io.StringIO(raw['content'])
data = buff.readlines()

temp_list = list()
for cnt,a in enumerate(data):
    line = a.replace("\n"," ").strip()
    if line != '':
        temp_list.append(line)


days_of_the_week = ["MONTAG","DIENSTAG","MITTWOCH","DONNERSTAG","FREITAG"]
for day in days_of_the_week:
    get_day(temp_list,day)