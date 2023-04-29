from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://jobs.bdjobs.com/jobsearch.asp?fcatId=8&icatId=').text
print(html_text)

soup = BeautifulSoup(html_text, 'lxml')
main = soup.find_all('div', class_='edu-text-d')
print(main)

print("____________________________________________")

education_list = []
for div in main:
    for li in div.find_all('li'):
        education_list.append(li.text.strip())

print(education_list)


