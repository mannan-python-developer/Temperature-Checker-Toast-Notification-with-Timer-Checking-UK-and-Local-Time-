############################### Our Local Time OR Current time #######################

import time
t = time.localtime()
time = time.strftime('%Y-%m-%d--%H:%M:%S', t)
print(time)


################################### UK Time #################################

import datetime
utc_time = datetime.datetime.utcnow()
uk_time = utc_time + datetime.timedelta(hours=1)
uk_time_str = uk_time.strftime("%H:%M:%S")
uk_date_str = uk_time.strftime("%Y-%m-%d")
print("Now Time in UK:", uk_time_str, 'and Date is:', uk_date_str)



###############################  For Tempreture Checking  ################################

import requests
from bs4 import BeautifulSoup
place = input('Enter the Place: ')
search = f'Tempreture in {place}'
url = f'https://www.google.com/search?&q={search}'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
update = soup.find('div', class_='BNeawe').text
print(f'{search} now is {update}')



################################# Timer + Toast notification ###############################

import time
my_time = int(input('Enter the time in seconds: '))
for i in reversed(range(1, my_time)):
    sec = i % 60
    min = int(i / 60)%60
    hrs = int(i / 3600)
    print(f'{hrs:02}:{min:02}:{sec:02}')
    time.sleep(1)

from win10toast import ToastNotifier
toaster = ToastNotifier()
toaster.show_toast("Python", "PLEASE FOCUS ON YOUR LAPTOP", duration=8)

print('TIME UP!!')
