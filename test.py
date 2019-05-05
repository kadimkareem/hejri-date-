
import requests
from bs4 import BeautifulSoup as bs

url="https://datehijri.com/en/"
result=requests.get(url)
print(result.status_code)

print(result.headers)


src=result.content

new_table=[]
soup=bs(src)
table = soup.find_all('table')[0] # Grab the first table
for tr in table:
    tr.find_all('tr')

    print('\n')

    for td in tr:
        td.find_all('td')
        new_table.append(td.text)
        print(td.text)


