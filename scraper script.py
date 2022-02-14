from bs4 import BeautifulSoup
import requests
import time

for n in range(1092):
    page = requests.get("https://pasttenses.com/verbs-list/" + str(n+1))
    soup = BeautifulSoup(page.text, 'html.parser')

    for i in range(79):
        if (i+1) % 4 == 0:
            data = soup.find_all('td')[i].get_text()
            with open('verbs.txt', 'a', encoding="utf-16") as file:
                file.write(f'{str(data)}\n')

        else:
            data = soup.find_all('td')[i].get_text()
            with open('verbs.txt', 'a', encoding="utf-16") as file:
                file.write(f'{str(data)}|')

    with open('verbs.txt', 'a', encoding="utf-16") as file:  # adds page number and line break between each page
        file.write(f'{str(data)}\n{str(n+1)}\n\n')  # Also, the last string is added here
    time.sleep(0.01)  # short intervals between each request

print('Successfully finished!')