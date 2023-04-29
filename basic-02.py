from bs4 import BeautifulSoup

with open('home.html', 'r', encoding='utf-8') as html_file:
    content = html_file.read()
    print(content)

    soup = BeautifulSoup(content, 'lxml')
    print(soup.prettify())

    tags1 = soup.find_all('div', class_='card')
    for course in tags1:
        tag_name = course.h5.text
        course_price1 = course.a
        course_price2 = course.a.text.split()[-1] # looking for last element
        print(tag_name)
        print(course_price1.text)
