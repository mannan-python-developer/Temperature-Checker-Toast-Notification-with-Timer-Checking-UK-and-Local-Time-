# Simple Python Scripts


## Temperature Checking

This Python script checks the temperature of a specified location using web scraping.

```python
import requests
from bs4 import BeautifulSoup

place = input('Enter the Place: ')
search = f'Temperature in {place}'
url = f'https://www.google.com/search?&q={search}'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
temperature = soup.find('div', class_='BNeawe').text
print(f'{search} now is {temperature}')
```

### Uses and Working:
- It prompts the user to enter a place.
- It uses web scraping to fetch the current temperature of the specified place from Google search results.
- The temperature is then printed.
---

# Timer + Toast Notification
This Python script implements a countdown timer with a toast notification.

```python
import time
from win10toast import ToastNotifier

my_time = int(input('Enter the time in seconds: '))
for i in reversed(range(1, my_time)):
    sec = i % 60
    min = int(i / 60) % 60
    hrs = int(i / 3600)
    print(f'{hrs:02}:{min:02}:{sec:02}')
    time.sleep(1)

toaster = ToastNotifier()
toaster.show_toast("Python", "PLEASE FOCUS ON YOUR LAPTOP", duration=8)

print('TIME UP!!')
```
### Uses and Working:
- The user is prompted to enter a time duration in seconds.
- It counts down and displays the remaining time in HH:MM:SS format.
- A toast notification is shown to remind the user to focus.
- The script prints "TIME UP!!" when the countdown is complete.
---

# Time-related Python Scripts

## Our Local Time OR Current Time

The following Python script prints the current local time.

```python
import time
t = time.localtime()
time = time.strftime('%Y-%m-%d--%H:%M:%S', t)
print(time)
```
### Uses and Working:

- This script uses the time module to get the local time.
- It formats the time and prints it in the 'YYYY-MM-DD--HH:MM:SS' format.

## UK Time

This Python script calculates and prints the current time in the UK.

```python
import datetime
utc_time = datetime.datetime.utcnow()
uk_time = utc_time + datetime.timedelta(hours=1)
uk_time_str = uk_time.strftime("%H:%M:%S")
uk_date_str = uk_time.strftime("%Y-%m-%d")
print("Now Time in UK:", uk_time_str, 'and Date is:', uk_date_str)
```

### Uses and Working:

- It uses the datetime module to get the current UTC time.
- It adds one hour to the UTC time to get the UK time.
- The result is formatted and printed.

