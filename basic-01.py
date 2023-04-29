from bs4 import BeautifulSoup

with open('profile.html', 'r', encoding='utf-8') as html_file:
    content = html_file.read()
    print(content)

    soup = BeautifulSoup(content, 'lxml')
    print(soup.prettify())

    tags1 = soup.find('h3')
    print("Tagging only 'h5' header html tag, here is the Raw Information: ", tags1)

    tags2 = soup.find_all('h3')
    print("Tagging only 'h5' header html tag, here is the Raw Information: \n", tags2)

    for tag in tags2:
        print(tag.text)